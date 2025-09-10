# Testing Guide - Hello World APIs

This guide explains how to run tests for the Hello World APIs and understand the test results.

## Test Structure

Currently, we have comprehensive tests for the Python API located in:
```
tests/
└── test_python_api.py
```

## Prerequisites

### For Python API Tests
```bash
cd python-apis
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running Tests

### Python API Tests

#### Option 1: Run from project root
```bash
cd tests
python -m pytest test_python_api.py -v
```

#### Option 2: Run specific test
```bash
cd tests
python -m pytest test_python_api.py::test_hello_world_endpoint -v
```

#### Option 3: Run with coverage
```bash
cd tests
python -m pytest test_python_api.py --cov=../python-apis --cov-report=html -v
```

### Expected Output
```
============================= test session starts ==============================
collected 9 items

test_python_api.py::test_hello_world_endpoint PASSED           [ 11%]
test_python_api.py::test_health_endpoint PASSED                [ 22%]
test_python_api.py::test_personalized_greeting_endpoint PASSED [ 33%]
test_python_api.py::test_personalized_greeting_with_special_characters PASSED [ 44%]
test_python_api.py::test_content_type_is_json PASSED           [ 55%]
test_python_api.py::test_nonexistent_endpoint_returns_404 PASSED [ 66%]
test_python_api.py::test_timestamp_consistency PASSED          [ 77%]
test_python_api.py::test_uptime_increases_over_time PASSED     [ 88%]

============================== 8 passed in 0.12s ==============================
```

## Test Coverage

The Python API tests cover:

### Functional Tests
- ✅ Basic Hello World endpoint (`/`)
- ✅ Health check endpoint (`/health`)
- ✅ Personalized greeting endpoint (`/hello/<name>`)
- ✅ URL encoding handling
- ✅ 404 error handling

### Response Format Tests
- ✅ JSON content type validation
- ✅ Required fields presence
- ✅ Data types validation
- ✅ ISO 8601 timestamp format

### Behavioral Tests
- ✅ Timestamp consistency and recency
- ✅ Uptime progression over time
- ✅ Special character handling

## Test Descriptions

### `test_hello_world_endpoint`
Validates the basic `/` endpoint returns correct message, version, and timestamp format.

### `test_health_endpoint`
Checks that `/health` returns status "OK", numeric uptime, and valid timestamp.

### `test_personalized_greeting_endpoint`
Tests `/hello/<name>` with various name inputs to ensure proper message formatting.

### `test_personalized_greeting_with_special_characters`
Verifies URL encoding works correctly (e.g., "John%20Doe" becomes "John Doe").

### `test_content_type_is_json`
Ensures all endpoints return proper JSON content type headers.

### `test_nonexistent_endpoint_returns_404`
Confirms that invalid endpoints return appropriate 404 status codes.

### `test_timestamp_consistency`
Validates that timestamps are recent and within expected time bounds.

### `test_uptime_increases_over_time`
Checks that the uptime value increases between subsequent requests.

## Running Individual Test Categories

### Basic Functionality
```bash
python -m pytest test_python_api.py -k "hello_world or health or greeting" -v
```

### Error Handling
```bash
python -m pytest test_python_api.py -k "404 or nonexistent" -v
```

### Data Validation
```bash
python -m pytest test_python_api.py -k "timestamp or uptime or content_type" -v
```

## Adding Tests for Node.js API

To add tests for the Node.js API, create `tests/test_nodejs_api.py`:

```python
# Example structure for Node.js tests
import requests
import pytest

BASE_URL = "http://localhost:3000"

def test_nodejs_hello_world():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    # ... additional assertions
```

**Note**: Node.js API tests would require the server to be running separately.

## Continuous Integration

For CI/CD pipelines, use:

```bash
# Install dependencies
pip install -r python-apis/requirements.txt

# Run tests with JUnit XML output
python -m pytest tests/ --junitxml=test-results.xml

# Run tests with coverage
python -m pytest tests/ --cov=python-apis --cov-report=xml
```

## Troubleshooting Tests

### Import Errors
Make sure you're running tests from the correct directory and the Python path includes the API modules.

### Port Conflicts
If port 3000 is in use, the Flask test client creates an isolated instance, so port conflicts shouldn't affect tests.

### Timing Issues
Some tests involve timing (uptime progression). If tests fail intermittently, consider increasing sleep durations in timing-sensitive tests.

### Missing Dependencies
Install test dependencies:
```bash
pip install pytest pytest-flask requests
```