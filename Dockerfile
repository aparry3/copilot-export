FROM amazonlinux

COPY . /app

EXPOSE 5000

RUN yum install -y redhat-rpm-config \
  python-devel \
  python-pip \
  python-setuptools \
  python-wheel \
  python-cffi \
  libffi-devel \
  cairo \
  pango \
  gdk-pixbuf2

# Install Python Setuptools
RUN yum install -y python3

WORKDIR /app

ENV VIRTUAL_ENV="/opt/venv"
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_APP=copilot.py

RUN pip install -r requirements.txt

CMD ["python3", "-m", "flask", "run"]
