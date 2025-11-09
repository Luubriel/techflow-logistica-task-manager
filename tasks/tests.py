from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_task_creation_with_defaults(self):
        """Teste se a tarefa é criada com os valores padrão corretos"""
        task = Task.objects.create(title="Tarefa Padrão", user=self.user)
        
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(task.priority, 'M') # Verifica padrão Média
        self.assertFalse(task.completed)     # Verifica padrão False (pendente)

    def test_task_custom_priority(self):
        """Teste se conseguimos definir prioridades diferentes"""
        task_high = Task.objects.create(title="Urgente", user=self.user, priority='A')
        task_low = Task.objects.create(title="Relax", user=self.user, priority='B')
        
        self.assertEqual(task_high.priority, 'A')
        self.assertEqual(task_low.priority, 'B')

    def test_task_str_representation(self):
        """Teste do __str__"""
        task = Task.objects.create(title="Comprar leite", user=self.user)
        self.assertEqual(str(task), "Comprar leite")

    def test_task_belongs_to_user(self):
        """Teste de relacionamento com User"""
        task = Task.objects.create(title="Minha tarefa", user=self.user)
        self.assertEqual(task.user, self.user)
        self.assertIn(task, self.user.tasks.all())