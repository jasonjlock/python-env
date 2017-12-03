FROM python:3.6.3
ADD . /code
WORKDIR /code
RUN pip install --upgrade -r requirements.txt
EXPOSE 8000
CMD ["python", "server.py"]

