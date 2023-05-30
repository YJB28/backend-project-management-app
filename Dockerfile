# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Upgrade pip
RUN python -m pip install --no-cache-dir --upgrade pip

# Install virtualenv
RUN python -m pip install --no-cache-dir virtualenv

# Create and activate a virtual environment
RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

# Copy the application code to the container
COPY . .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
