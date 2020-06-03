from scheduler.celery import app

from scheduler_app.models import Scheduler,Assets
from datetime import datetime,date




@app.task()
def Preview_publish(**kwargs):
    schedule_status = Scheduler.objects.get(id=kwargs['id'])
    schedule_status.publish_status = "Publish"
    schedule_status.save()
    asset_status = Assets.objects.get(id=kwargs['entity_id'])
    asset_status.is_published = True
    asset_status.save()
    print("successfully published")



class PreviewPublishScheduler():
    def __init__(self):
        self.today = date.today()
        self.scheduler_data = Scheduler.objects.filter(publish_schedule__year=self.today.year,publish_schedule__month=self.today.month,
                                          publish_schedule__day=self.today.day,publish_status="Unpublish",entity_type="Asset")


    def get_scheduler_by_date(self):
        print("calling")
        if self.scheduler_data:
            for schedule in self.scheduler_data:
                Preview_publish.apply_async(kwargs={'id':schedule.id,'entity_id':schedule.entity_id}, eta=schedule.publish_schedule)
        else:
            None



@app.task()
def do_task():
    print("do_task")
    today_schedule = PreviewPublishScheduler()
    today_schedule.get_scheduler_by_date()
