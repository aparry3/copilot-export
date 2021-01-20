# copilot-export
PDF export service for Copilot. Leverages the WeasyPrint Library to generate PDFs for
programs in mongo.

## Running Locally

To run locally make sure all dependencies are installed correctly (this includes both pip and
native c libraries).

1. Make sure pipenv is installed. You may use another virtualenv, but I have not tested that this works locally


2. `pipenv install`

3. Some other stuff...

...

...


## Deploying to Dev/Prod

1. Copy all project files to ec2 instance: `scp -r /PATH/TO/copilot-export/* copilot@EC2-INSTANCE:PATH/TO/copilot-export/`

2. Make sure `app.cfg` is copied to `/etc/copilot/app.cfg` as this is where Flask will try to read the file

3. Install the dependencies

```
yum install -y redhat-rpm-config \
  python-devel \
  python-pip \
  python-setuptools \
  python-wheel \
  python-cffi \
  libffi-devel \
  cairo \
  pango \
  gdk-pixbuf2

yum install -y python3
```

4. Set up Python virtualenv

```
VIRTUAL_ENV="/opt/venv"
python3 -m venv $VIRTUAL_ENV
PATH="$VIRTUAL_ENV/bin:$PATH"
```

5. Install `supervisor`

Update `supervisord.conf`...

6. Install `nginx`

Update `nginx.conf` to correctly expose the port exposed by copilot-export (8000)

Create `sites-enabled` entry and link to `nginx.conf`

**/etc/nginx/nginx.conf**
```
...
include /etc/nginx/sites-enabled/*;
...
```

**/etc/nginx/sites-enabled/[dev-]export.copilotfitness.com**
```server {
    listen       80;
    server_name  [dev-]export.copilotfitness.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

You will ned to start nginx as well

7. To run add the start command to `supervisor` and run `sudo supervisorctl start copilot-export`

`gunicorn -b 0.0.0.0:8000 wsgi`

`gunicorn` runs gunicorn server

`-b 0.0.0.0:8000` tells `gunicorn` which port to bind to

`wsgi` is the name of the python module for gunicorn to run

**supervisrd.conf**
```
[supervisord]
logfile=/tmp/supervisord.log ; main log file; default $CWD/supervisord.log
logfile_maxbytes=50MB        ; max main logfile bytes b4 rotation; default 50MB
logfile_backups=10           ; # of main logfile backups; 0 means none, default 10
loglevel=info                ; log level; default info; others: debug,warn,trace
pidfile=/tmp/supervisord.pid ; supervisord pidfile; default supervisord.pid
nodaemon=false               ; start in foreground if true; default false
minfds=1024                  ; min. avail startup file descriptors; default 1024
minprocs=200                 ; min. avail process descriptors;default 200

...

[supervisorctl]
serverurl=unix:///var/run/supervisor.sock ; use a unix:// URL  for a unix socket

...

[program:copilot]
directory=/home/copilot/app
command:/home/copilot/venv/bin/gunicorn -b 0.0.0.0:8000 wsgi
autostart=true
autorestart=true
stderr_logfile=/var/log/copilot/copilot.err.log
stdout_logfile=/var/log/copilot/copilot.out.log

...
```



## Useful Tips

* If traffic is not being handled by the server (aka backend is timing out), check logs for app,
    supervisor and nginx

* May just require a restart of process, supervisor, or nginx


#### Restart Copilot-Export

`sudo supervisorctl restart SERVICE`

Can also check the status of running services:

`sudo supervisorctl status`


#### Restart supervisor

`sudo systemctl restart supervisor`


#### Restart nginx

`sudo systemctl restart nginx`
