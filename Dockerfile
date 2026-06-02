FROM python:3.11-slim

WORKDIR /app

COPY requirements-docker.txt .

RUN pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    -r requirements-docker.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]