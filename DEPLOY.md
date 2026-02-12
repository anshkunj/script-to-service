# Deployment Guide

Script to Service

This document explains how to deploy the Script to Service project as a live automation service.

The goal is predictable and repeatable deployment.

---

## Prerequisites

You need the following:

- Python 3.9 or higher
- Git
- A Render account or any similar PaaS
- Basic knowledge of environment variables

---

## Local Setup

### Clone the repository
```
git clone https://github.com/anshkunj/script-to-service.git
cd script-to-service
```

---

### Create a virtual environment
```python -m venv venv```  

Activate it on Linux or macOS:  
```source venv/bin/activate```  

Activate it on Windows:  
```venv\Scripts\activate```

---

### Install dependencies
```pip install -r requirements.txt```

---

### Run the service locally
```uvicorn api.main:app --reload```  

The service will be available at:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/health

---

## Environment Variables

The service uses environment based configuration.

Example values:  
```ENV=production LOG_LEVEL=info SERVICE_TOKEN=your-secret-token```  

>Do not commit secrets to the repository.

---

## Deployment on Render

This project is designed to deploy cleanly on Render.

---

### Create a new web service

- Connect your GitHub repository
- Select the branch to deploy
- Choose Python as the environment

---

### Build command
```pip install -r requirements.txt```

---

### Start command
```uvicorn api.main:app --host 0.0.0.0 --port 10000```  

>Render assigns the port automatically.

---

### Configure environment variables

Add these in the Render dashboard:

- ENV
- LOG_LEVEL
- SERVICE_TOKEN

---

### Deploy

Click Deploy.

After deployment, verify the following:

- The health endpoint returns OK
- The docs page loads
- Example endpoints run successfully

---

## Health Endpoint

The health endpoint is used to verify service availability.

Expected response:  
{ "status": "ok", "service": "script-to-service" }  

>This endpoint should always be lightweight.

---

## Logs and Monitoring

- Logs are written to standard output
- Render captures logs automatically
- Use logs to debug failures and monitor runs

---

## Common Issues

### Service starts but endpoints fail

- Check environment variables
- Check logs for errors
- Verify input validation

---

### Service deploys but is unreachable

- Confirm host binding is 0.0.0.0
- Verify the start command
- Check platform status

---

## Scaling Notes

This project is intentionally simple.

Possible extensions:

- Background workers for heavy tasks
- External schedulers or queues
- Persistent storage for outputs
- Authentication layers

Only scale when required.

---

## Philosophy

Deployment should be boring.

If deployment feels complex, the system is not ready.

Script to Service values clarity over cleverness.

---

## Final Checklist

Before sharing publicly:

- Health endpoint works
- Logs are visible
- Secrets are not committed
- Example workflow runs end to end

If all checks pass, the service is ready.
