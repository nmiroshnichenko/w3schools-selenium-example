# w3schools-selenium-example

This is an example of Web UI tests using Selenium and pytest.

## How to run tests

### How to run tests locally
```bash
# Create a virtual environment
python3 -m venv venv

# Install runtime dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# If you will contribute, set up git pre-commit hook for linters
pre-commit install

# Run tests
pytest
```

### How to run tests in Docker
```bash
# Build docker image
docker build \
  --pull \
  --compress \
  --tag 'w3schools-selenium-example:latest' \
  .

# Run container with mounting the current directory
docker run \
  --name 'w3schools-selenium-example' \
  --volume "$(pwd):/tests" \
  --rm \
  'w3schools-selenium-example:latest'
```
