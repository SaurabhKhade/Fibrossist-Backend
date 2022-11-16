FROM python:3.10-slim-buster
WORKDIR /
COPY requirements.txt .
RUN python -m pip install --upgrade setuptools pip wheel
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . .
CMD gunicorn --bind 0.0.0.0:5000 app:app