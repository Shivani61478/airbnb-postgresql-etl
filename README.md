# Airbnb ETL Pipeline 🏠

A Data Engineering project that extracts Airbnb listing data from a Kaggle dataset, transforms and cleans the data using Pandas, and loads the processed data into a PostgreSQL database.

---

# Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using real-world Airbnb listing data.

The pipeline:

• Extracts Airbnb listing data from a Kaggle dataset
• Cleans and transforms raw records using Pandas
• Loads the processed dataset into PostgreSQL
• Records ETL execution details using Python logging

---

# Dataset Source

The raw dataset used in this project was sourced from Kaggle:

Airbnb Open Data Dataset:
https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata

Note: The original dataset (~35 MB) is not included in this repository. Please download it from the Kaggle link above before running the project.

---

# Tech Stack

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* psycopg2

---

# Project Workflow

```text
Kaggle Airbnb Dataset
          ↓
     Extract Data
          ↓
 Transform & Clean Data
          ↓
 Load into PostgreSQL
          ↓
 Structured Data Storage
```

---

#  Project Output & Results

### ETL Pipeline Execution
![ETL Pipeline Execution](screenshots/terminal.png)

### Logging & Monitoring
![ETL Logs](screenshots/logging.png)

### PostgreSQL Database Preview
![PostgreSQL Database Records](screenshots/database.png)

---

# Project Structure

```text
airbnb-etl-pipeline/
│
├── processed_data/
│   └── cleaned_data.csv          # Cleaned dataset generated after transformation
│
├── screenshots/
│   ├── terminal.png             # ETL pipeline execution output
│   ├── logging.png              # ETL logging records
│   └── database.png             # PostgreSQL database preview
│
├── extract.py                   # Extract raw Airbnb data
├── transform.py                 # Clean and transform data
├── load.py                      # Load data into PostgreSQL
├── main.py                      # Execute ETL pipeline
│
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
└── .gitignore                   # Ignore unnecessary files
```

---

# How to Run

## Clone Repository

```bash
git clone https://github.com/Shivani61478/airbnb-postgresql-etl.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Create PostgreSQL Database

```sql
CREATE DATABASE airbnb_db;
```

## Configure Database Connection

Update the PostgreSQL credentials inside `load.py`:

```python
engine = create_engine('postgresql+psycopg2://username:password@localhost:5432/airbnb_db')
```

## Run Project

```bash
python main.py
```

---

# Future Improvements

* Apache Airflow Scheduling
* AWS RDS Integration
* Incremental Data Loading

---

# Author

### SHIVANI JAISWAL
#    Data Engineer
