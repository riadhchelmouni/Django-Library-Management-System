# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY LMS /app/LMS

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "/app/LMS/manage.py", "runserver", "127.0.0.1:8000"]
