# Automated CI/CD Pipeline

Production-grade CI/CD pipeline that builds, tests, and deploys a
containerized Python application to AWS EC2 using GitHub Actions.

## Tech Stack

GitHub Actions, Docker, Terraform, AWS (EC2, ECR, VPC, CloudWatch, IAM)

## Pipeline Flow

Push to GitHub -> Run Tests -> Build Docker Image -> Push to ECR ->
Deploy to EC2 via SSH -> Health Check
