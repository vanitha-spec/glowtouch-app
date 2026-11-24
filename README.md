# ✨ GlowTouch – AI-Powered Beauty Assistant

<p align="center">
  <strong>An intelligent AI-powered beauty assistant built with Python, Google Gemini, FastAPI, Streamlit, Docker, and AWS.</strong>
</p>

## 🌐 Live Application

**Try GlowTouch here:**

🔗 http://18.117.237.151:8501/

**Backend API Documentation (Swagger UI):**

🔗 http://18.117.237.151:8000/docs

---

## 📌 1. Project Overview

GlowTouch is an AI-powered beauty assistant designed to provide users with an interactive and intelligent beauty-related assistance experience.

The application uses Google's Gemini AI model to process user queries and generate helpful responses. It combines a Streamlit frontend with a FastAPI backend to provide a user-friendly interface and backend API services.

The project is containerized using Docker and deployed on an AWS EC2 virtual machine. AWS Elastic Container Registry (ECR) is used to store and manage the Docker image.

The application runs both backend and frontend services inside a Docker container using Supervisor.

## 🎯 2. Project Objectives

- Build an interactive AI-powered beauty assistant.
- Integrate Google Gemini for AI-based responses.
- Develop backend services using FastAPI.
- Create a user-friendly interface using Streamlit.
- Organize application logic into reusable Python modules.
- Containerize the application using Docker.
- Deploy the application on AWS EC2.
- Store and manage Docker images using AWS ECR.

## 💡 3. Problem Statement

Users often need an accessible and interactive way to obtain beauty-related information and assistance.

Traditional static information sources may not provide an interactive question-and-answer experience.

**Proposed Solution:**

GlowTouch provides an AI-powered conversational interface where users can interact with the application and receive responses generated using Google's Gemini model.

## ⭐ 4. Key Features

- AI-powered conversational assistance using Google Gemini.
- Interactive Streamlit user interface.
- FastAPI backend for application services.
- Modular Python application structure.
- API documentation through Swagger UI.
- Docker-based application packaging.
- Cloud deployment using AWS EC2.
- Docker image management using AWS ECR.

## 🛠️ 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Main programming language |
| Google Gemini API | AI response generation |
| FastAPI | Backend API development |
| Streamlit | Frontend user interface |
| Docker | Application containerization |
| Supervisor | Running multiple services |
| AWS EC2 | Cloud application hosting |
| AWS ECR | Docker image storage |
| Linux | Cloud server environment |
| Git & GitHub | Version control |

## 🏗️ 6. System Architecture

The application follows a frontend-backend architecture.

```text
                  USER
                    |
                    v
          STREAMLIT FRONTEND
             Port 8501
                    |
                    v
             FASTAPI BACKEND
               Port 8000
                    |
                    v
           APPLICATION LOGIC
             agent.py
             tools.py
                    |
                    v
             GOOGLE GEMINI
                    |
                    v
             AI RESPONSE
                    |
                    v
          STREAMLIT INTERFACE
                    |
                    v
                   USER
```

### Cloud Deployment Architecture

```text
        DEVELOPER (LOCAL MACHINE)
                    |
                    v
              DOCKER BUILD
                    |
                    v
              AWS ECR
          Docker Image Storage
                    |
                    v
               AWS EC2
                    |
                    v
             DOCKER CONTAINER
                    |
             SUPERVISOR
              /       \
             /         \
        FASTAPI      STREAMLIT
        :8000          :8501
             \         /
              \       /
             GLOWTOUCH
             APPLICATION
```

## 📂 7. Project Folder Structure

```text
glowtouch/
│
├── data/
│
├── agent.py
├── app.py
├── frontend.py
├── main.py
├── tools.py
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env
└── README.md
```

### File Description

| File / Folder | Description |
|---|---|
| `data/` | Application data files |
| `agent.py` | AI agent configuration and Gemini integration |
| `app.py` | Application entry-point or supporting application logic |
| `frontend.py` | Streamlit frontend |
| `main.py` | FastAPI backend application |
| `tools.py` | Supporting application tools and functions |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Docker image build configuration |
| `.dockerignore` | Excludes unnecessary and sensitive files from Docker builds |
| `.env` | Stores API keys and configuration |
| `README.md` | Project documentation |

## ⚙️ 8. Local Installation and Execution

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd glowtouch
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure environment variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never upload your actual API key to GitHub.

### Step 5: Run the FastAPI backend

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

API documentation:

```text
http://localhost:8000/docs
```

### Step 6: Run the Streamlit frontend

Open another terminal:

```bash
streamlit run frontend.py
```

Local frontend:

```text
http://localhost:8501
```

## 🐳 9. Docker Implementation

The application is packaged into a Docker image so that it can run consistently across different environments.

### Build Docker image

```bash
docker build -t glowtouch-app:latest .
```

### Run Docker container locally

```bash
docker run -d \
  --name glowtouch-app \
  --env-file .env \
  -p 8501:8501 \
  -p 8000:8000 \
  glowtouch-app:latest
```

Supervisor manages both application processes inside the container:

- FastAPI backend on port 8000.
- Streamlit frontend on port 8501.

## ☁️ 10. AWS Cloud Deployment

The application was deployed using AWS cloud infrastructure.

### Deployment Workflow

**Step 1 – Docker Image Creation**

The application source code and dependencies were packaged into a Docker image.

**Step 2 – AWS ECR Repository**

An ECR repository named `glowtouch-app` was created in the `us-east-2` region.

**Step 3 – Push Docker Image**

The Docker image was tagged and uploaded to AWS ECR.

**Step 4 – EC2 Instance**

An AWS EC2 Linux instance was used as the cloud hosting environment.

**Step 5 – Pull Docker Image**

The image was downloaded from ECR to the EC2 instance.

**Step 6 – Environment Configuration**

The Gemini API key was configured on the EC2 instance through a separate environment file.

**Step 7 – Application Execution**

The Docker container was started with port mappings for both services.

**Step 8 – Application Testing**

The frontend and backend were tested using their respective endpoints.

### Docker Image

```text
471888984416.dkr.ecr.us-east-2.amazonaws.com/glowtouch-app:latest
```

### Application Ports

| Service | Port |
|---|---:|
| Streamlit Frontend | 8501 |
| FastAPI Backend | 8000 |

## 🔐 11. Security Considerations

- API keys are stored in environment variables.
- `.env` is excluded from Docker builds using `.dockerignore`.
- Sensitive credentials should not be committed to GitHub.
- AWS Security Group rules control inbound application traffic.
- Backend access should be restricted to trusted sources where possible.

## 🧪 12. Testing and Validation

The following deployment checks were performed:

| Validation | Expected Result |
|---|---|
| Docker image build | Successful |
| ECR image push | Successful |
| EC2 image pull | Successful |
| Docker container startup | Running |
| FastAPI documentation | HTTP 200 OK |
| Streamlit endpoint | HTTP 200 OK |
| External port connectivity | Successful |

## 🚀 13. Future Enhancements

- Custom domain name and HTTPS configuration.
- Improved conversational memory.
- User authentication and profile management.
- Enhanced monitoring and application logging.
- Automated CI/CD deployment pipeline.
- Additional AI-powered beauty assistance capabilities.

## 👩‍💻 14. Project Conclusion

GlowTouch demonstrates the integration of Generative AI, Python backend development, interactive frontend development, containerization, and cloud deployment.

This project provided practical experience in integrating an AI model with application services, developing REST APIs, building a user interface, creating Docker images, managing container registries, and deploying an application on AWS EC2.

**The final outcome is a cloud-hosted AI-powered application accessible through a web browser.**

---

**Project Name:** GlowTouch – AI-Powered Beauty Assistant  
**Backend:** FastAPI  
**Frontend:** Streamlit  
**AI Model:** Google Gemini  
**Containerization:** Docker  
**Cloud Platform:** AWS  
**Container Registry:** AWS ECR
