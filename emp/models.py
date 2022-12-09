from django.db import models

# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=200)
    empid=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    working=models.BooleanField(default=True)
    dept=models.CharField(max_length=10)
    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials/")
    rating=models.IntegerField(max_length=1)

    def __str__(self):
        return self.testimonial