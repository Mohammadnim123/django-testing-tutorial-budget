from django.test import SimpleTestCase
from django.urls import resolve, reverse
from budget.views import ProjectCreateView, project_detail, project_list

class TestUrls(SimpleTestCase):
    def test_project_list_url_resolves(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, project_list)


    def test_project_create_url_resolves(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)
        
    def test_project_detail_url_resolves(self):
        url = reverse('detail', args=['test-project'])
        self.assertEquals(resolve(url).func, project_detail)