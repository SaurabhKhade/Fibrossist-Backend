FROM python:3.10-slim-buster
WORKDIR /
COPY requirements.txt .
RUN python -m pip install --upgrade setuptools pip wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
COPY . .
# RUN export FLASK_APP=app.py
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]