# Step 1: Start with a clean, official Python image
FROM python:3.11-slim

# Step 2: Create a system group and non-root system user for security
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -m -s /bin/bash appuser

# Step 3: Set up the application directory
WORKDIR /app

# Step 4: Securely handle dependencies
COPY --chown=appuser:appgroup requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Step 5: Copy application files and grant explicit ownership to our user
COPY --chown=appuser:appgroup . .

# Step 6: Explicitly switch execution context away from root to our secure user
USER appuser

# Step 7: Expose port
EXPOSE 5000

# Step 8: Run application
CMD ["python", "app.py"]
