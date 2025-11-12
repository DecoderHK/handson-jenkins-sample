#!/bin/bash
# Test runner script for Selenium tests

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Starting Selenium Test Suite...${NC}"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/upgrade dependencies
echo -e "${BLUE}Installing dependencies...${NC}"
pip install --upgrade pip -q
pip install -r requirements.txt -q

# Create directories for reports and screenshots
mkdir -p reports screenshots

# Check if web server is running
if ! curl -s http://localhost:8000/login.html > /dev/null 2>&1; then
    echo -e "${BLUE}Starting web server on port 8000...${NC}"
    python3 -m http.server 8000 > /dev/null 2>&1 &
    SERVER_PID=$!
    sleep 3
    echo "Web server started (PID: $SERVER_PID)"
    echo "Note: Server will continue running. Stop it with: kill $SERVER_PID"
fi

# Run tests
echo -e "${BLUE}Running tests...${NC}"
./venv/bin/python3 -m pytest test_login.py -v --html=reports/report.html --self-contained-html

# Check exit code
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ All tests passed!${NC}"
    echo "View report: reports/report.html"
else
    echo -e "${RED}✗ Some tests failed. Check reports/report.html for details.${NC}"
    exit 1
fi

