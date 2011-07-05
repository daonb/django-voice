from django.utils import unittest
from djangovoice.models import *


class StatusTestCase(models.Model):
    def setUp(self):
        self.in_progress = Status.objects.create(
            title='In progress', slug='in_progress', default=False)
        self.need_to_test = Status.objects.create(
            title='Need to test', slug='need_to_test', default=True)

    def testSpeaking(self):
        self.assertEqual(self.in_progress.status, 'open')
        self.assertEqual(self.need_to_test.default, True)


class TypeTestCase(unittest.TestCase):
    def setUp(self):
        self.bug = Type.objects.create(title='Bug', slug='bug')
        self.betterment = Type.objects.create(title='Betterment',
                                              slug='betterment')

    def testSpeaking(self):
        self.assertEqual(self.bug.slug, 'bug')
        self.assertEqual(self.betterment.title, 'Betterment')


class FeedbackTestCase(unittest.TestCase):
    def setUp(self):
        feedback_type = Type.objects.create(title='Bug', slug='bug')
        feedback_user = User.objects.create_user(
            username='djangovoice', email='django@voice.com')
        self.login_form_does_not_work = Feedback.objects.create(
            type=feedback_type,
            title='Login form does not work.',
            description='What a fucking test...',
            anonymous=False,
            private=True,
            user=feedback_user)

    def testSpeaking(self):
        default_status = Status.objects.get(default=True)
        self.assertEqual(self.login_form_does_not_work.status, default_status)
