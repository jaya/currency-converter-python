FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

RUN chmod +x ./prestart.sh

EXPOSE 8000
CMD ["bash", "-c", "./prestart.sh"]
