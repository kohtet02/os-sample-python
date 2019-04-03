import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))
os.environ["SLACK_BOT_TOKEN"] = "xoxb-549447176039-564699325077-TrYuOPpMtnJAIsm2eBP8vmUO"

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
