from django.test import TestCase
from rest_framework.test import APIClient
import json

class ShortenerTestCase(TestCase):
    client = APIClient()
    initial = {
        'source_url': 'https://stackoverflow.com'
    }
    create = {
        'source_url': 'https://google.com'
    }

    def setUp(self):
        # Adding one row before
        self.client.post('/api/shortener/', self.initial, format='json')

    def test_create(self):
        response = self.client.post('/api/shortener/', self.create, format='json')
        data = json.loads(response.content)
        self.assertIn('source_url', data)
        self.assertIn('shortened_url', data)
        self.assertIn('views', data)
        self.assertIn('title', data)

        self.assertEquals(data['views'], 0)
        self.assertEquals(data['source_url'], self.create['source_url'])

        # Checks if the url was created in DB
        response = self.client.get('/api/shortener/', format='json')
        data = json.loads(response.content)
        self.assertEqual(2, len(data))

    def test_get(self):
        response = self.client.get('/api/shortener/', format='json')
        data = json.loads(response.content)
        self.assertEqual(1, len(data))
