FROM python:3.7.5

WORKDIR /opt/code
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python", "run.py"]
