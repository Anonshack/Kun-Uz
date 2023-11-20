from django.db import models


class HeadKunUz(models.Model):
    title = models.TextField(verbose_name='Title')
    image = models.ImageField(upload_to='kun-uz/', verbose_name='Image')
    set_data = models.DateField(null=True, verbose_name='Set Data', blank=True)
    info = models.TextField(verbose_name='Info')

    def __str__(self):
        return self.title


class InternalMenus(models.Model):
    menu = models.ForeignKey(HeadKunUz, on_delete=models.CASCADE)
    title = models.TextField(verbose_name='Title')
    set_data = models.DateField(null=True, verbose_name='Set Data', blank=True)
    link = models.URLField(blank=True, verbose_name='Link')
    info = models.TextField(verbose_name='Info')

    def __str__(self):
        return self.title


class TodayNews(models.Model):
    title = models.TextField(verbose_name='Title')
    set_data = models.DateField(null=True, verbose_name='Set Data', blank=True)
    info = models.TextField(verbose_name='Info')
    url = models.URLField(verbose_name='Urls')
    image = models.ImageField(upload_to='today-news/', verbose_name='Image', blank=True)

    def __str__(self):
        return self.title


class UnderKunUz(models.Model):
    title = models.TextField(verbose_name='Title')
    image = models.ImageField(upload_to='under-kun-uz/', verbose_name='Image')
    set_data = models.DateField(null=True, verbose_name='Set Data', blank=True)
    info = models.TextField(verbose_name='Info')
    url = models.URLField(verbose_name='Urls')

    def __str__(self):
        return self.title


class ThreeInfoUnder(models.Model):
    title = models.TextField(verbose_name='Title')
    image = models.ImageField(upload_to='three-kun-uz/', verbose_name='Image')
    set_data = models.DateField(null=True, verbose_name='Set Data', blank=True)
    info = models.TextField(verbose_name='Info')
    url = models.URLField(verbose_name='Urls')

    def __str__(self):
        return self.title