# Production ML

A production-oriented machine learning application environment built with Python, FastAPI, databases, experiment tracking, data versioning, Docker, and GitHub Actions.

## Project Stack

* **Python:** 3.12
* **Package management:** uv
* **API:** FastAPI + Uvicorn
* **Databases:**

  * PostgreSQL
  * MongoDB
  * Redis
  * InfluxDB
* **Experiment tracking:** MLflow
* **Data versioning:** DVC
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Infrastructure as Code:** Terraform
* **Cloud CLI:** AWS CLI

## Project Structure

```text
Production-ML/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dvc/
├── src/
│   └── production_ml/
├── Dockerfile
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

## Local Development

### 1. Activate the environment

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Run the API

```bash
uv run uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Docker

Build the image:

```bash
docker build -t production-ml:local .
```

Run the container:

```bash
docker run -d --name production-ml-api -p 8000:8000 production-ml:local
```

Test the API:

```bash
curl http://127.0.0.1:8000/
```

Stop the container:

```bash
docker stop production-ml-api
```

## Databases

The local development database stack is managed separately through Docker Compose.

Services:

```text
PostgreSQL   → 5432
MongoDB      → 27017
Redis        → 6379
InfluxDB     → 8086
```

## MLflow

MLflow is used for local experiment tracking.

Start the MLflow server:

```bash
mlflow server --host 127.0.0.1 --port 5000
```

MLflow UI:

```text
http://127.0.0.1:5000
```

## DVC

DVC is used for data versioning.

Initialize DVC if required:

```bash
dvc init
```

## CI/CD

GitHub Actions runs automatically for pushes to `main` and pull requests targeting `main`.

The CI pipeline currently:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs `uv`.
4. Installs locked project dependencies.
5. Verifies the FastAPI application imports successfully.
6. Builds the Docker image.

## Infrastructure

Terraform and AWS CLI are installed locally for infrastructure and cloud-development workflows.

AWS credentials are intentionally not stored in this repository.

## Development Principles

* Keep application dependencies inside the project environment.
* Do not use `sudo pip` or system Python for project packages.
* Keep secrets and credentials outside Git.
* Use Docker for reproducible services.
* Use MLflow for experiment tracking.
* Use DVC for data versioning.
* Use GitHub Actions for automated validation.
