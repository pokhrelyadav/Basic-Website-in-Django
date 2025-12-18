from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    DEVICE_CHOICE = [
        ('L','Laptop'),
        ('M','Mobile')
    ]
    
    OPERATING_SYSTEM_CHOICES = [
    ("Laptop", (("windows", "Windows"), ("macos", "macOS"), ("linux", "Linux"))),
    ("Mobile", (("android", "Android"), ("ios", "iOS"))),
    ("unknown", "Unknown"),
]

    name = models.CharField('Product Name', max_length=60)
    description = models.TextField(verbose_name='Description of Product') #no compulsory max length becaue it for long text
    image = models.ImageField(upload_to='productImages/')
    device_type = models.CharField(max_length=2,choices=DEVICE_CHOICE)
    date_added = models.DateTimeField(default=timezone.now)
    brochure = models.FileField(upload_to='productBrochures/')
    os = models.CharField(max_length=10, choices=OPERATING_SYSTEM_CHOICES, default='unknown')
    
    
    def __str__(self):
        return self.name