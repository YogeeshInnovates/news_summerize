# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies in a virtual environment
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Set environment variables, like database credentials or other config
# ENV VAR_NAME=value

# Expose the port the app will run on (defaults to 8000 for Django)
EXPOSE 8000

# Start the Django app
CMD ["/opt/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
