#!/usr/bin/env bash

set -Eeo pipefail

export STAND_INIT_COMPLETE='/opt/init/STAND_INIT_COMPLETE'


if [ ! -e "$STAND_INIT_COMPLETE" ]; then
  echo 'STAND INIT START'
  cd /opt/dbg_app

  echo 'WAITING FOR DB'
  while ! timeout 1 bash -c 'cat < /dev/null > /dev/tcp/db/5432'; do sleep 1; done
  python manage.py migrate
  python manage.py prepare_stand_user

  python manage.py loaddata fixtures/child_products.json
  python manage.py oscar_import_catalogue fixtures/*.csv
  python manage.py oscar_import_catalogue_images fixtures/images.tar.gz
  python manage.py oscar_populate_countries --initial-only
  python manage.py loaddata fixtures/pages.json fixtures/ranges.json

  python manage.py thumbnail cleanup
  python manage.py collectstatic --noinput

  echo 'WAITING FOR ELASTICSEARCH'
  while ! timeout 1 bash -c 'cat < /dev/null > /dev/tcp/e_search/9200'; do sleep 1; done
  python manage.py clear_index --noinput
  python manage.py update_oscar_index
  python manage.py prepare_stand_user

  touch "$STAND_INIT_COMPLETE"
  echo 'STAND INIT COMPLETE'
else
  echo 'STAND INIT SKIPPED'
fi

exec "$@"