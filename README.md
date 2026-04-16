## Overview
The objective of this project was to automate the deployment and management of containerized applications within a Kubernetes cluster. By using Helm as a package manager, I was able to simplify the deployment process and manage all infrastructure components as a single, organized package. 

## Tech Stack
* **Container Management:** Kubernetes (Minikube) managed with Helm
* **Scripting:** Python 
* **Environment:** Ubuntu (WSL)
* **Web Server:** Nginx (Containerized)

## Key Features & DevOps Principles
* **Simplified Deployment:** Used **Helm** to group Kubernetes templates into a single package, making it possible to set up the entire environment with one `helm install` command.
* **Health Monitoring with Python:** Developed a script in **Python** that checks the status of pods using `kubectl`. It helped me learn how to automate manual status checks and respond to service downtime.
* **Kubernetes Fundamentals:** Gained experience with **Pod lifecycles** and controllers, understanding how Kubernetes automatically keeps the requested number of containers running.
* **Scaling Practice:** Configured the project so that changing the number of running instances (replicas) is done by simply updating a single variable in Helm, rather than editing multiple files.

## Project Structure
- **my-nginx/**: The complete Helm chart directory, containing the infrastructure templates and the `values.yaml` configuration file.
- **health_check.py**: A custom Python script used to monitor the status of Kubernetes pods and verify the deployment.
