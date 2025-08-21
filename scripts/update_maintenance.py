#!/usr/bin/env python3
import os
import re
import json
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from typing import Optional, List, Set, Tuple


README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")


GITHUB_REPO_URL_RE = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)(?:\b|/|\))")
MAINT_LINE_RE = re.compile(r"(\*\*Maintenance\*\*:\s*)(.*)")


def github_api_get(url: str, token: Optional[str]) -> Optional[dict]:
    headers = {"User-Agent": "maintenance-updater-script"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(url, headers=headers)
    try:
        with urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        print(f"HTTP error fetching {url}: {e}")
    except URLError as e:
        print(f"URL error fetching {url}: {e}")
    except Exception as e:
        print(f"Unexpected error fetching {url}: {e}")
    return None


def classify_status(days: int) -> str:
    if days <= 30:
        return "Very active"
    if days <= 90:
        return "Active"
    if days <= 180:
        return "Occasionally updated"
    if days <= 365:
        return "Stale"
    return "Inactive"


def last_commit_date(owner: str, repo: str, token: Optional[str]) -> Optional[datetime]:
    repo_data = github_api_get(f"https://api.github.com/repos/{owner}/{repo}", token)
    if not repo_data:
        return None

    # Prefer explicit 'main' if exists, else fallback to default_branch
    branch = "main"
    # Attempt to fetch main; if fails, fallback later
    commit_data = github_api_get(
        f"https://api.github.com/repos/{owner}/{repo}/commits/{branch}", token
    )
    if not commit_data or "commit" not in commit_data:
        branch = repo_data.get("default_branch", "main")
        commit_data = github_api_get(
            f"https://api.github.com/repos/{owner}/{repo}/commits/{branch}", token
        )
        if not commit_data or "commit" not in commit_data:
            # Fallback to repo pushed_at if available
            pushed_at = repo_data.get("pushed_at")
            if pushed_at:
                try:
                    return datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
                except Exception:
                    return None
            return None

    date_str = (
        commit_data.get("commit", {})
        .get("committer", {})
        .get("date")
        or commit_data.get("commit", {}).get("author", {}).get("date")
    )
    if not date_str:
        return None
    try:
        return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    except Exception:
        return None


def update_lines_for_repo(lines: List[str], link_idx: int, status_text: str, updated_indices: Set[int]) -> bool:
    changed = False
    start = max(0, link_idx - 3)
    end = min(len(lines), link_idx + 20)
    for j in range(start, end):
        if j in updated_indices:
            continue
        line = lines[j]
        m = MAINT_LINE_RE.search(line)
        if m:
            new_line = MAINT_LINE_RE.sub(lambda mo: mo.group(1) + status_text, line)
            if new_line != line:
                lines[j] = new_line
                updated_indices.add(j)
                changed = True
                break
    return changed


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    # Find repo link occurrences
    occurrences: List[Tuple[int, str, str]] = []
    for idx, line in enumerate(lines):
        for m in GITHUB_REPO_URL_RE.finditer(line):
            occurrences.append((idx, m.group(1), m.group(2)))

    # Dedup repos
    seen: Set[str] = set()
    unique: List[Tuple[str, str]] = []
    for _, owner, repo in occurrences:
        key = f"{owner}/{repo}"
        if key not in seen:
            seen.add(key)
            unique.append((owner, repo))

    # Fetch last commit dates
    last_dates = {}
    for owner, repo in unique:
        dt = last_commit_date(owner, repo, token)
        if dt:
            last_dates[f"{owner}/{repo}"] = dt

    # Apply updates
    updated_indices: Set[int] = set()
    any_changed = False
    now = datetime.now(timezone.utc)
    for idx, owner, repo in occurrences:
        key = f"{owner}/{repo}"
        if key not in last_dates:
            continue
        dt = last_dates[key]
        days = max(0, (now - dt).days)
        status = classify_status(days)
        status_text = f"{status} (last commit {dt.date()})"
        if update_lines_for_repo(lines, idx, status_text, updated_indices):
            any_changed = True

    if not any_changed:
        print("No maintenance lines updated. README already up to date or no matches.")
        return 0

    new_content = "\n".join(lines) + ("\n" if content.endswith("\n") else "")
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README.md maintenance statuses updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
