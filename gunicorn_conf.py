from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/home/ubuntu/banjararide/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/ubuntu/logs/gunicorn-access.log'
errorlog =  '/home/ubuntu/logs/gunicorn-error.log'