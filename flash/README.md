# flash

## Examples

To illustrate the final content we want to show users, we made a few examples below that show you the power of contextualization and examples in learning new technologies.

- [Docker](./text-examples/docker/README.md)
- [Git](./text-examples/git/README.md)

## Dev Setup

You need two things to get started:

### Create venv

```bash
# In the project root directory
conda env create -f env.yml
```

### `.env` file

Currently, this project requires two API keys. One from [OpenAI](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key), and one from [Tavily AI](https://app.tavily.com/home). Follow these two links and get both of them, and then create a `.env` file in the `<project_root>/flash` directory, and paste your key like this:

```bash
OPENAI_API_KEY=<insert your key here>
TAVILY_API_KEY=<insert your key here>
```

These `env` variables are then loaded using the [`dotenv`](https://pypi.org/project/python-dotenv/) package for the code to find.

## Dev Workflow

### Start app

Our app is based on `taipy`, a python-markdown framework that builds data webapps.

```bash
conda activate flash-env
cd flash/
python main.py
```

### Adding new packages

If you need to add a new package dependency, as part of your push you need to update the `env.yml` file. To do this, run this command **with your `flash-env` activated**:

```bash
conda env export | grep -v "^prefix: " > env.yml
```
