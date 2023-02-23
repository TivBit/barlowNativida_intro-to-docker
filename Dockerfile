FROM python:3

WORKDIR /opt/payroll

COPY smonies.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./smonies.py"]

