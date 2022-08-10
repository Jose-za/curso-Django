
from django.forms import ModelForm

from cursos.models import Cursos


class cursosForms(ModelForm):
    class Meta:
        model = Cursos
        fields = ('nombre', 'curso','email','tiempo')

