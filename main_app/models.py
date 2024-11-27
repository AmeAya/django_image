from django.db import models


class Paintings(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='paintings')
    # Чтобы ImageField работал, надо установить библиотеку pillow(pip install pillow)
    # ImageField -> Поле в Джанго для сохранения и работы с картинками
    # upload_to='<DIR_NAME>' -> Указывает Джанго имя папки(<DIR_NAME>) внутри медиа папки куда сохранять

    def __str__(self):
        return self.name
