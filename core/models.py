from django.db import models

class Document(models.Model):
    DOC_TYPE = (
        ('note', 'Note'),
        ('paper', 'Previous Paper'),
    )

    title = models.CharField(max_length=200)
    exam = models.CharField(max_length=100)
    doc_type = models.CharField(max_length=10, choices=DOC_TYPE)
    pdf = models.FileField(upload_to='documents/', null=True, blank=True)
    price = models.IntegerField(default=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
