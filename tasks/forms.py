from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: Comprar leite'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Detalhes da tarefa...'
            }),
            # Checkbox precisa da classe 'form-check-input' para ficar bonito no Bootstrap
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }