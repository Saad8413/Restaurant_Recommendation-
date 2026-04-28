# 🍽️ Aura Gastronomica | Content-Based Recommender

![Python](https://img.shields.io/badge/Python-3.x-171717?style=flat-square\&logo=python\&logoColor=38B2AC)
![Flask](https://img.shields.io/badge/Flask-Backend-171717?style=flat-square\&logo=flask\&logoColor=38B2AC)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-ML-171717?style=flat-square\&logo=scikit-learn\&logoColor=38B2AC)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-UI/UX-171717?style=flat-square\&logo=tailwind-css\&logoColor=38B2AC)

**Aura Gastronomica** is an intelligent, web-based recommendation engine designed to curate personalized dining experiences in Bangalore.

Moving beyond generic “top-10” lists, this project leverages **Natural Language Processing (NLP)** to analyze unstructured customer reviews along with key metrics such as cuisine, cost, and ratings.

By processing these features through a **TF-IDF vectorization model**, the system delivers highly accurate, taste-based restaurant recommendations instantly.

---

## 🚀 Key Features

| Feature                    | Description                                                                                                |
| :------------------------- | :--------------------------------------------------------------------------------------------------------- |
| **Real-Time Engine**       | Optimized Flask backend computes cosine similarity across thousands of records in milliseconds.            |
| **Smart Auto-Complete**    | AJAX-powered search bar with real-time suggestions and full keyboard navigation (Up/Down/Enter).           |
| **Advanced NLP Model**     | Uses Scikit-Learn’s `TfidfVectorizer` with `NLTK` for stop-word removal and better semantic understanding. |
| **Premium UI/UX**          | Modern Light Mode interface built using **Tailwind CSS** with clean dashboards and smooth interactions.    |
| **Pre-Trained Efficiency** | Model matrix stored in `.pkl` format for instant response without recomputation.                           |

---

## 📂 Project Structure

```text
Restaurant_Recommendation_System/
│
├── Dataset/
│   └── Dataset.txt
│
├── Document/
│   └── RESTAURANT_RECOMMENDATION_SYSTEM.docx
│
├── Model/
│   └── Restaurant_Recommendation_System.ipynb
│
├── Flask/
│   ├── templates/
│   │   ├── index.html
│   │   ├── web.html
│   │   └── result.html
│   │
│   ├── app1.py
│   ├── Restaurant_Recommendation_System.ipynb
│   │
│   │   
│   ├── zomato.csv
│   ├── restaurant.pkl
│   └── restaurant1.csv
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites

Make sure Python is installed. Install dependencies using:

```bash
pip install -r requirements.txt
```

---

### 2. Train the Model (Jupyter Notebook)

Before running the web app, you must prepare the dataset and model:

* Navigate to the `Flask/` directory
* Place `zomato.csv` inside the folder
* Open `Restaurant_Recommendation_System.ipynb`
* Run all cells (EDA + model training)
* Ensure these files are generated:

  * `restaurant.pkl`
  * `restaurant1.csv`

---

### 3. Run the Application

```bash
python app1.py
```

---

### 4. Access the Web App

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🧠 Architectural Workflow

1. **Dynamic Input**
   User types → AJAX fetches matching restaurant names in real-time.

2. **Vectorization & Inference**
   Pre-trained TF-IDF matrix (`restaurant.pkl`) is loaded.

3. **Similarity Calculation**
   Cosine similarity is used to find top 10 similar restaurants.

4. **Results Display**
   Data is rendered into a clean Tailwind-styled dashboard.

---

## 📝 License & Credits

This project is developed for educational purposes as part of the **SmartInternz Applied Data Science Internship Program**.

**Developed by Saad Shaikh**
