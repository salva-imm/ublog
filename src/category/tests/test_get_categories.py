from rest_framework import status
from rest_framework.test import APITestCase
from category.models.category import Category


class CategoriesTests(APITestCase):

    def setUp(self) -> None:
        self.data = {}

    def test_get_categories(self):
        url = "/backend/api/v1/category/"
        category = Category.objects.create(
            name="category",
            slug="category",
            short_description="short description",
            parent=None
        )
        response = self.client.get(url, self.data, format='json')
        self.assertEqual(response.data[0].get('name'), category.name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
