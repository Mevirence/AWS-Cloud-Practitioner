# EC2 Simple Web Server

This project demonstrates how to launch and configure a simple Apache web server using AWS EC2 (Amazon Elastic Compute Cloud).

## 📌 Project Overview

- Launch a free-tier eligible Amazon EC2 instance
- SSH into the instance using Git Bash
- Install Apache web server
- Serve a basic HTML page
- Open to the internet via port 80

## 🧰 Tools & Services

- AWS EC2
- Amazon Linux 2
- Git Bash (on Windows)
- Apache HTTP Server

## 🚀 Steps

1. **Launch EC2 Instance**
   - Amazon Linux 2
   - t2.micro (Free Tier)
   - Allow SSH (22) and HTTP (80) in Security Group

2. **Connect via SSH**
   ```bash
   chmod 400 ec2-project.pem
   ssh -i "ec2-project.pem" ec2-user@18.140.1.154

3. **Install Apache**
   ```bash
   sudo yum update -y
   sudo yum install httpd -y
   sudo systemctl start httpd
   sudo systemctl enable httpd

4. **Deploy Web Page**
   ```bash
   echo "<h1>Hello from AWS EC2!</h1>" | sudo tee /var/www/html/index.html

5. **Access in Browser**
   http://18.140.1.154

# 📝 Notes
- This setup uses the Free Tier.
- No custom domain or SSL (HTTPS) was configured.
- For production environments, consider using NGINX, HTTPS (SSL/TLS), and security best practices.

# 📸 Screenshot
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/23bd9f64-0d28-470a-9ee6-796d37c43e4a" />


