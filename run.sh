#!/bin/bash

# Rice Disease Detection System - Run Script
# Usage: ./run.sh [dev|prod]

echo "=========================================="
echo "🌾 Rice Disease Detection System"
echo "=========================================="

# Detect OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "🍎 Detected macOS"

    # Check if conda is available
    if ! command -v conda &> /dev/null; then
        echo "❌ Conda tidak ditemukan. Silakan install Miniconda:"
        echo "Download dari: https://docs.conda.io/en/latest/miniconda.html"
        exit 1
    fi

    # Check if rice-env exists, create if not
    if ! conda env list | grep -q "rice-env"; then
        echo "📦 Membuat environment rice-env..."
        conda create -n rice-env python=3.10 -y
    fi

    # Activate environment
    echo "🔧 Mengaktifkan environment rice-env..."
    conda activate rice-env

    # Install requirements
    echo "📥 Menginstall dependencies..."
    pip install -r ../requirements.txt

    # Navigate to backend
    cd backend

    # Run the app
    echo "🚀 Menjalankan aplikasi..."
    python app.py

elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    echo "🪟 Detected Windows"

    # Check Python
    if ! command -v python &> /dev/null; then
        echo "❌ Python not found. Please install Python 3.8+"
        exit 1
    fi

    # Check if virtual environment exists
    if [ ! -d "venv" ]; then
        echo "📦 Creating virtual environment..."
        python -m venv venv
    fi

    # Activate virtual environment
    echo "🔧 Activating virtual environment..."
    source venv/Scripts/activate

    # Install requirements
    echo "📥 Installing dependencies..."
    pip install -r requirements.txt

    # Run the app
    echo "🚀 Starting application..."
    python app.py

else
    # Linux/other
    echo "🐧 Detected Linux/other"

    # Check Python
    if ! command -v python3 &> /dev/null; then
        echo "❌ Python3 not found. Please install Python 3.8+"
        exit 1
    fi

    # Check if virtual environment exists
    if [ ! -d "venv" ]; then
        echo "📦 Creating virtual environment..."
        python3 -m venv venv
    fi

    # Activate virtual environment
    echo "🔧 Activating virtual environment..."
    source venv/bin/activate

    # Install requirements
    echo "📥 Installing dependencies..."
    pip install -r requirements.txt

    # Run the app
    echo "🚀 Starting application..."
    python app.py
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt --quiet

# Check .env file
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found!"
    echo "   Creating from .env.example..."
    cp .env.example .env
    echo "   Please edit .env and add your ROBOFLOW_API_KEY"
    echo ""
fi

# Check API key
if grep -q "your_api_key_here" .env 2>/dev/null; then
    echo "⚠️  WARNING: ROBOFLOW_API_KEY not configured!"
    echo "   Please edit .env file and add your API key"
    echo ""
fi

# Run mode
MODE=${1:-dev}

if [ "$MODE" == "prod" ]; then
    echo "🚀 Starting in PRODUCTION mode..."
    cd backend
    gunicorn -w 4 -b 0.0.0.0:5000 app:app
else
    echo "🔧 Starting in DEVELOPMENT mode..."
    cd backend
    python app.py
fi
