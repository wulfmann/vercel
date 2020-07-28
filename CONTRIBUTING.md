# Contributing

## Steps

### Create an Issue

[Create an issue](https://github.com/wulfmann/vercel/issues/new/choose) and describe your idea and proposed changes.

### Fork the repo

Fork the repo into your own account and create a new branch.

### Do your thing

Make your changes locally.

For documentation on the development environment for this repo, see the [Development Section](#Development).

### Commit your changes

Commit your changes to your new branch.

### Create a Pull Request

When you are ready, Create a PR for review.

## Development

This project uses [poetry](https://python-poetry.org/) for dependency management and package build/publishing.

You can follow [their instructions](https://python-poetry.org/docs/#installation) on installation.

### Install Dependencies

```bash
poetry install --dev
```

### Run Tests

```bash
poetry run pytest
```

With Coverage

```bash
poetry run pytest --cov vercel
```

With Parallelization

```bash
poetry run pytest --cov vercel -n 2
```

### Run Formatter

```bash
poetry run black .
```

### Build / Publish

Make sure you bump the version of the package according to [semver](https://semver.org/). Then run:

```bash
poetry publish --build
```

This will prompt you for the username and password for the package.
