from django.test import TestCase
from budget.forms import ExpenseForm

class ExpenseFormTest(TestCase):
    
    def test_form_has_fields(self):
        form = ExpenseForm()
        expected = ['title', 'amount', 'category']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
    
    def test_valid_form(self):
        form = ExpenseForm({
            'title': 'test expense',
            'amount': 100,
            'category': 'test-category'
        })
        self.assertTrue(form.is_valid())    
    