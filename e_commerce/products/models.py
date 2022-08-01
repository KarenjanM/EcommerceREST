from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    @property
    def get_url(self):
        return f'/products/{self.id}/'

    @property
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    @staticmethod
    def make_thumbnail(image, size=(200, 220)):
        img = Image.open(image)
        img.convert('RGB')
        img = img.resize(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
