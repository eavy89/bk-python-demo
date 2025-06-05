# 🐍 FastAPI Backend Demo

A modern, production-ready backend demo built with **FastAPI**, **JWT authentication**, and **SQLite**.  
This project includes a secure login system, protected endpoints, and is fully containerized with **Docker Compose**. Ideal for portfolio or interview showcase.

---

## 📦 Features

- 🔐 JWT-based authentication with login & register
- 👤 Protected `/profile` endpoint
- 🛒 Purchase API: (`/purchases` [GET/POST]) create and retrieve item purchases
- 🗃️ SQLite for simple local storage
- 📄 Swagger/OpenAPI docs auto-generated (`ip:8000/docs`)
- 🐳 Dockerized for easy local deployment
- ☁️ Ready to scale with Kubernetes & AWS

---

### System Requirements
- Python 3.8+ (and: python3-pip, python3-distutils-extra)
- Docker
- Docker Compose
- 

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/your-username/backend-python-demo.git
cd backend-python-demo
```

### 2. Build and run the container
```bash
    docker-container up -d --build  # with sudo if you do not have permissions'
```

### 3. Access to API Docs
Go to: http://localhost:8000/docs