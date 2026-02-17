# Usamos Python 3.11
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiamos requirements y lo instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el main.py
COPY main.py .

# Puerto que exponemos
EXPOSE 10000

# Comando para correr la app
CMD ["python3", "main.py"]
