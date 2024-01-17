# Your Python version
FROM python:3.9

# Install your application
WORKDIR /app
COPY flash/ flash/

RUN pip install -r flash/requirements.txt

ENV PYTHONPATH "/app"

# Startup command
CMD python flash/app.py