FROM arm64v8/python:3.12-slim

RUN apt-get update && apt-get -y upgrade && apt-get install -y \
    --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip 
RUN pip install matplotlib numpy beautifulsoup4 \
    pymongo pytest flask 

# Default command to keep the container running or run your application
CMD ["tail", "-f", "/dev/null"]