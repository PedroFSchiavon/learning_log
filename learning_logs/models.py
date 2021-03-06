from django.db import models

# Create your models here.

class Topic(models.Model):
    """Local onde será inserido oq o usuário esta aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Retorna uma representação em string do modelo.'''
        return self.text


class Entry(models.Model):
    """Aprendizados sobre algum assunto qualquer."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''Devolve uma representação em string do modelo.'''
        if len(self.text.__str__()) <= 50:
            return self.text
        else:
            return self.text[:50] + '...'

