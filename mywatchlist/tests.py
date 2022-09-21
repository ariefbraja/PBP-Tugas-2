from django.test import TestCase, Client
from django.urls import resolve

class ContohAppTest(TestCase):
    def test_mywatchlist_html(self):
        response = Client().get('https://tugas2ariefbraja.herokuapp.com/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_json(self):
        response = Client().get('https://tugas2ariefbraja.herokuapp.com/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_xml(self):
        response = Client().get('https://tugas2ariefbraja.herokuapp.com/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)


# Create your tests here.
