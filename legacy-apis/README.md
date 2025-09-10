# Hello World API

A simple Node.js REST API that returns "Hello World" responses.

## Installation

```bash
npm install
```

## Usage

### Development
```bash
npm run dev
```

### Production
```bash
npm start
```

The API will run on port 3000 by default.

## Endpoints

- `GET /` - Returns basic Hello World message
- `GET /health` - Health check endpoint
- `GET /hello/:name` - Personalized greeting

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