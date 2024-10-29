FROM arm64v8/python:3.12-slim

RUN groupadd -g 1000 dev && \
    useradd -m -u 1000 -g dev -s /bin/bash dev

RUN apt-get update && apt-get -y upgrade && apt-get install -y \
    --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Switch to the dev user for working inside the container
USER dev

WORKDIR /app

COPY --chown=dev:dev . /app

RUN pip install --no-cache-dir --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

# Set the default user for the container (dev)
USER dev

# Default command to keep the container running or run your application
CMD ["tail", "-f", "/dev/null"]