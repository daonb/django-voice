from django.utils import unittest
from djangovoice.models import *

class TypeTestCase(unittest.TestCase):
    def setUp(self):
        self.bug = Type.objects.create(title='Bug', slug='bug')
        self.betterment = Type.objects.create(title='Betterment', slug='betterment')

    def testSpeaking(self):
        self.assertEqual(self.bug.slug, 'bug')
        self.assertEqual(self.betterment.title, 'Betterment')
