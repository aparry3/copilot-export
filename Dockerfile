FROM amazonlinux

COPY . /app

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

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi"]
