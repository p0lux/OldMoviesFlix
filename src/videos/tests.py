from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from .models import Video
from djangoflix.db.models import PublishStateOptions


class VideoModelTestCase(TestCase):
    def setUp(self):
        self.obj_A = Video.objects.create(title='This is my title', video_id='1')
        self.obj_B = Video.objects.create(title='This is my title', video_id='2', state=PublishStateOptions.PUBLISH)

    def test_valid_title(self):
        title = 'This is my title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_slug_field(self):
        title = self.obj_A.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_A.slug)

    def test_created_count(self):
        qs = Video.objects.all()
        self.assertTrue(qs.count(), 2)

    def test_draft_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.PUBLISH)
        published_qs = Video.objects.filter(
            state=Video.VideoStateOptions.PUBLISH,
            publish_timestamp__lte=timezone.now()
        )
        self.assertTrue(published_qs.exists())

    def test_published_manager(self):
        published_qs_query_set = Video.objects.all().published()  # Via query_set
        published_qs_manager = Video.objects.published()  # Via Manager
        self.assertTrue(published_qs_query_set.exists())
        self.assertEqual(published_qs_query_set.count(), published_qs_manager.count())
