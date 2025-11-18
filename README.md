# Docker Containers Learning Repository

Welcome! This repository is designed to help you learn Docker and build containers in a consistent environment using **GitHub Codespaces**, regardless of whether you're on Windows, macOS, or Linux.

## 🚀 Quick Start

### Using GitHub Codespaces (Recommended)

1. **Open in Codespaces**
   - Click the green "Code" button at the top of this repository
   - Select "Codespaces" tab
   - Click "Create codespace on main"
   - Wait for the environment to set up (1-2 minutes)

2. **Verify Docker Installation**
   ```bash
   docker --version
   docker compose version
   ```

3. **You're Ready!** Docker and Docker Compose are pre-installed and configured.

### Alternative: Local Development

If you prefer to work locally, you'll need:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/macOS)
- Docker Engine (Linux)
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## 📚 Examples Included

This repository includes several example projects to get you started:

### 1. Simple Web Server (`examples/simple-web/`)
A basic nginx web server serving a custom HTML page.

```bash
cd examples/simple-web
docker build -t simple-web .
docker run -d -p 8080:80 simple-web
```

Then open the forwarded port to see your web page!

### 2. Python Flask Application (`examples/python-app/`)
A Python web application using Flask.

```bash
cd examples/python-app
docker build -t python-app .
docker run -d -p 5000:5000 python-app
```

### 3. Multi-Container App with Docker Compose (`examples/docker-compose-example/`)
A multi-service application with nginx and Redis.

```bash
cd examples/docker-compose-example
docker compose up -d
```

To stop:
```bash
docker compose down
```

## 🛠️ Common Docker Commands

### Building Images
```bash
# Build an image from a Dockerfile
docker build -t my-image-name .

# Build with a specific Dockerfile
docker build -t my-image -f Dockerfile.dev .
```

### Running Containers
```bash
# Run a container
docker run my-image-name

# Run in detached mode (background)
docker run -d my-image-name

# Run with port mapping
docker run -p 8080:80 my-image-name

# Run with volume mount
docker run -v $(pwd):/app my-image-name

# Run with environment variables
docker run -e MY_VAR=value my-image-name
```

### Managing Containers
```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop container-id

# Remove a container
docker rm container-id

# View container logs
docker logs container-id

# Execute command in running container
docker exec -it container-id bash
```

### Managing Images
```bash
# List images
docker images

# Remove an image
docker rmi image-id

# Pull an image from Docker Hub
docker pull nginx:latest

# Tag an image
docker tag my-image:latest my-image:v1.0
```

### Docker Compose Commands
```bash
# Start services
docker compose up

# Start in background
docker compose up -d

# Stop services
docker compose down

# View logs
docker compose logs

# Rebuild services
docker compose up --build
```

### Cleanup Commands
```bash
# Remove all stopped containers
docker container prune

# Remove all unused images
docker image prune

# Remove all unused volumes
docker volume prune

# Remove everything unused
docker system prune -a
```

## 📝 Creating Your Own Dockerfile

Here's a template to get you started:

```dockerfile
# Choose a base image
FROM ubuntu:latest

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN apt-get update && apt-get install -y \
    package-name \
    && rm -rf /var/lib/apt/lists/*

# Expose port (documentation only)
EXPOSE 8080

# Set environment variables
ENV MY_VAR=value

# Run command when container starts
CMD ["executable", "param1", "param2"]
```

## 🎯 Learning Path

1. **Start with Simple Web** - Learn basic Docker commands and image building
2. **Try Python App** - Understand multi-step builds and dependencies
3. **Explore Docker Compose** - Learn to orchestrate multiple containers
4. **Create Your Own** - Build something custom!

## 🔧 Troubleshooting

### Port Already in Use
If you get a "port already in use" error:
```bash
# Find what's using the port
docker ps

# Stop the container using that port
docker stop container-id
```

### Container Won't Start
Check the logs:
```bash
docker logs container-id
```

### Out of Space
Clean up unused resources:
```bash
docker system prune -a
```

### Can't Connect to Docker Daemon
In Codespaces, Docker should work automatically. If you have issues:
```bash
# Check Docker is running
docker ps

# Restart the codespace if needed
```

## 📖 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/) - Find pre-built images
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

## 🤝 Contributing

Feel free to add your own examples! Create a new folder under `examples/` with:
- A `Dockerfile`
- A `README.md` explaining what it does
- Any necessary application files

## 💡 Tips for Success

1. **Always use `.dockerignore`** - Similar to `.gitignore`, exclude unnecessary files
2. **Keep images small** - Use alpine or slim base images when possible
3. **One process per container** - Follow the single responsibility principle
4. **Use multi-stage builds** - For smaller production images
5. **Don't run as root** - Create a user in your Dockerfile for security
6. **Tag your images** - Use meaningful version tags, not just `latest`

## 🐳 Happy Containerizing!

Remember: The beauty of Codespaces is that everyone gets the exact same environment. No more "it works on my machine" problems!

---

**Questions?** Open an issue or reach out to the repository maintainer.