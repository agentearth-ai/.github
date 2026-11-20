# Contributing to AgentEarth

Thanks for your interest in contributing! This guide applies to every repository in the `agentearth-ai` organization. A repository may add its own `CONTRIBUTING.md` with extra rules; where they differ, the repository's own guide wins.

## Before you start

- **Small fixes** (typos, docs, obvious bugs): open a pull request directly.
- **Larger changes** (new features, behavior changes, new integrations): open an issue first so we can agree on the approach before you spend time on it.
- Search existing issues and pull requests to avoid duplicates.

## Pull request workflow

1. Fork the repository and create a branch from `main`.
2. Make your change. Keep each pull request focused on one thing.
3. Add or update tests and docs where it makes sense.
4. Make sure the repository's checks pass locally (see its README).
5. Sign off your commits (see below) and open a pull request using the template.

A maintainer will review your pull request. We may ask for changes; please don't take it personally — we want every contribution to land in good shape.

## Sign off your commits (DCO)

We use the [Developer Certificate of Origin](https://developercertificate.org/). By signing off, you certify that you wrote the change or otherwise have the right to submit it under the repository's license.

Add a sign-off line to every commit with `-s`:

```sh
git commit -s -m "fix: handle empty tool result"
```

This appends `Signed-off-by: Your Name <your@email>` to the commit message. Pull requests with unsigned commits can't be merged.

## Commit messages

We recommend [Conventional Commits](https://www.conventionalcommits.org/), e.g. `feat: ...`, `fix: ...`, `docs: ...`.

## Never commit secrets

Do **not** commit API keys, tokens, passwords, or personal data — including your AgentEarth API key — in code, tests, examples, screenshots, or issue logs. Use environment variables and placeholders such as `YOUR_API_KEY`. If you committed a secret by accident, rotate it right away and let us know.

## License

Unless a repository states otherwise, contributions are accepted under that repository's license.

## Code of conduct

By participating, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

**中文简要说明：** 小改动直接提 PR；较大改动请先开 Issue 讨论。每个提交请用 `git commit -s` 签署（DCO）。不要提交任何 API Key、Token、密码或个人信息。
