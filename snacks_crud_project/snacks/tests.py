from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack


class TestSnack(TestCase):

    def test_list_page_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks.html')
        self.assertTemplateUsed(response, 'main.html')

    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='test',
            email='teas@email.com',
            password='1234'
        )

        self.snack = Snack.objects.create(
            title='test',
            description="test info",
            purchaser = self.user
        )


    def test_str_method(self):
        self.assertEqual(str(self.snack),"test")

    def test_detail_view(self):
        url = reverse('detailview', args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'detailview.html')

    def test_create_view(self):
        obj={
            'title':"test2",
            'description': "info...",
            'purchaser': self.user.id
        }

        url = reverse('create_snack')
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertRedirects(response, reverse('detailview', args=[2]))


    
    def test_update_view():
        pass


    def test_delete_view():
        pass