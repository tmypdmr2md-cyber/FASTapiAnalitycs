FROM python:3.12-slim

RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH
RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code
WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install gunicorn

COPY . .

RUN chmod +x ./boot/start.sh

EXPOSE 80

CMD ["./boot/start.sh"]