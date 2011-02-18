from django.test import TestCase

class HomePageUrlTest(TestCase):
    def test_sucess_when_get_homepage(self):
        response = self.client.get("/")
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, "index.htm")
