FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Comando para rodar Gunicorn com 1 worker e 2 threads
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "app:app"]