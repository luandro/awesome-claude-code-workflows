# Awesome Claude Code [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, workflows, configurations, and resources for enhancing Claude Code productivity

[Claude Code](https://docs.anthropic.com/claude-code) is Anthropic's agentic coding assistant that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

## Contents

- [Official Resources](#official-resources)
- [Development Environments & Docker](#development-environments--docker)
- [Guides & Best Practices](#guides--best-practices)
- [Project Management & Workflows](#project-management--workflows)
- [Configuration & Setup Tools](#configuration--setup-tools)
- [Terminal & CLI Enhancements](#terminal--cli-enhancements)
- [Authentication & OAuth](#authentication--oauth)
- [Agent Orchestration & Parallel Execution](#agent-orchestration--parallel-execution)
- [Learning Resources](#learning-resources)
- [Community & Collections](#community--collections)

## Official Resources

- **[Claude Code Documentation](https://docs.anthropic.com/claude-code)** - Official Anthropic documentation
- **[Claude Code GitHub](https://github.com/anthropics/claude-code)** - Official repository (30.8k⭐)
- **[Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)** - Comprehensive guide by Anthropic engineering team covering workflows, customization, and advanced patterns

## Development Environments & Docker

### ClaudeBox
- **Repository**: [RchGrav/claudebox](https://github.com/RchGrav/claudebox)
- **Stars**: 402⭐
- **Description**: The Ultimate Claude Code Docker Development Environment with pre-configured development profiles
- **Key Features**:
  - Containerized environment with 15+ language profiles (Python, Rust, Go, C/C++, etc.)
  - Project isolation with separate Docker images per project
  - Persistent configuration and Python virtual environments
  - Tmux integration for multi-pane workflows
  - Built-in security with network isolation
- **Strengths**: Production-ready containerization, excellent isolation, cross-platform support
- **Maintenance**: Active (last updated July 2025)
- **Best for**: Teams wanting containerized, reproducible development environments

### SuperClaude Framework
- **Repository**: [SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- **Description**: Configuration framework that enhances Claude Code with specialized commands, cognitive personas, and development methodologies
- **Key Features**:
  - 16 specialized commands for common dev tasks
  - MCP server integration (Context7, Sequential, Magic, Playwright)
  - Cognitive personas and development methodologies
  - Component-based installation system
- **Status**: Active development (V4 Beta)
- **Best for**: Developers wanting pre-built command sets and personas

## Guides & Best Practices

### Complete Command Reference
- **Repository**: [zebbern/claude-code-guide](https://github.com/zebbern/claude-code-guide)
- **Stars**: 1.8k⭐
- **Description**: Most complete Claude Code command reference available as of August 2025
- **Key Features**:
  - Every discoverable Claude Code command documented
  - Installation guides for Windows, Linux, macOS
  - MCP integration overview
  - Security & permissions best practices
  - Automation & scripting examples
- **Strengths**: Comprehensive documentation, regularly updated, practical examples
- **Best for**: New users wanting complete command reference

### Context Engineering Theory
- **Repository**: [davidkimai/Context-Engineering](https://github.com/davidkimai/Context-Engineering)
- **Stars**: 5.8k⭐ 
- **Description**: Advanced handbook moving beyond prompt engineering to context design and optimization
- **Key Features**:
  - Progressive learning from atoms→molecules→cells→organs→neural systems
  - Research-backed with 1400+ papers surveyed
  - Support for Claude Code and other AI tools
  - Mathematical foundations and practical applications
- **Strengths**: Deep theoretical foundation, research-backed, comprehensive
- **Maintenance**: Very active (daily updates)
- **Best for**: Advanced users wanting deep understanding of context engineering

## Project Management & Workflows

### Spec-Driven Development
- **Repository**: [Pimzino/claude-code-spec-workflow](https://github.com/Pimzino/claude-code-spec-workflow)
- **Description**: Automated workflows featuring spec-driven development (Requirements → Design → Tasks → Implementation)
- **Key Features**:
  - Complete feature development workflow
  - Requirements generation and validation
  - Task decomposition and automation  
  - Sub-agent orchestration
- **Status**: Evolved to MCP version (spec-workflow-mcp)
- **Best for**: Structured feature development with clear specifications

### Claude Code Project Management (CCPM)
- **Repository**: [automazeio/ccpm](https://github.com/automazeio/ccpm)
- **Stars**: 1.1k⭐
- **Description**: Battle-tested project management system using GitHub Issues and Git worktrees for parallel agent execution
- **Key Features**:
  - PRD → Epic → Tasks → GitHub Issues workflow
  - Parallel agent execution with worktrees
  - GitHub Issues as single source of truth
  - Complete audit trail and traceability
- **Strengths**: Production-tested, excellent documentation, team collaboration focus
- **Maintenance**: Active (August 2025)
- **Best for**: Teams wanting structured PM with GitHub integration

### Task Delegation System
- **Repository**: [GitHub Gist](https://gist.github.com/worksfornow/df0cb6c4f6fd4966cd17133bc711fd20)
- **Description**: Lightweight slash command for delegating multiple tasks in parallel using tmux, git worktrees, and markdown prompts
- **Key Features**:
  - Task Master Agent Spawner
  - Automatic worktree creation
  - Tmux session management
  - Task status tracking
- **Best for**: Solo developers wanting simple parallel task execution

## Configuration & Setup Tools

### Production Configuration Collections
- **Repository**: [Matt-Dionis/claude-code-configs](https://github.com/Matt-Dionis/claude-code-configs)
- **Description**: Comprehensive collection of production-grade Claude Code configurations for different tech stacks
- **Key Features**:
  - Next.js 15, shadcn/ui, MCP server configurations
  - Dynamic config generator (Claude Config Composer)
  - Specialized agents for different domains
  - Production-ready hooks and automation
- **Strengths**: Real-world tested, covers popular frameworks, excellent documentation
- **Maintenance**: Active (August 2025)
- **Best for**: Developers wanting battle-tested configurations

### Claude Code Settings Collection
- **Repository**: [feiskyer/claude-code-settings](https://github.com/feiskyer/claude-code-settings)
- **Description**: Curated settings and commands for "vibe coding" workflows
- **Key Features**:
  - Kiro workflow implementation
  - GitHub Copilot API proxy integration
  - Custom slash commands
  - Analysis and reflection tools
- **Best for**: Developers wanting predefined workflow patterns

## Terminal & CLI Enhancements

### Terminal Automation Tools
- **Repository**: [pchalasani/claude-code-tools](https://github.com/pchalasani/claude-code-tools)
- **Description**: Collection of practical tools for enhancing Claude Code with terminal automation
- **Key Features**:
  - tmux-cli for terminal automation ("Playwright for terminals")
  - Interactive CLI application control
  - Claude-to-Claude communication
  - Environment file management (vault, env-safe)
- **Strengths**: Solves real pain points, well documented, practical
- **Maintenance**: Active (August 2025)  
- **Best for**: Developers needing terminal automation and CLI interaction

## Authentication & OAuth

### OAuth Authentication for GitHub Actions
- **Repository**: [grll/claude-code-login](https://github.com/grll/claude-code-login)
- **Description**: OAuth 2.0 authentication tool for Claude Code with GitHub Actions integration
- **Key Features**:
  - OAuth 2.0 + PKCE authentication
  - GitHub Actions workflow ready
  - Automatic token refresh
  - Max subscription support
- **Status**: Made obsolete by native Anthropic OAuth support (July 2025)
- **Best for**: Historical reference (superseded by official solution)

## Agent Orchestration & Parallel Execution

### 24/7 Autonomous Agents
- **Repository**: [Jedward23/Tmux-Orchestrator](https://github.com/Jedward23/Tmux-Orchestrator)
- **Description**: Run AI agents 24/7 with autonomous scheduling, coordination across multiple projects
- **Key Features**:
  - Three-tier hierarchy (Orchestrator → Project Managers → Engineers)
  - Self-triggering agent check-ins
  - Context window management
  - Persistent work continuation
- **Architecture**: Solves context limitations with role separation
- **Best for**: Long-running autonomous development projects

## Learning Resources

### Official Course
- **Course**: [Claude Code: A Highly Agentic Coding Assistant](https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/)
- **Provider**: DeepLearning.AI (in partnership with Anthropic)
- **Instructor**: Elie Schoppik (Head of Technical Education at Anthropic)
- **Duration**: 1 hour 50 minutes, 10 lessons
- **Content**:
  - Best practices and advanced patterns
  - MCP server integration (Playwright, Figma)
  - GitHub integration and automation
  - Multi-session parallel development
- **Best for**: Comprehensive understanding of Claude Code capabilities

## Community & Collections

### Awesome Claude Code Collection
- **Repository**: [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)
- **Description**: Curated list of slash-commands, CLAUDE.md files, CLI tools, and resources
- **Focus**: Community-driven resource collection
- **Best for**: Discovering community-created resources

### Topic Collections
- **GitHub Topics**: 
  - [claude-code](https://github.com/topics/claude-code) - 30+ repositories
  - [claude-code-guide](https://github.com/topics/claude-code-guide) - Tips and optimization guides

## Getting Started Recommendations

### For Beginners
1. Start with the **[Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)** by Anthropic
2. Use **[zebbern/claude-code-guide](https://github.com/zebbern/claude-code-guide)** for complete command reference
3. Take the **[DeepLearning.AI course](https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/)** for structured learning

### For Intermediate Users
1. Explore **[Matt-Dionis/claude-code-configs](https://github.com/Matt-Dionis/claude-code-configs)** for production configurations
2. Try **[pchalasani/claude-code-tools](https://github.com/pchalasani/claude-code-tools)** for terminal enhancements
3. Implement structured workflows with **[automazeio/ccpm](https://github.com/automazeio/ccpm)**

### For Teams & Advanced Users
1. Deploy **[ClaudeBox](https://github.com/RchGrav/claudebox)** for containerized team environments
2. Study **[Context Engineering](https://github.com/davidkimai/Context-Engineering)** for advanced theory
3. Experiment with **[Tmux-Orchestrator](https://github.com/Jedward23/Tmux-Orchestrator)** for autonomous agents

## Contributing

Contributions are welcome! Please read the [contribution guidelines](https://github.com/sindresorhus/awesome/blob/main/contributing.md) first.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.