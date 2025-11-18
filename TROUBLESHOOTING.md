# Troubleshooting Guide for Learners

This document covers common issues you might encounter and how to fix them.

## Docker Permission Denied

### Error Message:
```
ERROR: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock
```

### Solution:

This happens when the dev container isn't fully initialized. Try these steps in order:

#### Option 1: Rebuild Container (Recommended)
1. Open Command Palette (Cmd/Ctrl + Shift + P)
2. Type: "Codespaces: Rebuild Container"
3. Wait for rebuild (1-2 minutes)
4. Try your Docker command again

#### Option 2: Restart Codespace
1. Go to your Codespaces page on GitHub
2. Click the "..." menu next to your codespace
3. Select "Stop codespace"
4. Start it again
5. Try your Docker command again

#### Option 3: Add User to Docker Group (Manual Fix)
If rebuilding doesn't work, run these commands:

```bash
# Add your user to the docker group
sudo usermod -aG docker $USER

# Restart the Docker service
sudo service docker restart

# Activate the new group (or restart your terminal)
newgrp docker

# Test Docker
docker ps
```

#### Option 4: Use sudo (Temporary Workaround)
```bash
# Use sudo for Docker commands (not ideal but works)
sudo docker build -t simple-web .
sudo docker run -d -p 8080:80 simple-web
```

**Note:** If you need sudo, report it - there may be a configuration issue.

## Port Already in Use

### Error Message:
```
Bind for 0.0.0.0:8080 failed: port is already allocated
```

### Solution:

```bash
# Find what's using the port
docker ps

# Stop the container using that port
docker stop <container-id>

# Or use a different port
docker run -d -p 8081:80 simple-web
```

## Container Won't Start

### Error Message:
Container exits immediately or shows "Exited (1)"

### Solution:

```bash
# Check the logs to see what went wrong
docker logs <container-id>

# Or if you don't have the container ID
docker ps -a  # Shows all containers including stopped ones
docker logs <container-id>
```

Common causes:
- Syntax error in Dockerfile
- Missing files (check your COPY commands)
- Application crashes on startup

## Can't Access Forwarded Port

### Problem:
Container is running but you can't access the web page

### Solution:

1. **Check the Ports tab** in VS Code (bottom panel)
2. **Look for your port** (e.g., 8080)
3. **Click the globe icon** to open in browser
4. **Check visibility** - should be "Private" or "Public"

If port isn't showing:
```bash
# Verify container is running
docker ps

# Check the port mapping
docker ps  # Look at the PORTS column

# Make sure you mapped the port correctly
docker run -d -p 8080:80 simple-web
#             ^^^^ ^^
#             host container
```

## Out of Disk Space

### Error Message:
```
no space left on device
```

### Solution:

```bash
# Remove stopped containers
docker container prune -y

# Remove unused images
docker image prune -a -y

# Remove everything unused
docker system prune -a -y

# Check disk usage
docker system df
```

## Image Build Fails

### Common Issues:

#### 1. File Not Found
```
COPY failed: file not found
```

**Solution:** Check your file paths and make sure you're in the right directory:
```bash
# List files
ls -la

# Make sure you're in the right directory
pwd

# Build from the correct location
cd /workspaces/containers/examples/simple-web
docker build -t simple-web .
```

#### 2. Network Timeout
```
failed to fetch ... timeout
```

**Solution:** Retry the build - network hiccups happen:
```bash
docker build -t simple-web . --no-cache
```

#### 3. Invalid Dockerfile Syntax
**Solution:** Check your Dockerfile for typos:
- Each instruction should be on its own line
- Instructions are UPPERCASE (FROM, RUN, COPY, etc.)
- Strings with spaces need quotes

## Docker Compose Issues

### Services Won't Start

```bash
# Check the logs
docker compose logs

# Check specific service logs
docker compose logs web

# Restart everything
docker compose down
docker compose up -d
```

### Can't Connect Between Services

Make sure services are on the same network (defined in docker-compose.yml):
```yaml
networks:
  app-network:
    driver: bridge
```

## Python Example Issues

### ModuleNotFoundError

```bash
# Make sure requirements are installed
cd examples/python-app
docker build -t python-app .  # Rebuilds and installs requirements
docker run -d -p 5000:5000 python-app
```

### Python Version Issues

Check the Dockerfile uses a compatible Python version:
```dockerfile
FROM python:3.11-slim  # ← Make sure this matches your needs
```

## General Tips

### 1. Check Container Status
```bash
# List running containers
docker ps

# List all containers
docker ps -a

# Inspect a container
docker inspect <container-id>
```

### 2. View Logs
```bash
# Follow logs in real-time
docker logs -f <container-id>

# Show last 50 lines
docker logs --tail 50 <container-id>
```

### 3. Enter Running Container
```bash
# Open a shell inside the container
docker exec -it <container-id> bash

# Or if bash isn't available
docker exec -it <container-id> sh
```

### 4. Clean Slate
When things get messy, start fresh:
```bash
# Stop all containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)

# Or remove everything at once
docker system prune -a -f
```

## Codespaces-Specific Issues

### Codespace is Slow
- First startup takes 1-2 minutes (normal)
- Subsequent startups are faster
- Building large images takes time

### Codespace Timeout
- Codespaces stop after 30 minutes of inactivity (default)
- Just restart it from GitHub

### Can't Save Files
- Make sure you're connected to the Codespace
- Check bottom-left corner in VS Code

### Extensions Not Working
- Wait for the Codespace to fully load
- Rebuild container if needed

## Getting Help

If none of these solutions work:

1. **Check the creation logs:**
   - Command Palette → "Codespaces: View Creation Log"

2. **Open an issue:**
   - Go to the repository on GitHub
   - Click "Issues" → "New Issue"
   - Describe your problem and include:
     - The command you ran
     - The full error message
     - What you've already tried

3. **Ask the instructor/maintainer**

## Quick Reference

### Most Common Fixes

```bash
# 1. Rebuild the Codespace
# Command Palette → "Codespaces: Rebuild Container"

# 2. Clean up Docker
docker system prune -a -y

# 3. Restart Docker service
sudo service docker restart

# 4. Check if Docker is running
docker ps

# 5. View container logs
docker logs <container-id>
```

## Prevention Tips

1. **Always stop containers when done:**
   ```bash
   docker stop <container-id>
   ```

2. **Clean up regularly:**
   ```bash
   docker system prune -y
   ```

3. **Use specific port numbers** to avoid conflicts

4. **Check you're in the right directory** before building

5. **Read error messages carefully** - they usually tell you what's wrong

---

**Remember:** Most issues can be fixed by rebuilding the container or cleaning up Docker resources. Don't hesitate to ask for help!
