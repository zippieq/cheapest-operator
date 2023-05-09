import unittest
import json
from io import StringIO
from app import app

class TestCSVUpload(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.trie = app.trie

    def test_upload_csv(self):
        data = {
            'file': (StringIO('Operator A\n1234, 0.5\n'), 'test.csv')
        }
        response = self.app.post('/upload-csv', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CSV uploaded successfully.', response.data)
        # Assert that trie has been updated correctly
        self.assertEqual(self.trie.search('1234'), (0.5, 'Operator A', '1234'))

    def test_find_cheapest_operator(self):
        # Insert test data into trie
        self.trie.insert('1234', 'Operator A', 0.5)
        self.trie.insert('12345', 'Operator B', 0.4)

        response = self.app.get('/find-cheapest-operator?number=12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {
            'number': '12345',
            'operator': 'Operator B',
            'cost': 0.4,
            'prefix': '12345'
        })

class TestCSVUploadBDD(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.trie = app.trie

    def test_upload_csv(self):
        # Given
        data = {
            'file': (StringIO('Operator A\n1234, 0.5\n'), 'test.csv')
        }
        expected_response = 'CSV uploaded successfully.'

        # When
        response = self.app.post('/upload-csv', data=data, content_type='multipart/form-data')

        # Then
        self.assertEqual(response.status_code, 200)
        self.assertIn(expected_response.encode('utf-8'), response.data)
        # Assert that trie has been updated correctly
        self.assertEqual(self.trie.search('1234'), (0.5, 'Operator A', '1234'))

    def test_find_cheapest_operator(self):
        # Given
        self.trie.insert('1234', 'Operator A', 0.5)
        self.trie.insert('12345', 'Operator B', 0.4)
        expected_response = {
            'number': '12345',
            'operator': 'Operator B',
            'cost': 0.4,
            'prefix': '12345'
        }

        # When
        response = self.app.get('/find-cheapest-operator?number=12345')

        # Then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), expected_response)
