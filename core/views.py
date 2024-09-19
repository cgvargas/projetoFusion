from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages

from .forms import ContatoForm
from .models import Servico, Funcionario, Recurso, Assinatura, Depoimento


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()  # Gera ação de posicionamento aleatório dos cards
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = Recurso.objects.order_by('?').all()
        context['assinaturas'] = Assinatura.objects.all()
        context['depoimentos'] = Depoimento.objects.all()
        # context['estrelas'] = list(range(1, 6))  # Adiciona a lista de estrelas
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)



