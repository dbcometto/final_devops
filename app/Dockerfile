FROM python:3.11-slim
COPY . /opt/app
WORKDIR /opt/app
RUN python -m pip install --upgrade pip && pip install -r ./requirements.txt
EXPOSE 8090
CMD ["python","app-log.py"]