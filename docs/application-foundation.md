# Application Foundation

## Objective

Create the initial Python/FastAPI application and establish a repeatable local development and testing workflow.

## Environment Setup

A Python virtual environment was created with:

```bash
python -m venv .venv
```

The virtual environment isolates project dependencies from the system Python installation.

PowerShell initially blocked the activation script because script execution was disabled. The execution policy was temporarily changed for the current PowerShell process only, allowing the virtual environment to be activated without changing the persistent system policy.

## Application

The initial FastAPI application contains a health endpoint:

```text
GET /health
```

Expected response:

```json
{"status":"healthy"}
```

The application is served locally with Uvicorn.

## Verification

The API was manually verified with:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

The TCP listener was also verified on:

```text
127.0.0.1:8000
```

## Automated Testing

Pytest and FastAPI's test client were added to validate the health endpoint automatically.

The test verifies:

- HTTP status code is `200`
- Response body is `{"status":"healthy"}`

Test command:

```bash
python -m pytest -v
```

Result:

```text
1 passed
```

## Dependency Troubleshooting

The initial test produced a Starlette deprecation warning because the test client was using `httpx`.

The installed dependency versions were inspected with:

```bash
python -m pip show fastapi starlette httpx
```

The deprecated dependency was replaced with `httpx2`, and the test was rerun successfully without warnings.

## Security Notes

- `.venv` is excluded from Git.
- Environment files such as `.env` are excluded from Git.
- The application currently listens only on `127.0.0.1`, limiting access to the local machine.
- PowerShell execution policy was changed only for the active process rather than persistently weakening script controls.

## Interview Takeaway

The application currently uses FastAPI behind the Uvicorn ASGI server. I created a health endpoint, verified it manually over HTTP, confirmed the TCP listener, and added an automated pytest test so the endpoint can later be validated in CI/CD.