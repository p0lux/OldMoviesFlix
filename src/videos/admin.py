from django.contrib import admin
from .models import VideoAllPoxy, VideoPublishedProxy


class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id', 'is_published', 'state']
    search_fields = ['title']
    list_filter = ['state', 'active']
    readonly_fields = ['id', 'is_published', 'publish_timestamp']

    class Meta:
        model = VideoAllPoxy

    # Define our property directly in our models.
    # def published(self, obj):
    #     return obj.active


admin.site.register(VideoAllPoxy, VideoAllAdmin)


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']

    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)


admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
