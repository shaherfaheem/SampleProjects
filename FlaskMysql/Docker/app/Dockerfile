FROM python:3.11.5
RUN pip install mysql-connector-python
EXPOSE 8080
WORKDIR /app
COPY  app.py /app
COPY ./templates/ /app/templates/
COPY ./static/ /app/static/
COPY  requirements.txt /app
RUN pip install -r requirements.txt
CMD python app.py