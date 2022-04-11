from django.test import TestCase
from budget.models import Project, Category, Expense

class ProjectModelTest(TestCase):
    def setUp(self):
        self.project1 = Project.objects.create(name='project 1', budget=10000)
        self.test_category = Category.objects.create(project=self.project1, name='test-category')
        
    def test_slug_creation(self):
        self.assertEquals(self.project1.slug, 'project-1')
        
    def test_budget_left(self):
        self.assertEquals(self.project1.budget_left, 10000)
        Expense.objects.create(project=self.project1, title='expense 1', amount=1000, category=self.test_category)
        self.assertEquals(self.project1.budget_left, 9000)
        
    def test_total_transactions(self):
        Expense.objects.create(project=self.project1, title='expense 1', amount=1000, category=self.test_category)
        Expense.objects.create(project=self.project1, title='expense 2', amount=1000, category=self.test_category)
        self.assertEquals(self.project1.total_transactions, 2)        