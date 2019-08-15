from django.db import models


class UrlsModel(models.Model):
    website_urls = models.URLField()

    def __str__(self):
        return "%s" % str(self.website_urls)

    class Meta:
        verbose_name = "Url"
        verbose_name_plural = "Urls"


class DataModel(models.Model):
    email = models.EmailField()
    # website_urls = models.ManyToManyField(UrlsModel)
    website_urls = models.TextField(max_length=5000)

    def __str__(self):
        return "%s" % self.email

    class Meta:
        verbose_name = "Data"
        verbose_name_plural = "Data Set"
