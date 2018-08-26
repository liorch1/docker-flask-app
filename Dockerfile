FROM python:alpine 
RUN pip install flask
COPY . /app
ENTRYPOINT ["python", "/app/app.py"]  
