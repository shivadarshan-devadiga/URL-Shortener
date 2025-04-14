# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /usr/src/app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Start app
CMD ["python", "run.py"]
