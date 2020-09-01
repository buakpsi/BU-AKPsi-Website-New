from django.db import models
from django.db.models import Case, When, Value, IntegerField

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

class PositionManager(models.Manager):
    def get_queryset(self):
        return super(PositionManager, self).get_queryset().annotate(
            position_order=Case(
                *[When(position=x, then=Value(i)) for i, x in enumerate(self.positions)],
                output_field = IntegerField()
            )
        ).order_by('position_order', 'brother__last_name')