from django.db import models

# Create your models here.
PUBLISH_TYPE = [
        ("Publish","Publish"),("Unpublish","Unpublish")
    ]

ENTITY_TYPE = [
        ("Asset","Asset"),("Content","Content")
    ]
class AssetsAndContent(models.Model):  
    entity_name = models.CharField(max_length=255, blank=True, null=True)
    entity_type = models.CharField(choices=ENTITY_TYPE,max_length=32)

    def __str__(self):
        return self.entity_name

class Scheduler(models.Model):
    entity_id = models.IntegerField(blank=True, null=True)
    entity_type = models.CharField(choices=ENTITY_TYPE,max_length=32)
    publish_status = models.CharField(max_length=100,choices=PUBLISH_TYPE)
    publish_schedule = models.DateTimeField(blank=True, null=True)

