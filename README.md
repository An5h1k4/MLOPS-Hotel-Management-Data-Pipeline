# 🏨 Hotel Reservation Cancellation Prediction  
### End-to-End MLOps Project on GCP 🚀  

Can we predict whether a customer will cancel their hotel reservation?

This project builds a **production-ready machine learning system** that predicts reservation cancellations and deploys it on **Google Cloud Run** using a complete **CI/CD + Docker + Jenkins + MLflow + DVC pipeline**.

---

## 📌 Business Problem

Hotels face heavy revenue loss due to last-minute cancellations.

### 🎯 Target Audience  
- Hotel Revenue Management Teams  
- Operations Teams  
- Fraud Detection Teams  

---

## 💼 Real-World Use Cases

### 1️⃣ Revenue Management  
Predict high cancellation probability → Enable **smart overbooking strategy**.

### 2️⃣ Retention Strategy  
If cancellation probability is high → Offer **discounts or incentives** to prevent churn.

### 3️⃣ Fraud Detection  
Identify suspicious booking patterns → Prevent coordinated cancellation scams.

---

# 🧠 ML + MLOps Architecture

```
GCP Bucket → Data Ingestion → Data Processing → Model Training (MLflow)
        → Training Pipeline → Docker → Jenkins CI/CD → GCR → Cloud Run
```

---

# 🗂 Project Structure

```
Hotel_Reservation_Prediction/
│
├── artifacts/                # Stores processed data & trained models
├── config/                   # YAML configs & model parameters
├── logs/                     # Log files
├── notebook/                 # Jupyter experiments
├── pipeline/                 # Training pipeline
├── src/                      # Core ML modules
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── model_train.py
│   ├── logger.py
│   ├── custom_exception.py
│
├── utils/                    # Common helper functions
├── templates/                # HTML templates (Flask app)
├── static/                   # CSS / JS
├── setup.py
├── requirements.txt
├── Dockerfile
├── application.py
└── config.yaml
```

---

# ⚙️ Tech Stack

## ☁️ Cloud
- Google Cloud Platform (GCP)
- GCP Buckets
- Google Cloud Run
- Google Container Registry (GCR)

## 🔄 Data Engineering
- Apache Airflow (ETL)
- Kafka (Streaming)
- GCP Service Accounts
- YAML Config Driven Design

## 🤖 Machine Learning
- Scikit-learn
- LightGBM
- Statsmodels (Multicollinearity Check)
- MLflow (Experiment Tracking)

## 🚀 MLOps
- DVC (Data Versioning)
- Git (Code Versioning)
- Docker
- Jenkins (CI/CD)
- GitHub Actions (Optional)

## 🌐 Backend
- Flask
- HTML/CSS

---

# 🔄 End-to-End Pipeline

---

## 1️⃣ Database Setup (GCP Bucket)

- Create bucket
- Upload `Hotel_Reservation.csv`
- Create Service Account
- Generate JSON Key
- Set credentials

```bash
gcloud --version
```

---

## 2️⃣ Virtual Environment Setup

```bash
conda create -p venv python=3.10 -y
conda activate venv/
pip install -r requirements.txt
pip install -e .
```

---

## 3️⃣ Data Ingestion (From GCP)

✔ Connect using service account  
✔ Download dataset  
✔ Split into train/test  
✔ Store in `artifacts/`

Output:

```
artifacts/
   ├── raw.csv
   ├── train.csv
   └── test.csv
```

---

## 4️⃣ Exploratory Data Analysis (Notebook)

- Remove unwanted columns
- Null & duplicate check
- Univariate analysis
- Histograms & boxplots
- Categorical distribution plots
- Multicollinearity check (VIF > 5 → High)

---

## 5️⃣ Data Processing

- Divide categorical & numerical columns (via config.yaml)
- Label Encoding
- Feature transformation
- Save processed data in:

```
artifacts/processed/
```

---

## 6️⃣ Model Training + MLflow Tracking

Model 1:
- 1000 rows
- 90% accuracy

Model 2:
- 1200 rows
- 92% accuracy ✅ (Selected)

### Why MLflow?

Because model2 overwrites model1 → We track:
- Parameters
- Metrics
- Artifacts
- Model versions

```bash
mlflow ui
```

---

## 7️⃣ Training Pipeline

Combine:
- Data Ingestion
- Data Processing
- Model Training

Run:

```bash
python pipeline/training_pipeline.py
```

---

## 8️⃣ Versioning

### 🔹 Code Versioning

```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

### 🔹 Data Versioning

- Small data → Git  
- Large data → DVC  

---

# 🌐 User Application (Flask)

Non-technical users can:

✔ Upload booking details  
✔ Get cancellation probability  
✔ Take action  

Run locally:

```bash
python application.py
```

---

# 🐳 Dockerization

### Dockerfile

```dockerfile
FROM python:slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -e .
EXPOSE 5000
CMD ["python", "application.py"]
```

### Build & Run

```bash
docker build -t hotel-cancel .
docker run -p 5000:5000 hotel-cancel
```

---

# 🔁 CI/CD Pipeline (Jenkins)

### Flow

```
GitHub Push
    ↓
Jenkins Pipeline
    ↓
Docker Build
    ↓
Push to GCR
    ↓
Deploy to Cloud Run
```

---

## Jenkins Setup (Docker-in-Docker)

```bash
docker run -d --name jenkins-dind \
--privileged \
-p 8080:8080 -p 50000:50000 \
-v //var/run/docker.sock:/var/run/docker.sock \
-v jenkins_home:/var/jenkins_home \
jenkins_dind
```

Access Jenkins:

```
http://localhost:8080
```

---

# ☁️ Deployment on Google Cloud Run

After CI/CD setup:

```
Push Code → Automated Build → GCR → Cloud Run
```

Your ML system is now fully automated and production-ready 🚀

---

# 📊 Key Highlights

✔ End-to-End ML Pipeline  
✔ Production Ready Architecture  
✔ Config-Driven Development  
✔ Custom Logging & Exception Handling  
✔ MLflow Experiment Tracking  
✔ Dockerized Application  
✔ Automated CI/CD  
✔ Cloud Deployment  

---

# 📈 Future Improvements

- Add Feature Store  
- Add Model Monitoring  
- Add Drift Detection  
- Switch to Kubernetes  
- Add API authentication  
- Add real-time streaming inference  

---

# 👩‍💻 Author

**Anshika Gautam**  
AI/ML | MLOps | Data Engineering  

Building production-grade ML systems 🚀
