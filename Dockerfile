FROM python:3.10-slim

WORKDIR /app

COPY subnet_calc.py /app/subnet_calc.py

RUN chmod +x /app/subnet_calc.py

ENTRYPOINT ["/app/subnet_calc.py"]
