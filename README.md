# `ML_project`

<div align="center">

### From data → model → prediction → application.

*A first end-to-end machine learning project, built to understand what happens beyond the notebook.*

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square\&logo=flask\&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square\&logo=scikit-learn\&logoColor=white)
![CatBoost](https://img.shields.io/badge/CatBoost-FFCC00?style=flat-square\&logoColor=black)

</div>

---

## ✦ About

This repository is my first **major machine learning project** — simple in concept, but built with the intention of going beyond a single Jupyter notebook.

The project takes a complete ML workflow and turns it into something that can actually be used:

```text
Raw Data
   ↓
Data Ingestion
   ↓
Data Transformation
   ↓
Model Training
   ↓
Evaluation
   ↓
Prediction Pipeline
   ↓
Flask Web Application
```

Instead of treating machine learning as *"train a model and print an accuracy score"*, the goal here was to understand the entire journey from **data to a working application**.

---

## ◌ What this project does

The application accepts a set of user inputs through a web interface and passes them through a trained machine-learning pipeline to generate a prediction.

Behind the interface, the project separates responsibilities into different components:

* **Data ingestion & processing**
* **Feature transformation**
* **Model training**
* **Model evaluation**
* **Prediction pipeline**
* **Web application layer**

The Flask application connects the user-facing form with the trained model, making the final system interactive rather than purely notebook-based.

---

## ⌁ Project Structure

```text
ML_project/
│
├── artifacts/              # Generated datasets, models & pipeline artifacts
│
├── catboost_info/          # CatBoost training information
│
├── ebextensions/           # Deployment configuration
│
├── notebook/               # Experiments & exploratory work
│
├── src/
│   ├── components/         # Individual ML workflow components
│   │
│   ├── pipeline/            # Training & prediction pipelines
│   │
│   ├── exception.py         # Custom exception handling
│   ├── logger.py            # Logging configuration
│   └── utils.py             # Utility functions
│
├── templates/              # Flask HTML templates
│
├── app.py                  # Flask application
├── application.py          # Application entry point
├── requirements.txt        # Python dependencies
├── setup.py                # Package configuration
└── README.md
```

The repository currently follows a modular structure with separate `components` and `pipeline` layers rather than putting the entire workflow inside one script.

---

## ⚙️ How it works

### 01 — Input

The user provides information through the web interface.

### 02 — Preprocessing

The submitted data is converted into the format expected by the machine-learning pipeline.

### 03 — Prediction

The trained model receives the processed features and produces a prediction.

### 04 — Output

The prediction is returned to the Flask interface and displayed to the user.

In the Flask application, the `/predictdata` route collects the form values, constructs the input dataframe and sends it through `PredictPipeline`.

---

## 🧠 The ML Pipeline

The important idea behind the project is **separation of concerns**.

Rather than coupling everything together:

```text
training.py
    └── does everything
```

the project is structured more like:

```text
                 ┌─────────────────┐
                 │      DATA       │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │   INGESTION     │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ TRANSFORMATION  │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ MODEL TRAINING  │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │    ARTIFACT     │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │    PREDICT      │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │   FLASK APP     │
                 └─────────────────┘
```

This makes the project easier to understand, debug and extend.

---

## 🖥️ Application

The project exposes the model through a **Flask web application**.

The application contains:

* a home page
* an input form
* a prediction endpoint
* integration with the trained prediction pipeline

The Flask layer acts as the bridge between the **machine-learning model** and the **end user**.

> **Machine learning doesn't end when the model is trained.**
>
> The interesting part is making the model usable.

---

## 🛠️ Tech Stack

| Layer              | Technology                          |
| ------------------ | ----------------------------------- |
| Language           | Python                              |
| ML                 | Scikit-learn                        |
| Boosting           | CatBoost                            |
| Backend            | Flask                               |
| Data Processing    | Pandas / NumPy                      |
| Experimentation    | Jupyter Notebook                    |
| Deployment         | AWS Elastic Beanstalk configuration |
| Package Management | `pip` / `setup.py`                  |

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/jackyhitter/ML_project.git
cd ML_project
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

The Flask application will start locally and can then be accessed through the address shown in the terminal.

---

## 📓 Experiments

The `notebook/` directory contains the experimental side of the project.

This is where ideas are explored before becoming part of the more structured pipeline.

The distinction is intentional:

```text
notebook/
    ↓
experiment
    ↓
understand
    ↓
refactor
    ↓
src/
    ↓
application
```

---

## 📈 What I learned

This project was less about building a complicated model and more about understanding what surrounds the model.

### Machine Learning

* Data preprocessing
* Feature transformation
* Model training
* Model evaluation
* Prediction pipelines

### Software Engineering

* Modular project structure
* Reusable components
* Logging
* Exception handling
* Package configuration

### Deployment

* Flask application development
* Application entry points
* Deployment configuration
* Turning an ML workflow into a usable service

---

## 🔭 What's next?

This project is intentionally a starting point.

Possible improvements include:

* [ ] Better frontend UI
* [ ] Model comparison dashboard
* [ ] More detailed evaluation metrics
* [ ] Automated testing
* [ ] CI/CD pipeline
* [ ] Containerization with Docker
* [ ] Improved model monitoring
* [ ] Cloud deployment
* [ ] API documentation
* [ ] Better experiment tracking

---

## ✦ Why this repository exists

> *The first version doesn't have to be perfect.*
>
> *It just has to exist.*

This project is a record of the transition from **learning machine learning** to **building with machine learning**.

It started as a simple project.

The point is to keep making it less simple.

---

<div align="center">

### Built with curiosity, Python, and a lot of debugging.

<br>

**[View the repository](https://github.com/jackyhitter/ML_project)**

</div>
