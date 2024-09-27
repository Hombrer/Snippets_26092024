from django.db import models
from django.contrib.auth.models import User


LANGS = (
    ('py', 'Python'),
    ('js', 'JavaScript'),
    ('cpp', 'C++'),
    ('html', 'HTML')
)


class Snippet(models.Model):
    class Meta:
        ordering = ['name', 'lang']

    name = models.CharField(max_length=100, verbose_name="Имя сниппета")
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    public = models.BooleanField(default=True) # True -> public, False -> private

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Snippet({self.name}, {self.lang})'
