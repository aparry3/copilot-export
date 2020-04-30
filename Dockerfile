FROM amazonlinux
COPY . /app

RUN yum install gcc libffi-devel python-devel openssl-devel -y

# Install Python Setuptools
RUN yum install -y python3 \
    python3-dev \
    python \
    python-dev \
    python3-pip \
    python-setuptools

WORKDIR /app
RUN python3 -m pip install -r requirements.txt
