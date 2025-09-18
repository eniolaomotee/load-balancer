# Build from a slim Debian(image) image
FROM debian:stable-slim

# Update apt
RUN apt update
RUN apt upgrade -y

# Install build tooling
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

# Download python interpreter code and unpack it
RUN wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz
RUN tar -xf Python-3.10.*.tgz

# Build the python interpreter from source
RUN cd Python-3.10.8 && ./configure --enable-optimizations && make && make altinstall

# Copy our code into the image 
COPY main.py main.py

# Copy our data dependency into the image
COPY books/ books/

CMD ["python3.10", "main.py"]



# A simpler version using the official python image

# FROM python:3.12-slim

# WORKDIR /app

# COPY main.py main.py
# COPY books/ books/

# CMD ["python", "main.py"]

# resource limiting example
# docker run -d --cpus="0.25" --name cpu-stress alexeiled/stress-ng --cpu 2 --timeout 10m