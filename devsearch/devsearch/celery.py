from devsearch.devsearch.celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devsearch.settings")

app = Celery("devsearch")

# ✅ Loading config from django settings with CELERY_ prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# ✅ auto-dicsover the task.py inside all the apps
app.autodiscover_tasks()
