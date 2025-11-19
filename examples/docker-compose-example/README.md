# 🎲 Boredom Buster - Docker Compose Example

An interactive web application that demonstrates the power of Docker Compose by coordinating a Flask web server with a Redis database.

## 🎯 What This Demonstrates

This example shows why Docker Compose is essential for multi-container applications:

- **Multi-container orchestration**: Flask web app + Redis database working together
- **Service discovery**: Containers communicate using service names (no hard-coded IPs!)
- **Dependency management**: Web service waits for Redis to be ready
- **Single command deployment**: Start everything with `docker compose up`
- **Isolated networking**: Containers communicate on a private network
- **Live updates**: Code changes reflect immediately with volume mounts

## 🤔 Why Docker Compose vs Regular Docker?

### Without Compose (The Hard Way):
```bash
# 1. Create a custom network
docker network create boredom-net

# 2. Start Redis container
docker run -d --name redis --network boredom-net redis:7-alpine

# 3. Build the web image
docker build -t boredom-web ./web

# 4. Run the web container with proper networking
docker run -d -p 5000:5000 --name web --network boredom-net \
  -v $(pwd)/web:/app boredom-web

# 5. To stop everything:
docker stop web redis
docker rm web redis
docker network rm boredom-net
```

### With Compose (The Easy Way):
```bash
# Start everything
docker compose up

# Stop everything
docker compose down
```

## 📁 Project Structure

```
docker-compose-example/
├── docker-compose.yml          # Orchestration configuration
├── README.md                   # This file
└── web/
    ├── Dockerfile              # Web container image definition
    ├── app.py                  # Flask application
    ├── requirements.txt        # Python dependencies
    ├── templates/
    │   └── index.html          # Frontend HTML
    └── static/
        └── style.css           # Styles
```

## 🚀 Usage

### Start the Application
```bash
docker compose up
```

Visit http://localhost:5000 in your browser.

### Start in Detached Mode (Background)
```bash
docker compose up -d
```

### View Logs
```bash
docker compose logs -f
```

### Stop the Application
```bash
docker compose down
```

### Rebuild After Code Changes
```bash
docker compose up --build
```

## 🎮 How to Use the App

1. **Get Suggestion**: Click the blue button to get a random activity suggestion
2. **Mark Complete**: Complete the activity and mark it done
3. **View Statistics**: See how many activities you've completed (stored in Redis!)
4. **Reset Stats**: Clear all statistics and start fresh
5. **Test Persistence**: 
   - Interact with the app
   - Run `docker compose down`
   - Run `docker compose up`
   - Notice the stats are gone (no persistent volume)

## 🔍 Key Docker Compose Features Shown

### Service Dependencies
```yaml
depends_on:
  - redis
```
The web service waits for Redis to start first.

### Service Networking
```yaml
redis_client = redis.Redis(host='redis', port=6379)
```
Flask connects to Redis using the service name `redis` - Docker Compose handles DNS!

### Port Mapping
```yaml
ports:
  - "5000:5000"  # Host:Container
```
Access the app on your host machine at localhost:5000.

### Volume Mounts (Development)
```yaml
volumes:
  - ./web:/app
```
Code changes on your host are immediately reflected in the container.

## 🧪 Experiments to Try

1. **Test Service Communication**:
   ```bash
   docker compose exec web ping redis
   ```
   The web container can reach Redis by name!

2. **View Redis Data**:
   ```bash
   docker compose exec redis redis-cli
   > KEYS *
   > GET total_suggestions
   ```

3. **Scale the App** (requires changes):
   ```bash
   docker compose up --scale web=3
   ```
   Note: Won't work without a load balancer, but shows the concept!

4. **Add Data Persistence**: Modify `docker-compose.yml`:
   ```yaml
   redis:
     image: redis:7-alpine
     volumes:
       - redis-data:/data
   
   volumes:
     redis-data:
   ```

5. **Monitor Resources**:
   ```bash
   docker stats
   ```

## 🛠️ Customization Ideas

- Add more activities to the list in `web/app.py`
- Add different activity categories
- Implement user profiles with sessions
- Add a progress bar for each activity
- Create an API endpoint to add custom activities
- Add environment variables for configuration
- Implement health checks in docker-compose.yml

## 📚 Learning Resources

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Docker Compose File Reference](https://docs.docker.com/compose/compose-file/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Redis Python Client](https://redis-py.readthedocs.io/)

## 🐛 Troubleshooting

**Port already in use?**
```bash
# Change the port in docker-compose.yml:
ports:
  - "5001:5000"  # Use port 5001 instead
```

**Can't connect to Redis?**
```bash
# Check if both containers are running:
docker compose ps

# Check logs:
docker compose logs redis
docker compose logs web
```

**Need to rebuild?**
```bash
docker compose down
docker compose build --no-cache
docker compose up
```

## 🎓 What You've Learned

After working through this example, you understand:

✅ How Docker Compose simplifies multi-container applications  
✅ How containers communicate using service names  
✅ How to manage dependencies between services  
✅ How to use volumes for development  
✅ How to expose ports for external access  
✅ How to view logs and debug containerized apps  
✅ The difference between stateless (web) and stateful (redis) services  

---

**Next Steps**: Try modifying the code, add new features, or build your own multi-container application!
