# Application Foundation

## Objective

Create the initial Python/FastAPI application and establish a repeatable local development and testing workflow.

The application was later refactored to separate application startup, configuration, and API routing responsibilities as the project begins to grow.

## Environment Setup

A Python virtual environment was created with:

```bash
python -m venv .venv
```

The virtual environment isolates project dependencies from the system Python installation.

PowerShell initially blocked the activation script because script execution was disabled. The execution policy was temporarily changed for the current PowerShell process only, allowing the virtual environment to be activated without persistently changing the system policy.

Project dependencies are recorded in `requirements.txt` so the environment can be recreated without committing the `.venv` directory.

## Application Structure

The application currently uses the following structure:

```text
app/
├── config.py
├── main.py
└── routes/
    └── health.py

tests/
└── test_health.py
```

### `app/main.py`

Creates the FastAPI application and registers application routers.

The goal is to keep `main.py` focused on assembling the application rather than defining every API endpoint directly.

### `app/config.py`

Contains application-wide configuration values.

The initial configuration value defines the API title:

```text
Secure DevSecOps Platform API
```

Separating configuration from application logic provides a foundation for future environment-specific settings such as database configuration, logging levels, and service URLs.

Secrets and credentials will not be hard-coded into this module.

### `app/routes/health.py`

Defines the health-check endpoint using FastAPI's `APIRouter`.

Using routers separates HTTP routing responsibilities from application initialization and allows future API functionality to be organized into logical modules.

## Health Endpoint

The application provides:

```text
GET /health
```

Expected response:

```json
{"status":"healthy"}
```

The current endpoint verifies that the FastAPI application can receive and process a request.

It does not currently verify external dependencies such as PostgreSQL. As the application develops, health checking can be expanded to distinguish between application liveness and dependency readiness.

## Running the Application

The application is served locally with Uvicorn:

```bash
python -m uvicorn app.main:app --reload
```

In `app.main:app`:

- `app` refers to the application package.
- `main` refers to `main.py`.
- The final `app` refers to the FastAPI application object.

The `--reload` option is useful during local development because Uvicorn automatically reloads when Python source files change. It should not normally be used for production deployments.

## Manual Verification

The health endpoint was verified with:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

Expected result:

```text
status
------
healthy
```

The HTTP response was also verified as:

```text
HTTP 200 OK
Content-Type: application/json
```

The TCP listener was inspected and confirmed on:

```text
127.0.0.1:8000
```

Binding to `127.0.0.1` limits access to the local machine during development.

## OpenAPI Verification

FastAPI automatically generates an OpenAPI specification.

The application metadata was inspected through:

```text
/openapi.json
```

The generated specification confirmed:

```text
title = Secure DevSecOps Platform API
version = 0.1.0
```

This verified that the application was successfully consuming the value defined in `config.py`.

## Automated Testing

Pytest and FastAPI's test client are used to validate the health endpoint automatically.

The test verifies:

- HTTP status code is `200`
- Response body is `{"status":"healthy"}`

Tests are executed with:

```bash
python -m pytest -v
```

Current result:

```text
1 passed
```

The same test continued to pass after the health route was moved from `main.py` into its own router module, confirming that the refactor changed the internal structure without changing external behavior.

## Dependency Troubleshooting

The initial test produced a Starlette deprecation warning because the test client was using `httpx`.

Installed dependency versions were investigated with:

```bash
python -m pip show fastapi starlette httpx
```

The deprecated dependency was replaced with `httpx2`, after which the test completed successfully without warnings.

This demonstrated the importance of investigating dependency warnings rather than assuming a passing test means the dependency stack is healthy.

## Architecture Decisions

### Separation of Concerns

The original health endpoint was defined directly in `main.py`.

It was refactored into a dedicated router:

```text
main.py
   │
   │ include_router()
   ▼
health router
   │
   ▼
GET /health
```

This keeps application initialization separate from HTTP endpoint definitions.

As the API grows, additional functionality can be organized into separate routing modules instead of accumulating inside `main.py`.

### Configuration Separation

Application configuration is maintained separately from routing and application startup.

This establishes a foundation for future environment-specific configuration without hard-coding operational values throughout the codebase.

### Regression Testing

The existing health test was run before and after the refactor.

Because the same test passed after restructuring the application, the refactor demonstrated an important engineering principle:

> Internal implementation can change while externally observable behavior remains consistent.

## Security Notes

- `.venv` is excluded from Git.
- Environment files such as `.env` are excluded from Git.
- Secrets and credentials should not be stored directly in application source code.
- The development server currently binds to `127.0.0.1`, limiting network exposure.
- PowerShell execution policy was changed only for the active process rather than persistently weakening script controls.
- Changes are developed on feature/refactor branches instead of directly on `main`.
- Automated tests are run before changes are committed and merged.

## Interview Takeaway

I built the initial API using FastAPI and Uvicorn, created a health endpoint, verified it over HTTP and at the TCP layer, and added automated testing with pytest.

I then refactored the application to separate startup, configuration, and HTTP routing responsibilities. The health endpoint was moved into an `APIRouter` module and registered with the main FastAPI application. I reran the existing test suite after the refactor to verify that the architecture changed without changing the API's behavior.

I also separated application metadata into a configuration module and verified through the generated OpenAPI specification that FastAPI was consuming the configuration correctly.

This structure provides a cleaner foundation for adding database access, additional API routes, security controls, containerization, and CI/CD later in the project.