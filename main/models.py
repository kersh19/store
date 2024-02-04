from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Product(models.Model):
    name = models.CharField('Наименование',max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField('Цена со скидкой',max_digits=10, decimal_places=2, null=True, blank=True)
    main_image = models.ImageField('Главное изображение',upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class AdditionalImage(models.Model):
    image = models.ImageField('Изображение',upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='additional_images')

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'