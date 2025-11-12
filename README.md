# Selenium Automated Testing Demo

A comprehensive demonstration project for automated web testing using Selenium WebDriver and pytest. This project showcases modern testing practices including multiple test scenarios, test reporting, and CI/CD integration.

## Features

- **Modern UI**: Beautiful, responsive login and form pages with gradient styling
- **Comprehensive Test Suite**: Multiple test scenarios covering positive, negative, and edge cases
- **Pytest Framework**: Professional test organization with fixtures and reporting
- **Screenshot Capture**: Automatic screenshots on test failures
- **HTML Test Reports**: Detailed test execution reports
- **CI/CD Ready**: Jenkins pipeline configuration included

## Project Structure

```
.
├── login.html          # Login page with modern styling
├── form.html           # Form submission page
├── simple_test.py     # Original simple test script (legacy)
├── test_all.py      # Comprehensive pytest test suite
├── conftest.py        # Pytest configuration and shared fixtures
├── pytest.ini         # Pytest settings
├── requirements.txt   # Python dependencies
├── Jenkinsfile        # Jenkins pipeline for Windows
├── Jenkinsfile_unix   # Jenkins pipeline for Unix/Linux
└── README.md          # This file
```

## Prerequisites

- Python 3.8 or higher
- Chrome browser installed
- ChromeDriver (automatically managed by Selenium 4.x)

## Setup

1. **Create and activate virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Start the web server** (in a separate terminal):
```bash
python3 -m http.server 8000
```

## Running Tests

### Run all tests with pytest:
```bash
./venv/bin/python3 -m pytest test_all.py -v
```

### Run specific test class:
```bash
./venv/bin/python3 -m pytest test_all.py::TestLogin -v
```

### Run specific test:
```bash
./venv/bin/python3 -m pytest test_all.py::TestLogin::test_successful_login -v
```

### Run with HTML report:
```bash
./venv/bin/python3 -m pytest test_all.py --html=reports/report.html --self-contained-html
```

### Run in headless mode (for CI/CD):
```bash
HEADLESS=true ./venv/bin/python3 -m pytest test_all.py -v
```

### Run original simple test script:
```bash
./venv/bin/python3 simple_test.py
```

## Test Scenarios

### Login Tests (`TestLogin`)
- ✅ Successful login with valid credentials
- ❌ Login with invalid username
- ❌ Login with invalid password
- ❌ Login with empty fields
- ❌ Login with whitespace-only input

### Form Submission Tests (`TestFormSubmission`)
- ✅ Successful form submission with all fields
- ✅ Form submission with only required fields (message optional)
- ❌ Form submission without name
- ❌ Form submission without email
- ❌ Form submission with invalid email format

### End-to-End Tests (`TestEndToEnd`)
- ✅ Complete user flow: login → fill form → submit

## Test Reports and Screenshots

- **HTML Reports**: Generated in `reports/report.html` after test execution
- **Screenshots**: Automatically captured on test failures in `screenshots/` directory

## CI/CD Integration

### Jenkins Pipeline

The project includes Jenkins pipeline configurations:
- `Jenkinsfile`: Windows-specific pipeline
- `Jenkinsfile_unix`: Unix/Linux pipeline

The pipeline includes:
1. Code checkout
2. Virtual environment setup
3. Web server startup
4. Dependency installation
5. Test execution
6. Cleanup

### Running in CI/CD

Set environment variables:
- `HEADLESS=true`: Run browser in headless mode
- `BASE_URL`: Override default URL (default: http://localhost:8000)

## Credentials

**Login Credentials:**
- Username: `user`
- Password: `pass`

## Technologies Used

- **Selenium WebDriver 4.24.0**: Browser automation
- **pytest 8.3.4**: Testing framework
- **pytest-html 4.1.1**: HTML test reports
- **pytest-xdist 3.6.1**: Parallel test execution (optional)

## Best Practices Demonstrated

1. **Page Object Model Ready**: Test structure allows easy migration to POM
2. **Fixture Management**: Proper setup/teardown with pytest fixtures
3. **Error Handling**: Comprehensive error handling and assertions
4. **Test Organization**: Logical grouping of related tests
5. **Reporting**: Detailed test reports with screenshots
6. **CI/CD Integration**: Ready for continuous integration

## Troubleshooting

### ChromeDriver Issues
If you encounter ChromeDriver issues, ensure Chrome browser is up to date. Selenium 4.x automatically manages ChromeDriver.

### Port Already in Use
If port 8000 is already in use, either:
- Stop the other service using port 8000
- Change the port in the test files and start server on different port

### Headless Mode
For headless execution (CI/CD), set `HEADLESS=true` environment variable.

## Contributing

Feel free to extend this demo with:
- Page Object Model implementation
- Data-driven testing
- API testing integration
- Performance testing
- Cross-browser testing

## License

This is a demonstration project for educational purposes.

