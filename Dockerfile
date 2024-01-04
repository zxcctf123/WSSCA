# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip3 install -r requirements.txt

# Set the entrypoint to run the script with any arguments passed to the docker run command
ENTRYPOINT ["python3", "wssca.py"]
