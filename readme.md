# 🛒 E-commerce ML Pipeline  
*A modular, production-style machine learning pipeline built with Python.*

This project demonstrates how to structure a **real ML engineering codebase** using:

- Python packages & modules  
- Virtual environments  
- Unit tests (pytest)  
- Logging  
- Feature engineering  
- Data pipelines  
- Clean project structure  
- Git version control  

The dataset used is the **Brazilian E-Commerce Public Dataset by Olist** (Kaggle).

---

## 📂 Project Structure

ecommerce_ml/
│
├── ecommerce_ml/ # Main Python package
│ ├── init.py
│ ├── data_loading.py # Load raw CSVs
│ ├── preprocessing.py # Feature engineering
│ ├── models.py # ML model wrapper (coming next)
│ ├── training.py # Training pipeline (coming next)
│ └── cli.py # Command-line interface (coming next)
│
├── tests/ # Unit tests
│ ├── test_data_loading.py
│ └── test_preprocessing.py
│
├── data/ # Raw + processed data (ignored by Git)
│ └── raw/
│
├── notebooks/ # Exploration notebooks
│ └── exploration.ipynb
│
├── scripts/ # Optional helper scripts
│
├── .gitignore
├── README.md
└── requirements.txt (optional)




---

## 🎯 Project Goals

This project is designed to exercise **real ML engineering skills**:

- Writing clean, modular Python code  
- Structuring a project like an industry ML repo  
- Testing data pipelines  
- Using loggers instead of prints  
- Organizing preprocessing steps  
- Preparing for model training & deployment  
- Practicing Git, GitHub, and reproducibility  

This is *not* just a notebook — it is a **proper Python package**.

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/nehlehk/ecommerce_ml.git
cd ecommerce_ml
```


###  2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install basic dependencies
```bash
pip install pandas numpy scikit-learn pytest

```

## 📥 Dataset
Download the Olist dataset from Kaggle:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Place all CSVs into:
```bash
data/raw/
```
This folder is already included in .gitignore.

## 🧪 Running Tests

All tests use pytest.

From the project root:
```bash
pytest -v
```

You should see tests for:

Data loading

Preprocessing pipelines


### 🔧 Usage 

When cli.py is finished, you'll be able to run:
```bash
python3 -m ecommerce_ml.cli train

```

## 🛠️ Features (current & planned)
### ✔ Implemented

Clean project structure

Python package ecommerce_ml

Data loading with logging

Preprocessing with feature engineering

Unit tests for core functionality

### 🔜 Coming next

OOP model wrapper (models.py)

Training pipeline (training.py)

CLI entry point (cli.py)

Config-driven experiment setup

Model evaluation

Deployment example


## 📝 License

This project is for educational and demonstration purposes only.
Dataset copyright belongs to the original Kaggle provider.

## 👩‍💻 Author

Nahleh Kargarfard
