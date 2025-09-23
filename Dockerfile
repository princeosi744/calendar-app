# Use an official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt first (if you have one)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]

