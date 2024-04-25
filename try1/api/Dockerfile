FROM python:3.11-slim
COPY . /opt/app
WORKDIR /opt/app
RUN python -m pip install --upgrade pip && pip install -r ./requirements.txt
EXPOSE 8080
CMD ["python","runapi.py"]