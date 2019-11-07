from django.db import models


class Pizza(models.Model):
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    ROZMIARY = (
        (LARGE, 'duża'),
        (MEDIUM, 'średnia'),
        (SMALL, 'mała'),
    )

    nazwa = models.CharField(verbose_name='pizza', max_length=30)
    opis = models.TextField(blank=True, default='', help_text='Opis pizzy')
    rozmiar = models.CharField(max_length=1, choices=ROZMIARY, default=LARGE)
    cena = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    data = models.DateField('dodano', auto_now_add=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "pizze"

class Skladnik(models.Model):
    pizze = models.ManyToManyField(Pizza, related_name='skladniki')
    nazwa = models.CharField(verbose_name='składnik', max_length=30)
    jarski = models.BooleanField(
        verbose_name='jarski?',
        help_text='Zaznacz, jeżeli składnik jest odpowiedni dla wegetarian',
        default=False)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "skladniki"