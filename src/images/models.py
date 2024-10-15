from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_prefix(self):
        return f'images/{self.id}/'

    