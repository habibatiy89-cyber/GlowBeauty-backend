Getting Started

# Clone repo
git clone https://github.com/yourusername/glowbeauty-backend.git
cd glowbeauty-backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Optional: seed sample data
python seed.py
Running the Server
uvicorn app.main:app --reload


Visit: http://127.0.0.1:8000

API Endpoints

GET /categories – List categories

GET /categories/{id}/products – Products in a category

GET /products – List all products

GET /products/{id} – Product details

POST /orders – Create an order

Project Structure
backend/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
├── seed.py
├── init_db.py
├── requirements.txt
└── README.md

Contributing

Fork the repo

Create a branch: git checkout -b feature-name

Commit changes: git commit -m "Add feature"

Push branch: git push origin feature-name

Open a Pull Request