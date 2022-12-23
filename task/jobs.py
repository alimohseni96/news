from apscheduler.schedulers.background import BackgroundScheduler
from .schedule import runtime


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(runtime, 'interval', minutes=5)
    scheduler.start()
