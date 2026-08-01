<div align="center">

# ❤️ Heart Disease Prediction using Machine Learning

### End-to-End Machine Learning Model Deployment using Flask, GitHub & Render

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Flask](https://img.shields.io/badge/Flask-Web%20API-black?logo=flask)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-purple?logo=numpy)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?logo=github)
![Render](https://img.shields.io/badge/Render-Cloud%20Deployment-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

Predict whether a patient is at risk of **Heart Disease** using Machine Learning and deploy the model as a **REST API** using **Flask** on **Render**.

</div>

---

# 🌐 Live Demo

### 🚀 Render Deployment

**https://heartdiseasedeployment-7fyf.onrender.com**

### 📂 GitHub Repository

**https://github.com/chouhanshaktiraj-netizen/HeartDiseaseDeployment**

---

# 📖 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction using clinical parameters can help healthcare professionals identify high-risk patients and improve treatment planning.

This project demonstrates an **End-to-End Machine Learning Deployment Pipeline**, including:

- Data preprocessing
- Model training
- Model evaluation
- Model serialization
- REST API development using Flask
- GitHub version control
- Cloud deployment using Render

---

# 🎯 Objectives

- Predict heart disease using patient clinical information.
- Build a supervised Machine Learning classification model.
- Develop a Flask REST API.
- Deploy the application on Render.
- Provide real-time predictions through JSON requests.

---

# 📊 Dataset

**Dataset:** Heart Disease Dataset

Source:
https://www.kaggle.com/datasets/johnsmith88/heart-diseasedataset

The dataset contains clinical information such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope
- Number of Major Vessels
- Thalassemia

Target Variable:

- **0 → No Heart Disease**
- **1 → Heart Disease**

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-Learn | Machine Learning |
| Flask | REST API |
| Joblib | Model Serialization |
| GitHub | Version Control |
| Render | Cloud Deployment |

---

# 🤖 Machine Learning Workflow

```
Heart Disease Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Train-Test Split
        │
        ▼
Random Forest Classifier
        │
        ▼
Model Evaluation
        │
        ▼
Save model.pkl
        │
        ▼
Flask REST API
        │
        ▼
GitHub
        │
        ▼
Render Deployment
```

---

# 📁 Repository Structure

```
HeartDiseaseDeployment/
│
├── app.py
├── train_model.py
├── model.pkl
├── heart.csv
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
│
└── templates/
    └── index.html
```

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Loaded dataset using Pandas
- Displayed first five records
- Identified numerical features
- Selected target variable
- Checked missing values
- Split dataset into:
  - 80% Training
  - 20% Testing

---

# 🧠 Model Development

Algorithm Used:

✅ Random Forest Classifier

Evaluation Metric:

- Accuracy Score

The trained model was saved using:

```
model.pkl
```

---

# 🌐 Flask REST API

### Endpoint

```
POST /predict
```

### Sample Request

```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```

### Sample Response

```json
{
    "prediction":"Heart Disease Detected"
}
```

---

# 🚀 Deployment

The Flask application has been successfully deployed on **Render**.

Live URL:

**https://heartdiseasedeployment-7fyf.onrender.com**

---

# 📸 Project Screenshots

Create a folder named:

```
screenshots
```

Add the following images:

```
screenshots/
│
├── dataset.png
├── training.png
├── flask.png
├── api.png
├── render.png
├── homepage.png
```

Then include:

## Dataset Preview

```
![Dataset](screenshots/dataset.png)
```

## Model Training

```
![Training](screenshots/training.png)
```

## Flask API

```
![Flask](screenshots/flask.png)
```

## API Testing

```
![API](screenshots/api.png)
```

## Render Deployment

```
![Render](screenshots/render.png)
```

## Home Page

```
![Home](screenshots/homepage.png)
```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/chouhanshaktiraj-netizen/HeartDiseaseDeployment.git
```

Move into the project directory

```bash
cd HeartDiseaseDeployment
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

# 📈 Future Improvements

- Add a responsive frontend
- Improve model accuracy using Hyperparameter Tuning
- Dockerize the application
- Add CI/CD pipeline using GitHub Actions
- Deploy using Kubernetes
- Add user authentication
- Store prediction history in a database

---

# 🎓 Learning Outcomes

Through this project, I learned:

- End-to-End Machine Learning Workflow
- Data Preprocessing
- Classification using Random Forest
- Model Serialization
- Flask REST API Development
- GitHub Version Control
- Cloud Deployment using Render
- MLOps Deployment Fundamentals

---
---

# 🌟 Project Highlights

- ✅ End-to-End Machine Learning Pipeline
- ✅ Random Forest Classification Model
- ✅ Data Preprocessing and Model Evaluation
- ✅ Flask REST API Development
- ✅ Model Serialization using Joblib
- ✅ API Testing with Postman
- ✅ Version Control using GitHub
- ✅ Cloud Deployment using Render
- ✅ Production-Ready Machine Learning Application

---

# 📝 Conclusion

This project successfully developed and deployed a **Random Forest** machine learning model to predict the risk of heart disease using clinical parameters. The model achieved strong predictive performance, demonstrating its ability to classify patients effectively based on the provided dataset. During deployment, challenges such as managing project dependencies, configuring the Flask application, creating deployment files (`requirements.txt`, `Procfile`, and `runtime.txt`), and ensuring compatibility with the Render hosting platform were successfully resolved. This project highlights the importance of **MLOps** practices, including version control with GitHub, model serialization, REST API development, and cloud deployment. These practices make machine learning solutions reproducible, scalable, and production-ready, bridging the gap between model development and real-world application.

---
# 👨‍💻 Author

**Shaktiraj Singh Chouhan**

Integrated M.Tech in Artificial Intelligence

VIT Bhopal University

GitHub:

https://github.com/chouhanshaktiraj-netizen

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

# 📄 License

This project is licensed under the **MIT License**.