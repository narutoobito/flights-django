from django.test import TestCase,Client

# Create your tests here.

class TestFlight(TestCase):


    def test_index(self):
        c= Client()
        response = c.get("/flights/")
        self.assertEqual(response.status_code,200)
