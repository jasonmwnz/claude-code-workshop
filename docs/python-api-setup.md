# Python Hello World API Setup Guide

This guide explains how to set up and run the Python Flask version of the Hello World API.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Navigate to the Python API directory
```bash
cd python-apis
```

### 2. Create a Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Server
```bash
python app.py
```

You should see output similar to:
```
Hello World API server running on port 3000
Visit: http://localhost:3000
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:3000
 * Running on http://[::1]:3000
```

## Environment Variables

The API supports the following environment variables:

- `PORT`: Set the port number (default: 3000)

Example:
```bash
PORT=8080 python app.py
```

## Stopping the Server

- Press `Ctrl+C` to stop the server
- To deactivate the virtual environment: `deactivate`

## Troubleshooting

### Common Issues

1. **Port already in use**: If port 3000 is busy, set a different port:
   ```bash
   PORT=8080 python app.py
   ```

2. **Module not found**: Make sure you've activated the virtual environment and installed dependencies:
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Permission denied**: On some systems, you might need to use `python3` instead of `python`

### Verifying Installation

Test that the API is working by visiting these URLs in your browser:
- http://localhost:3000 - Basic hello world
- http://localhost:3000/health - Health check
- http://localhost:3000/hello/YourName - Personalized greeting