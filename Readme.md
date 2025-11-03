# Weather Monitor - Jenkins Webhook Demo

Simple Flask application demonstrating Jenkins auto-build via GitHub webhook.

## Features
- Python Flask web app
- Dockerized application
- Jenkins CI/CD integration
- GitHub webhook auto-trigger

## Build & Run
docker build -t weather-monitor .
docker run -p 5000:5000 weather-monitor

## Webhook Auto-Build Test
Jenkins build triggered automatically via GitHub webhook! ✅