#!/bin/bash
set -e

echo "🚀 Starting application setup..."

# Initialize database
echo "📊 Initializing database..."
python init_db.py

# Initialize knowledge base
echo "📚 Initializing knowledge base..."
python init_kb.py

echo "✅ Setup complete! Starting application..."

# Start the application
exec uvicorn main:app --host 0.0.0.0 --port 8000
