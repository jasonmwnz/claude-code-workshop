const express = require('express');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// Basic Hello World endpoint
app.get('/', (req, res) => {
  res.json({
    message: 'Hello World!',
    timestamp: new Date().toISOString(),
    version: '1.0.0'
  });
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({
    status: 'OK',
    uptime: process.uptime(),
    timestamp: new Date().toISOString()
  });
});

// Personalized greeting endpoint
app.get('/hello/:name', (req, res) => {
  const { name } = req.params;
  res.json({
    message: `Hello, ${name}!`,
    timestamp: new Date().toISOString()
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Hello World API server running on port ${PORT}`);
  console.log(`Visit: http://localhost:${PORT}`);
});