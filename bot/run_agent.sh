#!/bin/bash

# AI Tech Stack Advisor Runner Script
# Makes it easy to run the agent from anywhere

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "=========================================="
echo "  🤖 AI Tech Stack Advisor"
echo "=========================================="
echo -e "${NC}"

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
python3 -c "import json, os, datetime" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Required Python modules not found."
    echo "Installing dependencies..."
    pip3 install -r "${SCRIPT_DIR}/../requirements.txt"
fi

echo -e "${GREEN}✅ Dependencies ready${NC}\n"

# Run the agent
cd "$SCRIPT_DIR"
python3 tech_stack_agent.py

echo -e "\n${GREEN}✅ Agent completed!${NC}\n"

