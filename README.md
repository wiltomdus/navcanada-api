# Python API for Upper Winds Data

This project is a FastAPI application that exposes data from a local MongoDB database related to upper winds stations. It provides endpoints to retrieve ICAO codes of stations, specific station data, and all upper winds collections from all databases.

## Project Structure

```
navcanada-api
├── src
│   ├── main.py                # Entry point of the application
│   ├── controllers            # Contains API endpoint handlers
│   │   └── upper_winds_controller.py
│   ├── models                 # Defines data models
│   │   └── upper_winds_model.py
│   ├── services               # Contains database interaction logic
│   │   └── upper_winds_service.py
│   └── config.py             # Configuration settings
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd python-api
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure MongoDB connection:**
   Update the `src/config.py` file with your MongoDB connection details.

5. **Run the application:**
   ```
   uvicorn src.main:app --reload
   ```

## API Endpoints

- **GET /upper-winds/stations**
  - Returns all stations ICAO codes that are in the database.

- **GET /upper-winds/station/{ICAO-code}**
  - Returns the data in the upper_winds collection for the specified ICAO code.

- **GET /upper-winds**
  - Returns all the upper_winds collections from all databases.

## License

This project is licensed under the MIT License. See the LICENSE file for details.