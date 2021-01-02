FROM python:3.9

# ---------- install ----------
COPY ./dbg_app /opt/dbg_app
COPY ./README.md /opt/dbg_app/README.md
COPY ./MANIFEST.in /opt/dbg_app/MANIFEST.in
COPY ./setup.cfg /opt/dbg_app/setup.cfg
COPY ./setup.py /opt/dbg_app/setup.py

WORKDIR /opt/dbg_app/
RUN apt-get update && apt-get install libgdal-dev -y
RUN python setup.py sdist && pip install dist/*

VOLUME /opt/init
COPY ./scripts/docker-entrypoint.sh /usr/local/bin/
COPY ./scripts/runserver.sh /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ['/usr/local/bin/runserver.sh']
