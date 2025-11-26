# Docker Quick Start Guide

This guide will help you run the entire Corporate Chatbot application with a single command.

## Prerequisites

- Docker Desktop installed ([Download here](https://www.docker.com/products/docker-desktop))
- At least 8GB of RAM available for Docker
- 10GB of free disk space (for Ollama model)

## Quick Start

### 1. Start Everything

Run this single command to start the entire application:

```bash
docker-compose up -d
```

This will:
- Build the application container
- Start Ollama LLM server
- Download the llama3.1 model (this may take 5-10 minutes first time)
- Initialize the database with default users
- Initialize the knowledge base with documents
- Start the web application

### 2. Check Status

Monitor the setup progress:

```bash
docker-compose logs -f
```

Wait until you see:
- `✅ Model ready!` from ollama-setup
- `✅ Application ready!` from the app

Press `Ctrl+C` to stop following logs.

### 3. Access the Application

Open your browser and go to:
```
http://localhost:8000
```

### 4. Login

Use one of these default accounts:

**Admin User:**
- Username: `admin`
- Password: `AdminPass123!`
- Role: Executive
- Department: IT

**HR User:**
- Username: `alice`
- Password: `AlicePass123!`
- Role: Staff
- Department: HR

**Security User:**
- Username: `bob`
- Password: `BobPass123!`
- Role: SecurityAnalyst
- Department: Security

## Management Commands

### Stop the Application
```bash
docker-compose down
```

### Stop and Remove All Data
```bash
docker-compose down -v
```

### View Logs
```bash
# All services
docker-compose logs -f

# Just the app
docker-compose logs -f app

# Just Ollama
docker-compose logs -f ollama
```

### Restart Services
```bash
docker-compose restart
```

### Rebuild After Code Changes
```bash
docker-compose up -d --build
```

## Troubleshooting

### Port Already in Use
If port 8000 or 11434 is already in use, edit `docker-compose.yml` and change:
```yaml
ports:
  - "8001:8000"  # Change 8000 to 8001 or any available port
```

### Ollama Model Download Fails
If the model download fails, manually pull it:
```bash
docker-compose exec ollama ollama pull llama3.1
```

### Application Won't Start
Check logs for errors:
```bash
docker-compose logs app
```

Common issues:
- Ollama not ready: Wait a bit longer, model download takes time
- Database errors: Remove volume and restart: `docker-compose down -v && docker-compose up -d`

### Reset Everything
To start fresh:
```bash
docker-compose down -v
docker-compose up -d --build
```

## Configuration

### Environment Variables

Edit `docker-compose.yml` to customize:

- `MODEL_NAME`: Change LLM model (default: llama3.1)
- `SECRET_KEY`: Change for production deployment
- `RATE_LIMIT_CHAT`: Adjust rate limiting
- `LOG_LEVEL`: Change to DEBUG for more verbose logs

### Using Different Models

To use a different Ollama model:

1. Edit `docker-compose.yml` and change `MODEL_NAME` and the model in `ollama-setup`
2. Restart: `docker-compose up -d --build`

Available models: llama3.1, llama2, mistral, codellama, etc.
See: https://ollama.ai/library

## Production Deployment

For production:

1. Change `SECRET_KEY` to a secure random value
2. Use a proper database (PostgreSQL) instead of SQLite
3. Set up proper SSL/TLS certificates
4. Configure firewall rules
5. Set up monitoring and logging
6. Use Docker secrets for sensitive data

## System Requirements

- **CPU**: 4+ cores recommended
- **RAM**: 8GB minimum, 16GB recommended
- **Disk**: 10GB for model + application
- **Network**: Internet connection for initial model download

## Support

For issues or questions:
1. Check logs: `docker-compose logs -f`
2. Verify all containers are running: `docker-compose ps`
3. Ensure ports are not blocked by firewall
