# 🛒 E-Commerce Product Recommendation Engine

A DSA-based E-Commerce Product Recommendation System built using Python, Data Structures & Algorithms, OOP, and Streamlit.

This project simulates how modern e-commerce platforms like Amazon, Flipkart, Myntra, and Netflix recommend products to users based on their interests, interactions, and behavior.

---

# 🚀 Project Overview

Online shopping platforms contain thousands of products. Finding relevant products quickly is difficult for users.

This project solves that problem by analyzing:

* Product ratings
* Search history
* Cart activity
* Product categories
* User preferences

and generates personalized product recommendations.

---

# 🎯 Problem Statement

Build a recommendation engine that:

* Stores products efficiently
* Tracks user interactions
* Calculates product similarity
* Ranks products
* Recommends relevant products
* Displays Top-N recommendations

---

# ✨ Features

## Core Features

* Product Catalog Management
* User Profile Management
* Personalized Recommendations
* Similar Product Suggestions
* Product Search System
* Recommendation Report Generation

## Advanced Features

* Trie-based Search Autocomplete
* Heap-based Top-K Recommendations
* Cosine Similarity Scoring
* Jaccard Similarity Analysis
* Streamlit Dashboard
* Interactive Analytics
* User Activity Tracking

---

# 🧠 DSA Concepts Used

| Concept               | Usage                       |
| --------------------- | --------------------------- |
| HashMap               | Product & User Storage      |
| Array/List            | Product Collections         |
| Set                   | Category Matching           |
| Trie                  | Product Search Autocomplete |
| Heap (Priority Queue) | Top-N Recommendations       |
| Sorting               | Product Ranking             |
| Similarity Algorithms | Recommendation Scoring      |
| OOP                   | Modular Design              |

---

# ⚙️ System Workflow

User Activity
(Purchases, Searches, Ratings, Cart)

↓

User Preference Analysis

↓

Similarity Calculation

↓

Recommendation Score Generation

↓

Heap-Based Ranking

↓

Top-N Product Recommendations

---

# 🏗️ Project Architecture

E-Commerce-Product-Recommendation-Engine/

├── src/

│ ├── **init**.py

│ ├── models.py

│ ├── data_structures.py

│ ├── similarity.py

│ └── engine.py

│

├── data/

│

├── outputs/

│ └── recommendation_report.txt

│

├── images/

│

├── streamlit_app.py

├── main.py

├── requirements.txt

├── README.md

└── .gitignore

---

# 📂 Module Description

## models.py

Contains:

* Product Class
* User Class

Responsible for:

* Product details
* Ratings
* Search history
* Cart activity

---

## data_structures.py

Contains:

* CustomHashMap
* TrieNode
* Trie

Responsible for:

* Fast data storage
* Prefix-based search
* Search autocomplete

---

## similarity.py

Contains:

* Cosine Similarity
* Jaccard Similarity

Responsible for:

* Product similarity calculations
* Recommendation scoring

---

## engine.py

Core recommendation engine.

Responsible for:

* Product registration
* User registration
* Recommendation generation
* Ranking logic
* Similarity calculations

---

# 📊 Recommendation Logic

Recommendation score is calculated using:

1. Product category match
2. User rating history
3. Cart activity
4. Product popularity
5. Similarity score

Products with higher scores are ranked higher.

---

# 🖥️ Streamlit Dashboard Features

* Dashboard Overview
* Product Catalog
* Product Search
* Personalized Recommendations
* Product Similarity Checker
* Analytics Dashboard
* User Profile Viewer
* Recommendation Graphs

---

# 🛠️ Installation

## Clone Repository

git clone https://github.com/arshkaur2405/E-Commerce-Product-Recommendation-Engine.git

cd E-Commerce-Product-Recommendation-Engine

---

## Install Dependencies

pip install -r requirements.txt

---

## Run CLI Version

python main.py

---

## Run Streamlit Dashboard

streamlit run streamlit_app.py

---
# 📈 Sample Output

Top Recommendations for Alice

1. Dell XPS 15

2. Samsung Monitor

3. Sony Headphones

4. Standing Desk

5. Ergonomic Chair

---

# 📄 Report Generation

The system generates:

outputs/recommendation_report.txt

Example:

User: Alice

Dell XPS 15 -> Score 67.99

Samsung Monitor -> Score 52.99

Sony Headphones -> Score 50.45

---

# 🎓 Learning Outcomes

Through this project, I learned:

* Data Structures & Algorithms
* HashMaps
* Trie Data Structure
* Priority Queues (Heap)
* Similarity Algorithms
* Recommendation Systems
* Python OOP
* Streamlit Development
* Software Architecture
* GitHub Project Management

---

# 🔮 Future Enhancements

* Collaborative Filtering
* Content-Based Filtering
* Machine Learning Recommendations
* Real-Time Recommendation Updates
* Product Review Analysis
* Database Integration
* REST API Development
* User Authentication System

---

# 👩‍💻 Author

Arshdeep Kaur

B.Tech Student

 | DSA Enthusiast | AI & Data Analytics Learner

---

# ⭐ If You Like This Project

Please consider giving this repository a star ⭐ and sharing feedback.
