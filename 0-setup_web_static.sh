#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Html document and adding content
sudo echo "<html>
  <head>
  </head>
  <body>
    <h1>Doing 'devops thing'</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Set ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo nginx -t
# Restart Nginx
sudo service nginx restart
