from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from src.main.views import *


class HomePageTest(TestCase):
    '''тест домашней страницы'''
    def test_root_url_resolves_to_home_page_view(self):
        '''тест: корневой url преобразуется в представление
        домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        request = HttpRequest()
        request.session = {}
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('Домашняя страница', html)
        self.assertTrue(html.endswith('</html>'))


