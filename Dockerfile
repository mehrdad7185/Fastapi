# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "8000"]