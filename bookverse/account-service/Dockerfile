FROM python:3.9


ENV PROJECT_DIR /usr/src/account

WORKDIR ${PROJECT_DIR}

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]