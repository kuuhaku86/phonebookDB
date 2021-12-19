gunicorn \
--access-logfile access.log \
--error-logfile error.log \
--pid process.pid \
--bind 0.0.0.0:32000 \
wsgi:app