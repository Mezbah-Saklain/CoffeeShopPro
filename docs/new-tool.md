# New Tool — GitHub Actions (CI/CD)

## 1. What I Chose and Why

I chose **GitHub Actions** as my new tool for Continuous Integration (CI). It
automatically runs my test suite on every push and pull request, guaranteeing
the code in `main` never breaks.

## 2. Comparison with Alternatives

| Tool | Why I rejected it |
|---|---|
| **Jenkins** | Requires a dedicated server, plugin installation, and ongoing maintenance — too heavy for a solo one-day project. |
| **GitLab CI** | Would require migrating my repository off GitHub; the project already lives on GitHub. |
| **Travis CI** | Reduced free tier; GitHub Actions is more tightly integrated with my repo. |

**Why GitHub Actions:** zero-server, free for public repositories, integrated
directly with GitHub where my code already lives, and configured with a single
YAML file.

## 3. How It Is Used in the Project

The file `.github/workflows/ci.yml` defines the pipeline:
- Triggers on every `push` and every `pull_request` to `main`.
- Runs on a fresh Ubuntu VM with Python 3.11.
- Installs `coverage` and runs the entire test suite.
- Fails the pipeline if any test fails.

## 4. Evidence

- The CI badge in the README reflects live pipeline status.
- Screenshots of the first successful run and the merged PR will be captured
  after the workflow completes (see GitHub Actions tab).

## 5. What This Demonstrates

GitHub Actions turns testing from "something I run manually" into a **gate** —
no code merges to `main` unless its tests pass. This directly satisfies the lab
requirement of "tests passing in CI."