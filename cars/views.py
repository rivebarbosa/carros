from typing import Any
from django.db.models.query import QuerySet
from cars.models import cars
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,UpdateView, DeleteView 


class CarsListView(ListView):
   model = cars
   template_name = 'cars.html'
   context_object_name = 'cars'

   def get_queryset(self):
      Carros = super().get_queryset().order_by('model')
      search = self.request.GET.get('search') 
      if search:
         Carros = Carros.filter(model__icontains=search)
      return Carros

class CarDetailView(DetailView):
   model = cars
   template_name = 'car_detail.html'
   
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
   model = cars
   form_class = CarModelForm
   template_name = 'new_car.html'
   success_url = '/cars'



@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
   model = cars
   form_class = CarModelForm
   template_name = 'car_update.html'

   def get_success_url(self):
      return reverse_lazy(
         'car_detail', kwargs = {'pk': self.object.pk}
      )
   
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
   model = cars
   template_name = 'car_delete.html'
   success_url =  '/cars/'
