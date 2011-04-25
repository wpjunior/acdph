from django.db import models

class Category(models.Model):
    name = models.CharField("Nome", max_length=100)

    def __unicode__(self):
        return self.name

class Notice(models.Model):
    name = models.CharField("Nome", max_length=100)
    category = models.ForeignKey(Category, verbose_name="Categoria")
    date = models.DateField("Data", auto_now_add=True)
    text = models.TextField("Texto")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/news/%d/" % self.id
