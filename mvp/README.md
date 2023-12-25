# MVP

## Examples

To illustrate the final content we want to show users, we made a few examples below that show you the power of contextualization and examples in learning new technologies.

- [Docker](./text-examples/docker/README.md)
- [Git](./text-examples/git/README.md)

## Dev Setup

You need two things to get started:

### Create venv

```bash
# While in mvp/src directory
conda env create -f env.yml
```

### `.env` file

The langchain `mvp` by default looks for an environment variable called "OPENAI_API_KEY", which you can set just paste into your local `.env` file.

Create a `.env` file in the `<project_root>/mvp/src` directory, then paste your key like this:

```bash
OPENAI_API_KEY=<insert your key here>
```

## Dev Workflow

### Start app

Our app is based on `taipy`, a python-markdown framework that builds data webapps.

```bash
conda activate flash-env
cd src/
python main.py
```

### Adding new packages

If you need to add a new package dependency, as part of your push you need to update the `env.yml` file. To do this, run this command **with your `flash-env` activated**:

```bash
conda env export | grep -v "^prefix: " > env.yml
```
