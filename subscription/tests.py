from django.test import TestCase

class SubscriptionUrlTest(TestCase):
    def test_sucess_when_get_homepage(self):
        response = self.client.get("/inscricao")
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, "subscription.htm")
