# Hello World API (Python)

A Python Flask version of the Hello World REST API, migrated from the Node.js version in `legacy-apis`.

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Development
```bash
python app.py
```

The API will run on port 3000 by default (same as Node.js version).

## Endpoints

- `GET /` - Returns basic Hello World message
- `GET /health` - Health check endpoint  
- `GET /hello/<name>` - Personalized greeting

## Example Responses

### GET /
```json
{
  "message": "Hello World!",
  "timestamp": "2024-01-01T00:00:00.000Z",
  "version": "1.0.0"
}
```

### GET /health
```json
{
  "status": "OK",
  "uptime": 123.45,
  "timestamp": "2024-01-01T00:00:00.000Z"
}
```

### GET /hello/John
```json
{
  "message": "Hello, John!",
  "timestamp": "2024-01-01T00:00:00.000Z"
}
```

## Testing

Run tests from the project root:
```bash
cd tests
python -m pytest test_python_api.py -v
```