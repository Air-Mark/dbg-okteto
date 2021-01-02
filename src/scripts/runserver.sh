#!/usr/bin/env bash

set -Eeo pipefail

while ! timeout 1 bash -c 'cat < /dev/null > /dev/tcp/db/5432'; do sleep 1; done
while ! timeout 1 bash -c 'cat < /dev/null > /dev/tcp/e_search/9200'; do sleep 1; done

#/usr/local/bin/gunicorn dbg_app.wsgi:application -w 2 -b 0.0.0.0:888
python main.py