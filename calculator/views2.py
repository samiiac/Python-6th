from django.views import generic


class CalculatorView(generic.TemplateView):
    template_name = 'calc.html'
    
    
    
#CRUD views

from calculator.models import CalculatorHistory

class CalculatorCreateView(generic.CreateView):
    template_name = 'calc/create.html'
    queryset = CalculatorHistory.objects.all()
    fields = "__all__"
    
class CalculatorReadView(generic.ListView):
    template_name = 'calc/index.html'
    queryset = CalculatorHistory.objects.all()
    fields = "__all__"
    context_object_name = 'object_list'
    #default = "object_list"

class CalculatorUpdateView(generic.UpdateView):
    template_name = 'calc/update.html'
    queryset = CalculatorHistory.objects.all()
    fields = "__all__"
    
class CalculatorDeleteView(generic.DeleteView):
    template_name = 'calc/delete.html'
    queryset = CalculatorHistory.objects.all()
