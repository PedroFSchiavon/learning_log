from django.db import models

# Create your models here.

class Topic(models.Model):
    '''Local onde será inserido oq o usuário esta aprendendo'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        '''Retorna uma representação em string do modelo.'''
        return self.text
