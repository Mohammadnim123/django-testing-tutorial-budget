from urllib import response
from django.test import Client, TestCase
from django.urls import reverse
from budget.models import Project, Category, Expense
import json

class TestViews(TestCase):
    def setUp(self):    
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['project4'])
        self.project = Project.objects.create(name='project4', budget=100)
        #here it will generate a slug automatically

    def test_list_project_get(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')
        
    def test_detail_project_get(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')
        
    def test_detail_project_post(self):
        Category.objects.create(project=self.project, name='category1')
        response = self.client.post(self.detail_url, {'title': 'title1', 'amount': '10', 'category': 'category1'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.project.expenses.first().title, 'title1')
        
    def test_detail_project_post_no_data(self):
        response = self.client.post(self.detail_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.project.expenses.count(), 0)
        
    def test_detail_project_delete(self):
        Category.objects.create(project=self.project, name='category1')
        self.client.post(self.detail_url, {'title': 'title1', 'amount': '10', 'category': 'category1'})
        response = self.client.delete(self.detail_url, json.dumps({'id': 1}))
        self.assertEquals(self.project.expenses.count(), 0)
        self.assertEquals(response.status_code, 204)     

    def test_detail_project_delete_no_id(self):
        response = self.client.delete(self.detail_url, json.dumps({'id': 1}))
        self.assertEquals(self.project.expenses.count(), 0)
        self.assertEquals(response.status_code, 404)
        
    def test_create_new_project(self):
        url = reverse('add')
        response = self.client.post(url, {'name': 'project5', 'budget': '100', 'categoriesString': 'category1,category2'})
        project5 = Project.objects.get(id=2)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(project5.name, 'project5')
        self.assertEquals(project5.budget, 100)
        self.assertEquals(project5.category_set.count(), 2)
        