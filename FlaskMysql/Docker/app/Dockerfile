FROM python:3.11.5
RUN pip install mysql-connector-python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY  app.py /app
COPY ./templates/ /app/templates/
COPY ./static/ /app/static/
COPY  requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python app.py