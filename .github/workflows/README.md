# Automated Testing Project

## Overview

This project contains automated tests for counting posts on the Ocula resources page and API tests for the
OpenWeatherMap API.

## Setup

### Prerequisites

- Docker
- GitHub Actions

### Running Tests Locally

1. Build and run the Docker image:

```bash
docker build -t naishwaryaghandhi/ocula_e2e_tests:latest .
docker run --rm naishwaryaghandhi/ocula_e2e_tests:latest
```

### Conclusion

By dockerizing the project and setting up GitHub Actions, you ensure a consistent environment for running your tests and
automate the process of running tests on every code change. This enhances the reliability and maintainability of the
project.
