# 🔗 **Load-Balanced URL Shortener using Docker & Kubernetes**

The **URL Shortener** is a scalable, containerized service that allows users to shorten long URLs and seamlessly redirect to the original ones. Built using **Flask** and **Redis**, and deployed via **Docker** and **Kubernetes**, the project is designed for horizontal scalability and high availability. Features like **Ingress routing**, **Horizontal Pod Autoscaling**, and **Redis-based persistence** make it production-ready and cloud-native.

---

## 📜 **Overview**

The system is composed of microservices orchestrated through Kubernetes:

- **Flask App**: Handles API requests to shorten and expand URLs.
- **Redis**: Stores mappings between short and long URLs.
- **Docker**: Used to containerize the application.
- **Kubernetes**: Handles deployment, scaling, and networking.
- **Ingress Controller**: Exposes the application via a custom domain.
- **HPA (Horizontal Pod Autoscaler)**: Scales application pods automatically based on resource usage.

---

## 🚀 **Features**

- 🔗 Generate and manage short URLs.
- 📦 Fully containerized with Docker.
- ☁️ Deployed using Kubernetes for easy scalability.
- ⚖️ Load balanced using Kubernetes Ingress.
- 🔁 Automatically scaled using HPA and Metrics Server.
- 🔐 Secrets and ConfigMaps for secure and configurable deployments.

---

## 🛠 **Setup Instructions**

### 1. **Docker Build and Push (Optional)**

Build the image locally:

```bash
docker build -t url-shortener:latest .
```

Login to Docker Hub and push your image:

```bash
docker login
docker tag url-shortener:latest shivadarshan/url-shortener:latest
docker push shivadarshan/url-shortener:latest
```

---

### 2. **Kubernetes Deployment**

Apply all the Kubernetes manifests:

```bash
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml
kubectl apply -f url-shortener-deployment.yaml
kubectl apply -f url-shortener-service.yaml
kubectl apply -f configmap.yaml
kubectl apply -f redis-secret.yaml
```

---

### 3. **Verify Redis Connection**

Check if Redis pods are running:

```bash
kubectl get pods -l app=redis
```

Enter the Redis container:

```bash
kubectl exec -it <redis-pod-name> -- sh
```

Access Redis CLI:

```bash
redis-cli -n 0
AUTH PESU123#
```

> Replace `PESU123#` with your actual Redis password from the Kubernetes secret.

---

## 📊 **Autoscaling with HPA**

### 1. **Enable Metrics Server**

```bash
minikube addons enable metrics-server
```

### 2. **Create Horizontal Pod Autoscaler**

```bash
kubectl autoscale deployment url-shortener \
  --cpu-percent=50 \
  --min=3 \
  --max=7
```

Check the autoscaler:

```bash
kubectl get hpa
```

---

## 🌐 **Enable Ingress Routing**

### 1. **Enable Ingress Addon**

```bash
minikube addons enable ingress
```

### 2. **Set Up Domain**

Find your Minikube IP:

```bash
minikube ip
```

Edit your hosts file:

```bash
sudo nano /etc/hosts
```

Add:

```
<minikube-ip> url-shortener.local
```

Now access the application at:

```bash
http://url-shortener.local
```

---

## 🔐 **Handling Secrets**

Base64 encode your Redis password:

```bash
echo -n "password" | base64
```

Paste the encoded string into `redis-secret.yaml`.

---

## 🧰 **Helpful Kubernetes Commands**

List all pods:

```bash
kubectl get pods
```

Check logs of a specific pod:

```bash
kubectl logs <pod-name>
```

List services:

```bash
kubectl get svc
```

View deployments:

```bash
kubectl get deployments
```

Describe a specific pod:

```bash
kubectl describe pod <pod-name>
```

Delete a Kubernetes resource:

```bash
kubectl delete -f <filename>.yaml
```

---

## 👨‍💻 **Author**

- [Shivadarshan](https://github.com/shivadarshan-devadiga)

---

## 📜 **License**

This project is licensed under the [MIT License](LICENSE).

---

## 💬 **Feedback and Support**

For suggestions or issues, feel free to open an issue on GitHub:

[Open an Issue](https://github.com/shivadarshan-devadiga/url-shortener/issues)

---

Thank you for checking out the **URL Shortener** project! 🎉
```

---
