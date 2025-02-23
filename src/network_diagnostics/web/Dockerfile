FROM python:3.10-slim

WORKDIR /app

# Copy api.py
COPY api.py /app/api.py

# Install Flask + dependencies
RUN apt-get update && apt-get install -y \
    iputils-ping \
    traceroute \
    dnsutils \
  && rm -rf /var/lib/apt/lists/*

RUN pip install flask

EXPOSE 5001

ENTRYPOINT ["python", "/app/api.py"]
