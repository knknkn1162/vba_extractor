FROM python:3.10

WORKDIR /app

ARG VERSION=v0.60
RUN pip install -U https://github.com/knknkn1162/oletools/archive/refs/heads/${VERSION}_ja.zip

COPY extract_code.py ./
ENTRYPOINT ["./extract_code.py"]
