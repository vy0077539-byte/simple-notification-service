# Simple Notification Service on AWS 🚀

A cloud-based notification service fully designed and deployed on Amazon Web Services (AWS).  
This project focuses on AWS infrastructure, security, and service integration rather than application frameworks.

---

## 🌐 Project Overview
- **Cloud Provider:** Amazon Web Services (AWS)
- **Deployment Type:** Infrastructure-based deployment
- **Status:** Successfully deployed and tested

This project demonstrates how to build a secure and scalable notification system using core AWS services.

---

## 📌 Key Features
- Custom VPC and subnet configuration
- Secure EC2 instance with IAM role-based access
- Notification delivery using AWS SNS
- Network security using Security Groups
- Monitoring and logging using CloudWatch
- No hardcoded credentials (IAM best practices)

---

## 🏗 Architecture Components
- **VPC:** Isolated virtual network
- **Subnet:** Logical segmentation of the VPC
- **Route Table & Internet Gateway:** Internet connectivity
- **Security Group:** Acts as a virtual firewall
- **IAM Role & Policies:** Secure access to AWS services
- **EC2 Instance:** Hosts the notification service
- **AWS SNS:** Publishes and delivers notifications
- **CloudWatch:** Logs and monitoring

---

## 🛠 AWS Services Used
- Amazon VPC
- Subnets (CIDR-based)
- Internet Gateway
- Route Tables
- Security Groups
- IAM (Roles & Policies)
- Amazon EC2
- Amazon SNS
- Amazon CloudWatch

---

## 🔁 Notification Flow
1. Infrastructure is created inside a custom VPC
2. EC2 instance is launched within a subnet
3. IAM role is attached to EC2 for secure permissions
4. EC2 publishes messages to an SNS topic
5. SNS delivers notifications to subscribed endpoints
6. Logs and metrics are monitored via CloudWatch

---

## 🚀 Deployment Steps (High-Level)
1. Created a custom VPC
2. Configured subnet with CIDR validation
3. Set up route tables and internet gateway
4. Created IAM role with required permissions
5. Attached IAM role to EC2 instance
6. Configured Security Group rules
7. Launched EC2 instance
8. Created SNS topic and subscriptions
9. Tested notification delivery
10. Verified logs in CloudWatch

---

## 🔐 Security Practices
- IAM role-based access (no access keys in code)
- Least privilege IAM policies
- Restricted Security Group rules
- Isolated VPC networking

---

## 📘 What I Learned
- AWS VPC and subnet design
- IAM roles and permission management
- EC2 networking and security configuration
- Integrating EC2 with AWS SNS
- Monitoring AWS resources using CloudWatch
- Real-world AWS infrastructure deployment

---

## 🔮 Future Enhancements
- Auto Scaling and Load Balancer
- Dead Letter Queue (DLQ) for failed notifications
- API Gateway integration
- CI/CD pipeline using GitHub Actions or AWS CodePipeline
- Infrastructure as Code (Terraform / CloudFormation)

---

## 🤝 Feedback
This project is part of my hands-on AWS and cloud learning journey.  
Feedback and suggestions are welcome.

---

### ⭐ If you find this project useful, feel free to star the repository!
