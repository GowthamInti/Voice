
## Our notes

the app is designed to run and only one model at instantiation which is xtts_v2 this can be changed in the future to preload multiple models though.

To run different models, run `python dev-run.py <MODEL INFO>`. the availble options is text2speech. Checkout the file for more info, and you can also run `--envkey=envvalue` to change environment variables
# Poetry managed Python FastAPI application with Docker multi-stage builds

### This repo serves as a minimal reference on setting up docker multi-stage builds with poetry


### Requirements

- [Docker >= 17.05](https://www.python.org/downloads/release/python-381/)
- [Python >= 3.7](https://www.python.org/downloads/release/python-381/)
- [Poetry](https://github.com/python-poetry/poetry)


---
**NOTE** - Run all commands from the project root


## Local development

---
## Poetry


Create the virtual environment and install dependencies with:

        poetry install

See the [poetry docs](https://python-poetry.org/docs/) for information on how to add/update dependencies.

Run commands inside the virtual environment with:

        poetry run <your_command>

Spawn a shell inside the virtual environment with

        poetry shell

Start a development server locally

        poetry run uvicorn app.main:app --reload --host localhost --port 8000

API will be available at [localhost:8000/](http://localhost:8000/)

Swagger docs at [localhost:8000/docs](http://localhost:8000/docs)

To run testing/linting locally you would execute lint/test in the [scripts directory](/scripts).


---

## Docker


Build images with:
        
        docker build --tag poetry-project --file docker/Dockerfile . 



