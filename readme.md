# AWS AIOps Demo

A comprehensive demonstration of AI-powered operations (AIOps) for monitoring, detecting, and remediating issues in a containerized Flask application deployed on Amazon EKS.

## 🏗️ Architecture

This project showcases a complete AIOps pipeline:

- **Flask Application**: Simple web app with intentional performance issues for demo purposes
- **Containerization**: Docker-based deployment with multi-stage builds
- **CI/CD Pipeline**: GitHub Actions with AI-powered code review using Amazon Bedrock
- **Container Registry**: Amazon ECR for storing Docker images
- **Orchestration**: Kubernetes deployment on Amazon EKS
- **Monitoring**: CloudWatch alarms for anomaly detection
- **AI Analysis**: Automated root cause analysis using generative AI

## 📁 Project Structure

```
myaiops/
├── readme.md                 # Project documentation
├── app/
│   ├── sample.py             # Flask application with intentional bugs
│   ├── dockerfile            # Docker container definition
│   ├── k8s/
│   │   ├── deployment.yaml   # Kubernetes deployment manifest
│   │   └── service.yaml      # Kubernetes service manifest
│   └── cicd/
│       ├── ai/
│       │   └── ai-review.py  # AI code review script (Bedrock)
│       └── github-actions/
│           └── ai-ci.yaml    # GitHub Actions CI/CD workflow
```

## 🚀 Prerequisites

- AWS Account with appropriate permissions
- Amazon EKS cluster (`aiops-cluster`)
- GitHub repository with the following secrets:
  - `AWS_KEY`: AWS access key ID
  - `AWS_SECRET`: AWS secret access key
  - `AWS_ACCOUNT_ID`: Your AWS account ID
- Local development:
  - Python 3.10+
  - Docker
  - kubectl configured for your EKS cluster

## 🛠️ Local Development

### Running the Application Locally

```bash
cd app
python sample.py
```

The app will be available at `http://localhost:5000`

### Building Docker Image

```bash
docker build -t aiops-demo ./app
docker run -p 5000:5000 aiops-demo
```

## 🚀 Deployment

### Automated CI/CD

1. Push changes to the main branch
2. GitHub Actions will:
   - Run AI code review using Amazon Bedrock
   - Build and push Docker image to ECR
   - Deploy to EKS cluster

### Manual Deployment

```bash
# Build and push image
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
docker build -t aiops-demo ./app
docker tag aiops-demo:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/aiops-demo:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/aiops-demo:latest

# Deploy to Kubernetes
kubectl apply -f app/k8s/
```

## 📊 Monitoring & AIOps

### CloudWatch Alarm Setup

```bash
aws cloudwatch put-metric-alarm \
  --alarm-name HighCPU-AIOps \
  --metric-name CPUUtilization \
  --namespace AWS/EKS \
  --statistic Average \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2
```

### AI Root Cause Analysis

The system uses Amazon Bedrock to analyze logs and metrics for automated incident response:

- Detects CPU spikes, latency increases, and pod restarts
- Provides root cause analysis and remediation suggestions
- Integrates with existing monitoring tools

## 🔧 Configuration

### Environment Variables

The application supports the following environment variables:

- `PORT`: Server port (default: 5000)
- `DEBUG`: Enable debug mode (default: false)

### Kubernetes Resources

- **CPU Limit**: 500m per pod
- **Replicas**: 1 (can be scaled as needed)
- **Service Type**: LoadBalancer

## 🐛 Intentional Issues

This demo includes intentional bugs for AIOps demonstration:

- **Artificial Latency**: 2-second delay on home route
- **CPU Spike**: Infinite loop on `/crash` endpoint
- **Resource Constraints**: Limited CPU allocation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run AI code review: `python app/cicd/ai/ai-review.py`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions or issues, please open a GitHub issue or contact the maintainers.
