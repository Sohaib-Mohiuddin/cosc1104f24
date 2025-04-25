FROM arm64v8/python:3.12-slim

# RUN apk --update add --no-cache bash nano vim
RUN groupadd -g 1000 dev && \
    useradd -m -u 1000 -g dev -s /bin/bash dev

RUN apt-get update && apt-get -y upgrade && apt-get install -y \
    --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

USER dev

WORKDIR /app

# ENV STATIC_URL /static
# ENV STATIC_PATH /app/static
ENV FLASK_APP server.py

COPY --chown=dev:dev . /app
COPY ./requirements.txt ./requirements.txt

RUN python3 -m pip install -r ./requirements.txt

EXPOSE 5555

ENTRYPOINT ["python3", "-m"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5555"]