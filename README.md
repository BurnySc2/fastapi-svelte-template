# fastapi-react-typescript-template

# Requirement

-   Python 3.7 or newer
-   Node.js 12+

# Installation

You can clone a fresh template with
`npx degit sveltejs/template my-svelte-project`

Install node and python 3.7+

```
pip install poetry --user
poetry install
npm install
```

# Development

```
npm run dev
poetry run uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
Then to go http://localhost:8080 to preview the page

# Deploy

Create the front end and host it somewhere (e.g. github pages)

```
npm run build
```

Launch the backend on a server

```
pip install poetry --user
poetry install
poetry run uvicorn main:app --host 0.0.0.0 --port 5000
```

# Functionality

## Requests

[x] Communicate between front and backend

[x] Accept file download (sent via backend)

[ ] Accept file upload

[ ] User register

[ ] User login

[ ] Use cookies to store login? https://sanic.readthedocs.io/en/latest/sanic/cookies.html

# Tests
Run python backend tests via
```
poetry run pytest test_backend --benchmark-skip
```
and Javascript unit tests via 
```
npm run test
```

[x] How to test a webserver?
Run frontend tests via 
```
poetry run pytest test_frontend --benchmark-skip --headless
```

You can benchmark tests with 
```
poetry run pytest test_backend --benchmark-only
poetry run pytest test_frontend --benchmark-only
```

# Install and run all pre-commit hook scripts
```py
poetry run pre-commit install
poetry run pre-commit run --all-files
```

This runs pylint, mypy, pytest tests, apply autoformatter yapf

# Upgrade packages to latest major version
```
npx npm-check-updates -u
```
Or run 
```
npm run update
```
to update versions, reinstall node_modules from scratch

# Autoformatting

```
npx prettier --write "src/**/*.{json,ts,svelte}"
yapf ./**/*.py -i
```
Or just 
```
npm run format
```
