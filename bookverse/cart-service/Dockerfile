FROM python:3.9


ENV PROJECT_DIR /usr/src/cart

WORKDIR ${PROJECT_DIR}

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5010

CMD ["flask", "run", "--host=0.0.0.0", "--port=5010"]
