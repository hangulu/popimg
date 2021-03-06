from django.db import models

# Create your models here.
class PopImage(models.Model):
    """
    Create a model to define how the Popmeme objects should be stored in the
    database.
    """
     # Twiter handle
    user = models.CharField(max_length=120, default=None)
    # The most popular image on the user's timeline
    pop_img = models.CharField(max_length=120, null=True, blank=True, default=None)
    # The frequency of the most popular image
    freq = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user
