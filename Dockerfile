FROM python:3.9-slim

WORKDIR /app
RUN apt-get -y update
RUN apt-get -y install curl
COPY requirement.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirement.txt
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app","--reload","--host", "0.0.0.0", "--port", "8000"]