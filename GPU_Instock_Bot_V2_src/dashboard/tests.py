from django.test import TestCase

class TestDashboard(TestCase):
    def test_call_main(self):
        # redirects to same url path
        response = self.client.get('', follow=True)
        self.assertRedirects(response, '')

    def test_call_view_load(self):
        # check that response is OK for user submission
        self.client.login(username='user', password='notapassword')
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'suboverview.html')