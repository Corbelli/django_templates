from django.db import models
from model_utils.models import TimeStampedModel


class UserMeta(TimeStampedModel):
    user_id = models.UUIDField(primary_key=True)
    name = models.TextField()