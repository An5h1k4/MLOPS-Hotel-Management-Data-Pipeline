# 🏨 Hotel Reservation Cancellation Prediction  
### Production-Grade ML + MLOps System on GCP 🚀

This project builds a **cloud-native machine learning system** to predict hotel reservation cancellations and deploy it using a fully automated CI/CD pipeline.

It is designed with **real-world MLOps architecture principles**, not just model training.

---

# 📌 Problem Statement

Predict whether a hotel booking will be cancelled before check-in.

### Business Impact

- Enable smart overbooking
- Prevent revenue loss
- Reduce cancellation churn
- Detect fraudulent booking patterns

---

# 🧠 System Architecture

```
GCP Bucket
    ↓
Data Ingestion (Service Account Auth)
    ↓
Data Processing
    ↓
Model Training (MLflow Tracking)
    ↓
Training Pipeline
    ↓
Docker Image
    ↓
Jenkins CI/CD
    ↓
Google Container Registry (GCR)
    ↓
Google Cloud Run Deployment
```

---

# 🗂 Project Structure

```
Hotel_Reservation_Prediction/
│
├── artifacts/          # Processed data + trained models
├── config/             # YAML configs + model params
├── logs/               # Logging files
├── notebook/           # EDA & experimentation
├── pipeline/           # Training pipeline
├── src/                # Core ML modules
├── utils/              # Common reusable functions
├── templates/          # HTML templates
├── static/             # CSS/JS
├── Dockerfile
├── setup.py
├── requirements.txt
└── application.py
```

---

# ⚙️ How To Use This Project

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/An5h1k4/MLOPS-Hotel-Management-Data-Pipeline.git
cd hotel-reservation-mlops
```

---

## 2️⃣ Create Virtual Environment

```bash
conda create -p venv python=3.10 -y
conda activate venv/
pip install -r requirements.txt
pip install -e .
```

Why `pip install -e .`?

It installs the project as a local package so that imports like:

```
from src.data_ingestion import DataIngestion
```

work properly across directories.

---

## 3️⃣ Setup GCP Credentials

- Create Service Account
- Assign:
  - Storage Admin
  - Storage Object Viewer
- Download JSON key

Set environment variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/key.json"
```

---

## 4️⃣ Run Full Training Pipeline

```bash
python pipeline/training_pipeline.py
```

This executes:

- Data ingestion
- Data preprocessing
- Model training
- Model saving
- MLflow experiment tracking

---

## 5️⃣ Launch MLflow UI

```bash
mlflow ui
```

Open:

```
http://localhost:5000
```

Track:
- Parameters
- Metrics
- Model artifacts
- Run comparison

---

## 6️⃣ Run Flask App Locally

```bash
python application.py
```

Access:

```
http://localhost:5000
```

---

# 🐳 Running with Docker

## Build Image

```bash
docker build -t hotel-mlops .
```

## Run Container

```bash
docker run -p 5000:5000 hotel-mlops
```

---

# 🔁 CI/CD Workflow

### Trigger: Git Push

```
Developer → GitHub → Jenkins → Docker Build → GCR → Cloud Run
```

---

# ☁️ Cloud Deployment (Google Cloud Run)

Deployment Flow:

1. Jenkins builds Docker image
2. Pushes image to GCR
3. Cloud Run pulls image
4. Container becomes publicly accessible

Cloud Run handles:
- Auto-scaling
- Load balancing
- HTTPS endpoints
- Zero server management

---

# 📊 ML Details

- Algorithm: LightGBM
- Evaluation Metric: Accuracy
- Multicollinearity Check: VIF (Statsmodels)
- Encoding: Label Encoding
- Config-driven column selection

---

# 🧪 Experiment Tracking (MLflow)

Why we use MLflow:

Without tracking:
- Model 2 overwrites Model 1
- No reproducibility
- No audit trail

With MLflow:
- Version control for models
- Metric comparison
- Artifact storage
- Production promotion capability

---

# 📦 Data Versioning Strategy

Small datasets:
- Git versioning

Large datasets:
- DVC (Data Version Control)

Why DVC?
- Git is inefficient for large data
- Keeps data out of repo
- Tracks metadata and changes
- Reproducible pipelines

---

# 🔍 Technical Concepts Not Obvious (DevOps Deep Dive)

---

## 1️⃣ Why Service Accounts Instead of Admin Credentials?

Service accounts:
- Follow principle of least privilege
- Restrict bucket access
- Prevent credential leakage
- Production-ready authentication

Never hardcode credentials inside application.

---

## 2️⃣ Why Config-Driven Architecture?

All paths, parameters, column definitions stored in `config.yaml`.

Benefits:
- Zero hardcoded paths
- Easy environment switching
- Supports dev / staging / production configs

---

## 3️⃣ Why Custom Logging + Exception Handling?

Instead of printing errors:

- Centralized logging
- Structured error tracing
- Production observability
- Easier debugging in CI/CD

---

## 4️⃣ Why Docker Instead of Virtualenv in Production?

Virtualenv:
- Works locally

Docker:
- OS-level reproducibility
- Identical dev/prod environment
- No dependency conflicts
- Portable deployment

---

## 5️⃣ Why Jenkins Instead of Manual Deployment?

Manual deployment risks:
- Human errors
- Inconsistent builds
- No rollback strategy

Jenkins provides:
- Automated build pipelines
- Controlled deployment
- Integration with SCM
- Continuous testing

---

## 6️⃣ Why Cloud Run Instead of VM?

VM:
- Requires manual scaling
- Costly idle resources

Cloud Run:
- Serverless
- Auto-scaling
- Pay-per-request
- Zero infrastructure management

---

## 7️⃣ Why Use Setup.py?

It makes the project:

- Installable as a package
- Cleaner imports
- Modular
- Production structured

---

# 🚀 Production Improvements (Next Level)

- Add model registry (MLflow registry)
- Add drift detection
- Add Prometheus monitoring
- Add API authentication
- Add Canary deployment
- Add Kubernetes orchestration

---

# 📈 Key Engineering Highlights

- Modular pipeline design
- Cloud-native deployment
- CI/CD automation
- Config-driven architecture
- Secure credential management
- Experiment reproducibility
- Data + Code versioning

---

# 👩‍💻 Author

Anshika Gautam  
AI/ML Engineer | MLOps Enthusiast  
Building production-grade ML systems 🚀
