from django.test import TestCase
from django.urls import reverse
from .models import Notice, Author

# Create your tests here.
# Tests to be created as part of teh next task


class NoticeModelTest(TestCase):
    """
    Test suite for validating Notice-related views, including list and
    detail pages. Ensures that each view responds correctly and
    displays data.
    """

    def setUp(self):
        """
        Create sample Author and Notice objects for view tests.
        """
        author = Author.objects.create(name='Test Author')
        Notice.objects.create(title='Test Notice', content='This is a test '
                              'notice.', author=author)

    def test_notice_has_title(self):
        """
        Verify that a Notice object stores the correct title.
        """
        notice = Notice.objects.get(id=1)
        self.assertEqual(notice.title, 'Test Notice')

    def test_notice_has_content(self):
        """
        Verify that a Notice object stores the correct content.
        """
        notice = Notice.objects.get(id=1)
        self.assertEqual(notice.content, 'This is a test notice.')


class NoticeViewTest(TestCase):
    """
    Test suite for validating Notice-related views, including list and
    detail pages. Ensures that each view responds correctly and displays data.
    """

    def setUp(self):
        """
        Create sample Author and Notice objects for view tests.
        """
        author = Author.objects.create(name='Test Author')
        Notice.objects.create(title='Test Notice', content='This is a test '
                              'notice.', author=author)

    def test_notice_list_view(self):
        """
        Ensure the notice list view loads successfully and displays notices.
        """
        response = self.client.get(reverse('notice_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Notice')

    def test_notice_detail_view(self):
        """
        Ensure the notice detail view loads correctly and displays notice data.
        """
        notice = Notice.objects.get(id=1)
        response = self.client.get(reverse('notice_detail', args=[str(notice.
                                                                      id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Notice')
        self.assertContains(response, 'This is a test notice.')
