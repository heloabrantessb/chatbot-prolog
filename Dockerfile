FROM python:3.11

RUN apt-get update && apt-get install -y --no-install-recommends \
    swi-prolog \
    gcc \
    g++ \
    make \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyswip 
WORKDIR /chatbot 

COPY . .

CMD ["tail", "-f", "/dev/null"]
