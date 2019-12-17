FROM tiangolo/uvicorn-gunicorn:python3.7

RUN mkdir -p /prosapient

WORKDIR /prosapient

COPY requirements.txt /prosapient/requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir -r /prosapient/requirements.txt

COPY prosapient /prosapient

EXPOSE 8000
