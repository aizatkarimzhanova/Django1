from django.db import models

class ProgLang(models.Model):
    title = models.CharField(max_length=100, verbose_name='укажите язык програмирование')
    description = models.TextField(verbose_name='укажите описание языка')
    image = models.ImageField(upload_to='proglang/', verbose_name='загрузите фото', null=True)
    created_date_lang = models.PositiveIntegerField(verbose_name='укажите од создание языка програмирование', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    viki_url = models.URLField(verbose_name='вставьте ссылку википедии', null=True)
    file_lang = models.FileField(upload_to='files/', verbose_name='file', null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'язык прогримирование'
        verbose_name_plural = 'языки програмирование'

