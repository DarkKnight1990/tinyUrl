from django.db import models

# Create your models here.


class CustomURL(models.Model):
    unique_id = models.BigIntegerField(unique=True, db_index=True)
    short_url = models.CharField(max_length=10)
    long_url = models.URLField(max_length=300)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.short_url

    @staticmethod
    def url_exists(long_url):
        try:
            custom_url = CustomURL.objects.get(long_url__iexact=long_url)
            return custom_url
        except CustomURL.DoesNotExist:
            return None
    
    @staticmethod
    def get_long_url(unique_id):
        try:
            custom_url = CustomURL.objects.get(unique_id__exact=unique_id)
            return custom_url.long_url
        except CustomURL.DoesNotExist:
            return None
