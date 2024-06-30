# Using the official Python image from the Docker Hub
FROM python:3.9

# Setting the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    & pip install -r resources/requirements.txt

# Install Playwright browsers
RUN playwright install \
    & playwright install-deps

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the bash script to execute tests
ENTRYPOINT ["./run_tests.sh"]