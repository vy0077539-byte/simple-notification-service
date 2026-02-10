# AWS File Upload Service 🚀

A simple cloud-based file upload application built using Python (Flask) and deployed on Amazon Web Services (AWS).  
This project allows users to upload files through a web interface and securely store them in an Amazon S3 bucket.

---

## 🌐 Project Overview
- **Backend:** Python (Flask)
- **Cloud Provider:** Amazon Web Services (AWS)
- **Compute:** Amazon EC2
- **Storage:** Amazon S3
- **Status:** Deployed and working

---

## 📌 Features
- Web-based file upload using Flask
- Secure file storage in Amazon S3
- IAM role-based access (no hardcoded AWS keys)
- Deployed on AWS EC2
- Secure file handling using `secure_filename`

---

## 🏗 Architecture
- **EC2 Instance:** Hosts the Flask application
- **IAM Role:** Grants EC2 permission to access S3
- **S3 Bucket:** Stores uploaded files
- **Security Group:** Controls network access to EC2

---

## 🛠 Tech Stack
- Python
- Flask
- AWS EC2
- AWS S3
- AWS IAM
- AWS Security Groups

---

## 📂 Project Structure
aws-file-upload-service/ │ ├── app.py ├── requirements.txt ├── README.md └── .gitignore---

## 🔁 Application Flow
1. User opens the web page
2. Selects a file to upload
3. Flask receives the file request
4. File is uploaded to Amazon S3 using boto3
5. Success message is returned to the user

---

## 🚀 Deployment Steps (High-Level)
1. Created an IAM role with S3 permissions
2. Launched an EC2 instance
3. Attached IAM role to EC2
4. Installed Python and project dependencies
5. Created an S3 bucket
6. Deployed the Flask application on EC2
7. Tested file upload functionality

---

## 🔐 Security Best Practices
- IAM roles used instead of access keys
- Least privilege permissions
- Secure file handling
- Restricted Security Group rules

---

## 📘 What I Learned
- Deploying Flask applications on AWS EC2
- Integrating Python applications with Amazon S3
- Using IAM roles for secure AWS access
- Basic cloud security best practices
- Real-world AWS deployment workflow

---

## 🔮 Future Improvements
- Add user authentication
- File size and type validation
- Nginx + Gunicorn setup
- HTTPS using Load Balancer
- CloudWatch monitoring

---

## 🤝 Feedback
This project is part of my hands-on AWS and cloud learning journey.  
Feedback and suggestions are welcome.

---

### ⭐ If you find this project useful, feel free to star the repository!
