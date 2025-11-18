# Example: Simple Web Server
FROM nginx:alpine

# Copy a custom index page
COPY index.html /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
