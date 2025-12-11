# AWS EC2 Name Generator

This project provides a Python-based tool for generating standardized and unique EC2 instance names across multiple departments in an AWS environment.

## 🎯 Objective

Ensure that EC2 instances follow a consistent and readable naming convention to improve:

- Resource identification  
- Cost allocation  
- Cloud infrastructure organization  
- Automation workflows  

This script generates descriptive and unique EC2 instance names by combining a department name and a random alphanumeric suffix.

---

## 🔧 Features

- User input for the number of EC2 names to generate  
- User input for department name  
- Automatic random suffix generation  
- Clean and standardized EC2 naming format  
- Lightweight and easy to integrate into automation workflows  

---

## 🏗️ Project Architecture

ec2-name-generator/
├── main.py
└── README.md

The project is intentionally simple, containing a Python script and its documentation in the root directory.

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ec2-name-generator.git

3. Run the script

python3 main.py

📁 Example Output

finance-web-2A9
hr-app-F3K
security-api-9ZQ
it-backend-7M2


🧠 What I Learned
	•	How to organize and document a simple cloud automation script
	•	Importance of AWS naming conventions for EC2 resources
	•	Handling user input and random generation in Python
	•	Best practices for writing clean and readable Python code
	•	Structuring a beginner DevOps/Cloud project with clear documentation
