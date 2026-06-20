# Step 1: Start with a clean, official, lightweight Python base image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy just the requirements file first to take advantage of Docker caching
COPY requirements.txt .

# Step 4: Install your Flask dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your application code (app.py, etc.) into the container
COPY . .

# Step 6: Expose the port your Flask app runs on (usually 5000)
EXPOSE 5000

# Step 7: Specify the exact command to run your application when the container starts
CMD ["python", "app.py"]
