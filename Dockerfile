FROM python:3.12-slim

WORKDIR /app

# Copy code and install dependencies
COPY requeriments.txt .
RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

# Expose the Port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]