# MVP

## Dev Start

You need two things to get started:

### Create venv
```
cd project-root
conda env create -f env.yml
```

### `.env` file
The langchain `mvp` by default looks for an environment variable called "OPENAI_API_KEY", which you can set just paste into your local `.env` file.

Create a `.env` file in the `mvp/` directory, then paste your key like this:
```
OPENAI_API_KEY=<insert your key here>
```


# Examples

To illustrate the final content we want to show users, we made a few examples below that show you the power of contextualization and examples in learning new technologies.

- [Docker](./examples/docker/README.md)
- [Git](./examples/git/README.md)

# mvp/README.md

## Instructions to run the MVP Flask app using Docker

```bash
# Build Docker image
docker build -t my-flask-app .

# Run Docker container
docker run -p 5000:5000 my-flask-app
```

