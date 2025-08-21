#!/usr/bin/env python3
import os
import re
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from typing import Optional, List, Set, Tuple, Dict


README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")


GITHUB_REPO_URL_RE = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)(?:\b|/|\))")


def format_stars(n: int) -> str:
    if n >= 1_000_000:
        s = f"{n/1_000_000:.1f}m"
    elif n >= 1000:
        s = f"{n/1000:.1f}k"
    else:
        s = str(n)
    # Trim trailing .0
    if s.endswith(".0k"):
        s = s.replace(".0k", "k")
    if s.endswith(".0m"):
        s = s.replace(".0m", "m")
    return s


def fetch_stars(owner: str, repo: str, token: Optional[str]) -> Optional[int]:
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"User-Agent": "star-updater-script"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(api_url, headers=headers)
    try:
        with urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return int(data.get("stargazers_count", 0))
    except HTTPError as e:
        print(f"HTTP error fetching {owner}/{repo}: {e}")
    except URLError as e:
        print(f"URL error fetching {owner}/{repo}: {e}")
    except Exception as e:
        print(f"Unexpected error fetching {owner}/{repo}: {e}")
    return None


STAR_LINE_RE = re.compile(r"(\*\*Stars\*\*:\s*)([0-9]+(?:\.[0-9])?[kKmM]?)(\s*⭐)")
OFFICIAL_REPO_RE = re.compile(r"(Official repository\s*\()(?:[0-9]+(?:\.[0-9])?[kKmM]?)(⭐\))")


def update_lines_for_repo(lines: List[str], link_idx: int, new_star_text: str, updated_indices: Set[int]) -> bool:
    """
    Given a link occurrence at lines[link_idx], search a small window around it
    to update either a "Stars: X⭐" line or an "Official repository (X⭐)" fragment.
    Returns True if an update was made.
    """
    changed = False
    start = max(0, link_idx - 2)
    end = min(len(lines), link_idx + 6)
    for j in range(start, end):
        if j in updated_indices:
            continue
        line = lines[j]
        # Case 1: explicit Stars line
        m = STAR_LINE_RE.search(line)
        if m:
            new_line = STAR_LINE_RE.sub(lambda mo: mo.group(1) + new_star_text + mo.group(3), line)
            if new_line != line:
                lines[j] = new_line
                updated_indices.add(j)
                changed = True
                break
        # Case 2: Official repository (X⭐)
        m2 = OFFICIAL_REPO_RE.search(line)
        if m2:
            # Replace inside parentheses, preserving trailing '⭐)'
            new_line = OFFICIAL_REPO_RE.sub(lambda mo: mo.group(1) + new_star_text + mo.group(2), line)
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

    # Gather all repo occurrences with their line indices
    occurrences: List[Tuple[int, str, str]] = []  # (line_idx, owner, repo)
    for idx, line in enumerate(lines):
        for m in GITHUB_REPO_URL_RE.finditer(line):
            owner, repo = m.group(1), m.group(2)
            occurrences.append((idx, owner, repo))

    # Deduplicate fetches
    unique_repos: List[Tuple[str, str]] = []
    seen: Set[str] = set()
    for _, owner, repo in occurrences:
        key = f"{owner}/{repo}"
        if key not in seen:
            seen.add(key)
            unique_repos.append((owner, repo))

    # Fetch star counts
    stars_by_repo: Dict[str, str] = {}
    for owner, repo in unique_repos:
        count = fetch_stars(owner, repo, token)
        if count is None:
            continue
        stars_by_repo[f"{owner}/{repo}"] = format_stars(count)

    # Apply updates near each occurrence
    updated_indices: Set[int] = set()
    any_changed = False
    for idx, owner, repo in occurrences:
        key = f"{owner}/{repo}"
        if key not in stars_by_repo:
            continue
        star_text = stars_by_repo[key]
        if update_lines_for_repo(lines, idx, star_text, updated_indices):
            any_changed = True

    if not any_changed:
        print("No star counts updated. README already up to date or no stars found.")
        return 0

    new_content = "\n".join(lines) + ("\n" if content.endswith("\n") else "")
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README.md star counts updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
