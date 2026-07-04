# DevOps CI/CD Pipeline Project
![Architecture Diagram](architecture.png)
## Overview
A complete end-to-end DevOps project featuring a Python Flask To-Do API, 
fully automated CI/CD pipeline, containerization, and Kubernetes deployment.

## Tech Stack
- **App:** Python Flask
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Container Registry:** Docker Hub
- **Orchestration:** Kubernetes

## Pipeline Flow
Code Push → GitHub Actions → Docker Image Build → Docker Hub Push → Kubernetes Deploy

## Features
- REST API with GET and POST endpoints
- Automated Docker image build on every code push
- Automatic deployment pipeline using GitHub Actions
- Kubernetes deployment with NodePort service

## How to Run Locally
```bash
cd app
pip install -r requirements.txt
python3 app.py
```

## API Endpoints
- `GET /` — Health check
- `GET /tasks` — Get all tasks
- `POST /tasks` — Add a new task

## Project Structure
```
my-first-devops-project/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── .github/
    └── workflows/
        └── main.yml
```

