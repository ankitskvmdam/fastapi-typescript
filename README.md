# fastapi-typescript

This repository contains a FastAPI server with TypeScript client.

## Setup FastAPI server

### Create and activate virtual environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
. .venv/bin/activate
```
### Install dependencies

```bash
# Run inside fastapi-typescript/server
pip install -r requirements.txt
```

### Run FastAPI server

```bash
# Run inside fastapi-typescript/server
fastapi dev main.py
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

### Run tests

```bash
# Run inside fastapi-typescript/server
pytest
```
## Setup TypeScript client

### Install the dependencies

```bash
# Run inside fastapi-typescript/client
npm install
```

### Run TypeScript client

```bash
# Run inside fastapi-typescript/client
npm dev
```

This will start the TypeScript client on `http://127.0.0.1:5173`.


# License
This repository is licensed under the MIT License.
