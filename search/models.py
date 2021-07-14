from django.db import models
from django.urls import reverse


# # Create your models here.
# class article(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField(blank=True, null=True)
#
#     def get_absolute_url(self):
#         # return f"/products/{self.id}/delete/"
#         return reverse("articles:article-detail", kwargs={"id": self.id})
#
#         class Meta:
#             db_table = "article"

class job_data(models.Model):
    job_title = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    special = models.CharField(max_length=255, blank=True, null=True)
    # branch = models.CharField(max_length=255)
    # job_type = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=False)
    url = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

    class Meta:
        db_table = "job_data"


class user_history(models.Model):
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    special = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=255)
    exp_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = "user_history"
