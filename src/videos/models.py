from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    # timestamp =
    # updated =
    # state =
    # publish_timestamp =

    @property
    def is_published(self):
        return self.active


class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Published video'
        verbose_name_plural = 'Published videos'


class VideoAllPoxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'All video'
        verbose_name_plural = 'All videos'