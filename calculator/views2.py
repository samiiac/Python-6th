from django.views import generic
from django.urls import reverse_lazy

class CalculatorView(generic.TemplateView):
    template_name = 'calc.html'
    
    
    
#CRUD views eager load lazy load
#formsets

from calculator.models import CalculatorHistory

class CalculatorCreateView(generic.CreateView):
    template_name = 'commons/form.html'
    queryset = CalculatorHistory.objects.all()
    fields = "__all__"
    
    success_url = reverse_lazy('calc-list')
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        # breakpoint()
        data.update(
            title = "Create new calculator history."
        )
        
        return data
    
class CalculatorReadView(generic.ListView):
    template_name = 'calc/index.html'
    queryset = CalculatorHistory.objects.all()
    fields = "__all__"
    context_object_name = 'object_list'
    #default = "object_list"
    
    success_url = reverse_lazy('calc-list')
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        data.update(
            title = "All the history."
        )
        return data

class CalculatorUpdateView(generic.UpdateView):
    template_name = 'commons/form.html'
    queryset = CalculatorHistory.objects.all()
    fields = "__all__"
    
    success_url = reverse_lazy('calc-list')
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        data.update(
            title = "Update the calculator history."
        )
        return data
    
class CalculatorDeleteView(generic.DeleteView):
    template_name = 'commons/form.html'
    queryset = CalculatorHistory.objects.all()
    
    success_url = reverse_lazy('calc-list')
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        data.update(
            title = "Delete the history."
        )
        
        return data
