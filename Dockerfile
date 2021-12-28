FROM python:3.10

WORKDIR /app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
COPY extract_code.py ./

ENTRYPOINT ["./extract_code.py"]
