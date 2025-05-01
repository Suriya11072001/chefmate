# 🍽️ ChefMate — Restaurant Clustering & Cooking Guide Application

ChefMate is an end-to-end machine learning + interactive chatbot app that combines **restaurant clustering**, **filter-based recommendations**, and a **step-by-step cooking assistant** — designed for food lovers and home chefs alike.

---

## 🔍 Problem Statement

The problem revolves around enabling users to discover restaurants that match their preferences (e.g., cuisine, location, cost) while also assisting them in preparing meals through a chatbot. The project tackles the challenges of structuring unorganized data, efficient data preprocessing, and creating a user-friendly application with cloud support.

---

## 📦 Project Overview

| Component              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 📊 Restaurant Clustering | Groups restaurants using unsupervised learning (KMeans)                    |
| 🧑‍🍳 Cooking Assistant     | An NLP-style chatbot that guides users step-by-step through recipes        |
| 🌐 Streamlit App        | A responsive 2-page app for filtering restaurants + chatting with ChefBot  |
| ☁️ AWS Deployment       | S3 for storage, RDS for structured SQL data, EC2 for deployment             |

---

## 🛠️ Tech Stack

- **Python**: Core logic, clustering, and data wrangling
- **Scikit-learn**: KMeans clustering
- **Streamlit**: Interactive frontend
- **AWS S3 / RDS / EC2**: Cloud storage, SQL, and deployment
- **SQLAlchemy**: Database handling
- **Pickle**: Model persistence
- **VS Code**: Dev environment

---

## 🚀 Features

### 🔍 Restaurant Clustering & Filtering
- Group restaurants by:
  - Cuisine
  - Location
  - Rating
  - Price range
- Dynamically filter and explore results via dropdowns and sliders

### 🤖 Chatbot Cooking Guide
- Step-by-step guidance through recipes
- Responds to prompts like "start cooking", "what’s next?", "repeat step"
- Makes home cooking easier and interactive
