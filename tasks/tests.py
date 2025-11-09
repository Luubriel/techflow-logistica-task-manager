from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskModelTest(TestCase):
    
    def setUp(self):
        # Cria um usuário para ser usado nos testes
        self.user = User.objects.create_user(
            username='testuser', 
            password='password123'
        )

    def test_task_creation_with_defaults(self):
        """Teste se a tarefa é criada com os valores padrão corretos"""
        task = Task.objects.create(
            title="Tarefa Simples",
            user=self.user
        )
        
        # Verifica se salvou no banco
        self.assertEqual(Task.objects.count(), 1)
        
        # Verifica os campos
        self.assertEqual(task.title, "Tarefa Simples")
        self.assertEqual(task.description, "") # blank=True deve resultar em string vazia
        
        self.assertFalse(task.completed) 

    def test_task_str_representation(self):
        """Teste se o __str__ retorna o título da tarefa"""
        task = Task.objects.create(
            title="Comprar leite",
            user=self.user
        )
        self.assertEqual(str(task), "Comprar leite")

    def test_task_belongs_to_user(self):
        """Teste se a relação ForeignKey com User está funcionando"""
        task = Task.objects.create(
            title="Minha tarefa",
            user=self.user
        )
        # Verifica se podemos acessar o usuário através da tarefa
        self.assertEqual(task.user, self.user)
        # Verifica se podemos acessar a tarefa através do usuário (related_name='tasks')
        self.assertIn(task, self.user.tasks.all())

    def test_task_fields_max_length(self):
        """Teste (opcional) para garantir que não estamos excedendo limites, 
        embora o SQLite às vezes seja permissivo, é bom validar."""
        long_title = "a" * 201 # 1 caractere a mais que o max_length=200
        
        task = Task(
            title=long_title,
            user=self.user
        )
        
        # O Django não lança erro de validação no .save() automaticamente para max_length 
        # em alguns bancos, então forçamos a validação
        from django.core.exceptions import ValidationError
        with self.assertRaises(ValidationError):
            task.full_clean()