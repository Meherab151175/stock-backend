Stock CRUD API 📈
A high-performance FastAPI backend application for managing stock data, built with SQLModel and PostgreSQL. This API supports CRUD operations, pagination, filtering by trade code, and fetching distinct trade codes. It’s designed to integrate seamlessly with a frontend like React with CORS enabled. 🚀

Table of Contents 📋

Features
Tech Stack
Installation
Environment Variables
Database Setup
Running the App
API Endpoints
Example Requests
Requirements
Gitignore
Contributing
License

Features ✨

CRUD Operations: Create, read, update, and delete stock records with ease. 🛠️
Pagination: Efficiently handle large datasets with paginated responses. 📄
Trade Code Filtering: Filter stock data by trade_code for targeted queries. 🔍
Distinct Trade Codes: Retrieve unique trade codes for streamlined frontend integration. 📊
CORS Support: Seamlessly integrates with React or other frontend frameworks. 🌐
PostgreSQL & SQLModel: Robust database management with a modern ORM. 🗄️

Tech Stack 🛠️

Backend: FastAPI – High-performance, asynchronous API framework. ⚡
Database: PostgreSQL – Scalable and reliable relational database. 🐘
ORM: SQLModel – Combines SQLAlchemy and Pydantic for robust data handling. 📊
Environment Variables: python-dotenv – Manage configuration securely. 🔑
Server: Uvicorn – ASGI server for running FastAPI. 🚀

Installation ⚙️

Clone the Repository:
git clone https://github.com/yourusername/stock-crud-api.git
cd stock-crud-api

Create a Virtual Environment:
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows

Install Dependencies:
pip install -r requirements.txt

Environment Variables 🔑

Create a .env file in the project root:
touch .env

Add the PostgreSQL database URL (replace with your credentials):
DATABASE_URL=postgresql://username:password@host:port/dbname

Optionally, copy the example configuration:
cp .env.example .env

.env.example:
DATABASE_URL=postgresql://username:password@host:port/dbname

Database Setup 🗄️

Ensure PostgreSQL is installed and running.
Create a database for the application.
The API automatically creates tables on startup using:SQLModel.metadata.create_all(engine)

Note: Ensure your PostgreSQL credentials in .env are correct to avoid connection errors.

Running the App 🚀

Start the FastAPI server with Uvicorn:
uvicorn main:app --reload

Access the API at:

Base URL: http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs 📜
ReDoc: http://127.0.0.1:8000/redoc 📄

API Endpoints 📡

Method
Endpoint
Description
Parameters

POST
/stocks
Create a new stock record
Stock data (JSON)

GET
/stocks
Retrieve stocks (with pagination & filter)
last_id (opt), limit (default=100), trade_code (opt)

GET
/stocks/trade-codes
Retrieve distinct trade codes
None

GET
/stocks/{stock_id}
Retrieve a stock by ID
stock_id

PUT
/stocks/{stock_id}
Update a stock by ID
stock_id, Stock data (JSON)

DELETE
/stocks/{stock_id}
Delete a stock by ID
stock_id

Stock Schema
{
"date": "2025-09-14",
"trade_code": "AAPL",
"high": 180.5,
"low": 178.2,
"open": 179.0,
"close": 180.0,
"volume": 50000
}

Example Requests 🌐
Below are example curl commands for interacting with the API:

1. Create a Stock
   curl -X POST "http://127.0.0.1:8000/stocks" \
   -H "Content-Type: application/json" \
   -d '{"date":"2025-09-14","trade_code":"AAPL","high":180.5,"low":178.2,"open":179.0,"close":180.0,"volume":50000}'

Response:
{
"id": 1,
"date": "2025-09-14",
"trade_code": "AAPL",
"high": 180.5,
"low": 178.2,
"open": 179.0,
"close": 180.0,
"volume": 50000
}

2. Get Stocks (with Pagination & Filter)
   curl "http://127.0.0.1:8000/stocks?last_id=0&limit=50&trade_code=AAPL"

Response:
[
{
"id": 1,
"date": "2025-09-14",
"trade_code": "AAPL",
"high": 180.5,
"low": 178.2,
"open": 179.0,
"close": 180.0,
"volume": 50000
}
]

3. Get Distinct Trade Codes
   curl "http://127.0.0.1:8000/stocks/trade-codes"

Response:
["AAPL", "MSFT", "GOOG"]

4. Get Stock by ID
   curl "http://127.0.0.1:8000/stocks/1"

Response:
{
"id": 1,
"date": "2025-09-14",
"trade_code": "AAPL",
"high": 180.5,
"low": 178.2,
"open": 179.0,
"close": 180.0,
"volume": 50000
}

5. Update Stock
   curl -X PUT "http://127.0.0.1:8000/stocks/1" \
   -H "Content-Type: application/json" \
   -d '{"date":"2025-09-14","trade_code":"AAPL","high":181,"low":179,"open":179.5,"close":180.5,"volume":55000}'

Response:
{
"id": 1,
"date": "2025-09-14",
"trade_code": "AAPL",
"high": 181.0,
"low": 179.0,
"open": 179.5,
"close": 180.5,
"volume": 55000
}

6. Delete Stock
   curl -X DELETE "http://127.0.0.1:8000/stocks/1"

Response:
{"ok": true}

Requirements 📦
Create a requirements.txt file with the following dependencies:
fastapi
uvicorn
sqlmodel
psycopg2-binary
python-dotenv

Install them using:
pip install -r requirements.txt

Gitignore 🚫
The .gitignore file ensures unnecessary files are excluded from version control:
venv/
**pycache**/
_.pyc
.env
_.sqlite
.DS_Store

Contributing 🤝
Contributions are welcome! To contribute:

Fork the repository. 🍴
Create a feature branch (git checkout -b feature/your-feature). 🌿
Commit your changes (git commit -m "Add your feature"). 💾
Push to the branch (git push origin feature/your-feature). 🚀
Open a Pull Request. 📬

License 📜
This project is licensed under the MIT License. See the LICENSE file for details.

Happy coding! 🎉
