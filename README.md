# Bundesliga Players Data Pipeline

## Overview
This project processes Bundesliga player data using **Pandas**, stores it in **MongoDB**, and interacts with it using both **PyMongo** and **MongoEngine (ODM)**.

It demonstrates a complete data pipeline from raw dataset → cleaning → database → querying.

---

## Technologies Used
- Python
- Pandas
- MongoDB
- PyMongo
- MongoEngine (ODM)
- Docker

---

## Dataset
The dataset contains Bundesliga player information such as:
- Name
- Age
- Height
- Nationality
- Market Value (price, max_price)
- Position
- Club

> Note: Data was cleaned and transformed before being stored in MongoDB.

---

## Features
- Data cleaning and preprocessing with Pandas
- Conversion of dataset into structured records
- Batch insertion into MongoDB
- CRUD operations using PyMongo
- ODM-based queries using MongoEngine
- Filtering, updating, and deleting records

---

## Project Structure
bundesliga-players-mongodb/
│
├── data/
├── notebooks/
│ └── db_bundesliga_players.ipynb
│
├── src/
│ ├── db.py
│ ├── cleaning.py
│ ├── models.py
│ ├── seed.py
│ └── queries.py
│
├── docker-compose.yml
├── requirements.txt
└── README.md

---

## How to Run

### 1. Start MongoDB (Docker)
```bash
docker compose up -d
pip install -r requirements.txt
python -m src.seed
python -m src.queries
