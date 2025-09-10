import os
import time
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

# Get port from environment or default to 3000 for consistency with Node.js version
PORT = int(os.environ.get('PORT', 3000))

# Store start time for uptime calculation
start_time = time.time()

@app.route('/')
def hello_world():
    """Basic Hello World endpoint"""
    return jsonify({
        'message': 'Hello World!',
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'version': '1.0.0'
    })

@app.route('/health')
def health_check():
    """Health check endpoint"""
    uptime = time.time() - start_time
    return jsonify({
        'status': 'OK',
        'uptime': uptime,
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    })

@app.route('/hello/<name>')
def personalized_greeting(name):
    """Personalized greeting endpoint"""
    return jsonify({
        'message': f'Hello, {name}!',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    })

if __name__ == '__main__':
    print(f'Hello World API server running on port {PORT}')
    print(f'Visit: http://localhost:{PORT}')
    app.run(host='0.0.0.0', port=PORT, debug=True)