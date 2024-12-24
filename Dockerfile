# Use an official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY app/ /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5000

# Run the Flask app
CMD ["python", "task_tracker.py"]
