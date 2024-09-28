from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name or ''

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'


class News(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    link = models.URLField(blank=True, null=True)
    time = models.CharField(max_length=200, blank=True, null=True)
    tag = models.CharField(max_length=200, blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or ''

    class Meta:
        verbose_name = 'New category'
        verbose_name_plural = 'News category'


class Sud(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='sud_images/', null=True, blank=True)
    link = models.URLField(blank=True, null=True)
    time = models.CharField(max_length=200, blank=True, null=True)
    tag = models.CharField(max_length=200, blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or ''

    class Meta:
        verbose_name = 'Sud'
        verbose_name_plural = 'Sudlar'


class Jurnalistik(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='jurnalistik_images/', null=True, blank=True)
    link = models.URLField(blank=True, null=True)
    time = models.CharField(max_length=200, blank=True, null=True)
    tag = models.CharField(max_length=200, blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or ''

    class Meta:
        verbose_name = 'Jurnalistik surishtiruv'
        verbose_name_plural = 'Jurnalistik surishtiruvlar'


class Yangilik_sub(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='yangilik_sub_images/', null=True, blank=True)
    link = models.URLField(blank=True, null=True)
    time = models.CharField(max_length=200, blank=True, null=True)
    tag = models.CharField(max_length=200, blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or ''

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    sud = models.ForeignKey(Sud, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    jurnalistik = models.ForeignKey(Jurnalistik, on_delete=models.CASCADE, related_name='comments', null=True,
                                    blank=True)
    yangilik_sub = models.ForeignKey(Yangilik_sub, on_delete=models.CASCADE, related_name='comments', null=True,
                                     blank=True)

    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.comment[:20]}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def save(self, *args, **kwargs):
        if sum(bool(x) for x in [self.news, self.sud, self.jurnalistik, self.yangilik_sub]) > 1:
            raise ValueError("Comment can only be related to one model at a time.")
        super().save(*args, **kwargs)


