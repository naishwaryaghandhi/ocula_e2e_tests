# Automated Testing Project

## Overview

This project contains automated tests for counting posts on the Ocula resources page and API tests for the
OpenWeatherMap API.

## Setup

### Prerequisites

- Docker
- GitHub Actions

### Running Tests

1. Run from GitHub Actions
    click Actions tab
    Click on the workflow name Docker Build, Test, and Push
    Click on Run workflow in the right hand side
    Check logs from Run container

3. Running Tests Locally- Build and run the Docker image:

```bash
docker build -t naishwaryaghandhi/ocula_tests:latest .
docker run --rm naishwaryaghandhi/ocula_tests:latest
```

### Conclusion

By dockerizing the project and setting up GitHub Actions, you ensure a consistent environment for running your tests and
automate the process of running tests on every code change. This enhances the reliability and maintainability of the
project.
