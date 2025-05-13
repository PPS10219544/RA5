FROM python:3.11-slim

WORKDIR /app

COPY RA5_1_1/ ./RA5_1_1/

RUN pip install --no-cache-dir --upgrade pip

CMD ["python3", "-m", "unittest", "RA5_1_1/test_calculator.py"]
