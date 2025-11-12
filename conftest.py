"""
Pytest configuration and shared fixtures.
"""
import pytest
import os
import socket
import urllib.request
import urllib.error
from selenium import webdriver


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application."""
    return os.getenv("BASE_URL", "http://localhost:8000")


@pytest.fixture(scope="session")
def headless():
    """Whether to run browser in headless mode."""
    return os.getenv("HEADLESS", "false").lower() == "true"


@pytest.fixture(scope="session", autouse=True)
def check_web_server(base_url):
    """Check if web server is running before tests start."""
    try:
        # Parse URL
        if base_url.startswith("http://"):
            host_port = base_url[7:]  # Remove 'http://'
        elif base_url.startswith("https://"):
            host_port = base_url[8:]  # Remove 'https://'
        else:
            host_port = base_url
        
        if ":" in host_port:
            host, port = host_port.split(":")
            port = int(port)
        else:
            host = host_port
            port = 8000
        
        # Try to connect to the server
        try:
            response = urllib.request.urlopen(f"{base_url}/login.html", timeout=2)
            response.read()
            print(f"✓ Web server is running at {base_url}")
        except (urllib.error.URLError, socket.timeout, ConnectionRefusedError):
            pytest.exit(
                f"\n❌ ERROR: Web server is not running at {base_url}\n"
                f"Please start the web server first:\n"
                f"  python3 -m http.server 8000\n"
                f"Or use the run_tests.sh script which starts it automatically.\n",
                returncode=1
            )
    except Exception as e:
        pytest.exit(
            f"\n❌ ERROR: Could not check web server: {e}\n"
            f"Please ensure the web server is running at {base_url}\n",
            returncode=1
        )

