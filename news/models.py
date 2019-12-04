from django.db import models

class Rubric(models.Model):
    rubric = models.CharField(max_length=50, verbose_name="Рубрика")

    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"
        ordering = ["rubric"]

class Images(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)


class NewsM(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True)
    image_links = models.ManyToManyField(Images,)
    date = models.CharField(max_length=100, verbose_name="Дата публикации")
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-date"]
        unique_together = ("title", "content")



