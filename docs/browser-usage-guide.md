# Browser Usage Guide - Hello World APIs

This guide shows you how to interact with both the Node.js and Python Hello World APIs using a web browser.

## Starting the Servers

### Node.js API (Legacy)
```bash
cd legacy-apis
npm install
npm run dev
```
Server runs on: http://localhost:3000

### Python API
```bash
cd python-apis
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Server runs on: http://localhost:3000

**Note**: Only run one server at a time since they both use port 3000 by default.

## Available Endpoints

Both APIs provide identical endpoints with the same response format:

### 1. Basic Hello World
**URL**: http://localhost:3000/

**Response**:
```json
{
  "message": "Hello World!",
  "timestamp": "2024-01-01T00:00:00.000Z", 
  "version": "1.0.0"
}
```

### 2. Health Check
**URL**: http://localhost:3000/health

**Response**:
```json
{
  "status": "OK",
  "uptime": 123.45,
  "timestamp": "2024-01-01T00:00:00.000Z"
}
```

### 3. Personalized Greeting
**URL**: http://localhost:3000/hello/YourName

Replace `YourName` with any name you want. Examples:
- http://localhost:3000/hello/Alice
- http://localhost:3000/hello/Bob
- http://localhost:3000/hello/John%20Doe (for names with spaces)

**Response**:
```json
{
  "message": "Hello, YourName!",
  "timestamp": "2024-01-01T00:00:00.000Z"
}
```

## Using Different Browsers

### Desktop Browsers
- **Chrome/Edge**: Full JSON formatting with syntax highlighting
- **Firefox**: Clean JSON display with collapsible sections
- **Safari**: Basic JSON text display

### Mobile Browsers
All endpoints work on mobile browsers. The JSON responses will display as plain text.

## Browser Extensions

For better JSON viewing experience, consider installing:
- **Chrome**: JSON Viewer, JSONView
- **Firefox**: JSONView (built-in in newer versions)
- **Edge**: JSON Formatter

## Testing with Browser Developer Tools

### Using Browser Console
You can also test the API using JavaScript in the browser console:

```javascript
// Basic fetch request
fetch('http://localhost:3000/')
  .then(response => response.json())
  .then(data => console.log(data));

// Personalized greeting
fetch('http://localhost:3000/hello/Browser')
  .then(response => response.json())
  .then(data => console.log(data));
```

### Network Tab
Use the Network tab in Developer Tools to:
- View request/response headers
- See response times
- Monitor API calls

## Common Browser Issues

### CORS (Cross-Origin Resource Sharing)
If you're making requests from a different domain/port, you might encounter CORS issues. Both APIs currently allow all origins for simplicity.

### Caching
Browsers may cache API responses. To see fresh data:
- Hard refresh: `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac)
- Open Developer Tools and disable cache
- Add a query parameter: `http://localhost:3000/?t=123456`

### URL Encoding
For names with special characters, use URL encoding:
- Spaces: `%20` (e.g., `John%20Doe`)
- Special chars: See URL encoding reference

## Bookmarking Endpoints

You can bookmark these URLs for quick testing:
- [Basic Hello World](http://localhost:3000/)
- [Health Check](http://localhost:3000/health)
- [Hello Test](http://localhost:3000/hello/Test)