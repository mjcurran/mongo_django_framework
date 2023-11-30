from celery import Celery

celery_app = Celery('config.celery_app')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

@celery_app.task
def add_message(text_data):
    import json
    from utils import get_db_handle
    print(text_data)
    handle, client = get_db_handle(db_name="radiohound",
                                       host="mongo",
                                       port=27017,
                                       username="django",
                                       password="vogqx496RjrJ")
    text_data_json = json.loads(text_data)
    print(text_data_json)
    collection = handle['messages']
    result = collection.insert_one(text_data_json)
    print("result: ", result)
    