# Contributing to the Docker Containers Repository

Thank you for your interest in contributing! This repository is meant to be a learning resource for everyone.

## How to Contribute

### Adding a New Example

1. Create a new directory under `examples/` with a descriptive name
2. Include the following files:
   - `Dockerfile` - Your container definition
   - `README.md` - Explanation of what it does and how to use it
   - Any application files needed
   - (Optional) `docker-compose.yml` if using multiple services

3. Test your example in Codespaces to ensure it works

### Example Structure

```
examples/
  your-example-name/
    ├── Dockerfile
    ├── README.md
    ├── app files...
    └── docker-compose.yml (optional)
```

### README Template for Examples

```markdown
# Example Name

Brief description of what this example demonstrates.

## What You'll Learn

- Concept 1
- Concept 2
- Concept 3

## How to Build

\`\`\`bash
docker build -t example-name .
\`\`\`

## How to Run

\`\`\`bash
docker run -p 8080:80 example-name
\`\`\`

## What's Inside

Explain the Dockerfile and any interesting configuration.

## Next Steps

Suggestions for how to modify or extend this example.
```

### Guidelines

- Keep examples simple and focused on one concept
- Include comments in Dockerfiles explaining each step
- Test in Codespaces before submitting
- Use best practices (small images, security, etc.)
- Document any prerequisites or dependencies

### Submitting Your Contribution

1. Fork the repository
2. Create a new branch for your example
3. Add your example following the structure above
4. Test thoroughly in Codespaces
5. Submit a pull request with:
   - Clear description of what the example demonstrates
   - Any special instructions for testing
   - Screenshots if applicable

## Ideas for Examples

- Different programming languages (Ruby, Rust, C#, etc.)
- Databases (PostgreSQL, MongoDB, MySQL)
- Development tools (Redis, Elasticsearch, RabbitMQ)
- Full-stack applications
- Microservices architecture
- CI/CD pipelines
- Monitoring and logging

## Questions?

Open an issue if you have questions about contributing!

Thank you for helping others learn Docker! 🐳
