# Stock CRUD API 📈

A high-performance FastAPI backend application for managing stock data, built with FastAPI and JSON file storage. This API supports CRUD operations, pagination, filtering by trade code, and fetching distinct trade codes. It's designed to integrate seamlessly with a frontend like React with CORS enabled. 🚀

# Table of Contents 📋

- Features
- Tech Stack
- Installation
- Data Storage
- Running the App
- API Endpoints
- Example Requests
- Requirements
- Gitignore
- Contributing
- License

# Features ✨

- CRUD Operations: Create, read, update, and delete stock records with ease. 🛠️
- Pagination: Efficiently handle large datasets with paginated responses. 📄
- Trade Code Filtering: Filter stock data by trade_code for targeted queries. 🔍
- Distinct Trade Codes: Retrieve unique trade codes for streamlined frontend integration. 📊
- CORS Support: Seamlessly integrates with React or other frontend frameworks. 🌐
- JSON File Storage: Simple and portable data storage using a JSON file. 🗄️

# Tech Stack 🛠️

- Backend: FastAPI – High-performance, asynchronous API framework. ⚡
- Data Storage: JSON – Simple file-based data storage. 📁
- Data Validation: Pydantic – Data validation and settings management. 📊
- Server: Uvicorn – ASGI server for running FastAPI. 🚀

# Installation ⚙️

### Clone the Repository:

```bash
git clone https://github.com/yourusername/stock-crud-api.git
cd stock-crud-api
```

### Create a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

# Data Storage 🗄️

This application uses a JSON file (`stock_market_data.json`) for data storage instead of a traditional database. The file is automatically created if it doesn't exist.

Key benefits of this approach:

1. Simplicity: No database setup required
2. Portability: Easy to move or share the entire dataset
3. Transparency: Data structure is human-readable

The application handles all CRUD operations by reading from and writing to this JSON file.

# Running the App 🚀

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload
```

Access the API at:

- Base URL: https://stock-backend-07c7.onrender.com
- Swagger UI: http://127.0.0.1:8000/docs 📜
- ReDoc: http://127.0.0.1:8000/redoc 📄

# API Endpoints 📡

| Method | Endpoint            | Description                                | Parameters                                      |
| ------ | ------------------- | ------------------------------------------ | ----------------------------------------------- |
| POST   | /stocks             | Create a new stock record                  | Stock data (JSON)                               |
| GET    | /stocks             | Retrieve stocks (with pagination & filter) | skip (opt), limit (default=10), trade_code (opt) |
| GET    | /stocks/trade-codes | Retrieve distinct trade codes              | None                                            |
| GET    | /stocks/{stock_id}  | Retrieve a stock by ID                     | stock_id (UUID)                                 |
| PUT    | /stocks/{stock_id}  | Update a stock by ID                       | stock_id (UUID), Stock data (JSON)              |
| DELETE | /stocks/{stock_id}  | Delete a stock by ID                       | stock_id (UUID)                                 |

### Stock Schema Example:

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "date": "2025-09-14",
  "trade_code": "AAPL",
  "high": 180.5,
  "low": 178.2,
  "open": 179.0,
  "close": 180.0,
  "volume": 50000
}
```

# Example Requests 🌐

### 1. Create a Stock
```bash
curl -X POST "https://stock-backend-07c7.onrender.com/stocks" \
-H "Content-Type: application/json" \
-d '{"id":"123e4567-e89b-12d3-a456-426614174000","date":"2025-09-14","trade_code":"AAPL","high":180.5,"low":178.2,"open":179.0,"close":180.0,"volume":50000}'
```

Response:

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "date": "2025-09-14",
  "trade_code": "AAPL",
  "high": 180.5,
  "low": 178.2,
  "open": 179.0,
  "close": 180.0,
  "volume": 50000
}
```

### 2. Get Stocks (with Pagination & Filter)
```bash
curl "https://stock-backend-07c7.onrender.com/stocks?skip=0&limit=10&trade_code=AAPL"
```

### 3. Get Distinct Trade Codes

```bash
curl "https://stock-backend-07c7.onrender.com/stocks/trade-codes"
```

### 4. Get Stock by ID
```bash
curl "https://stock-backend-07c7.onrender.com/stocks/123e4567-e89b-12d3-a456-426614174000"
```

### 5. Update Stock
```bash
curl -X PUT "https://stock-backend-07c7.onrender.com/stocks/123e4567-e89b-12d3-a456-426614174000" \
-H "Content-Type: application/json" \
-d '{"id":"123e4567-e89b-12d3-a456-426614174000","date":"2025-09-14","trade_code":"AAPL","high":181,"low":179,"open":179.5,"close":180.5,"volume":55000}'
```

### 6. Delete Stock
```bash
curl -X DELETE "https://stock-backend-07c7.onrender.com/stocks/123e4567-e89b-12d3-a456-426614174000"
```

Response:

```json
{ "ok": true }
```

# Requirements 📦

`requirements.txt`

```
fastapi
uvicorn
pydantic
```

Install using:

```bash
pip install -r requirements.txt
```

# Gitignore 🚫

```
venv/
__pycache__/
*.pyc
.DS_Store
```

# License 📜

This project is licensed under the MIT License. See the LICENSE file for details.

Happy coding! 🎉
