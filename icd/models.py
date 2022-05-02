from django.db import models
# Create your models here.

# Model Objects to interact through ORM with the Db
class Codes(models.Model):
    category_codes = models.CharField(max_length=20)
    diagnosis_codes = models.CharField(max_length=20, blank=True, null=True)
    full_code = models.CharField(max_length=20)
    abbrev_description = models.TextField(blank=True, null=True)
    full_description = models.TextField(blank=True, null=True)
    category_title = models.TextField(blank=True, null=True)
    version = models.SmallIntegerField(default=10)

    # Overriding the string form of the object when called to display category codes instead
    def __str__(self):
        return self.category_codes

