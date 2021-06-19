# fastapi-react-typescript-template

# Requirement

-   Python 3.7 or newer
-   Node.js

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

[ ] Accept file download (sent via backend)

[ ] Accept file upload

[ ] User register

[ ] User login

[ ] Use cookies to store login? https://sanic.readthedocs.io/en/latest/sanic/cookies.html

# Tests

[ ] How to test a webserver?

# Autoformatting

```
npx prettier --write "src/**/*.tsx"
black --line-length 120 .
```

# Run pre commit hooks
`poetry run pre-commit run --all-files`
