FROM spark:python3

USER root

WORKDIR /app

COPY ./app /app

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

RUN useradd -s /bin/bash -m pyadm

RUN chown -R pyadm:1000 /app
RUN chmod -R 755 /app

USER pyadm

EXPOSE 8080
EXPOSE 11000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

