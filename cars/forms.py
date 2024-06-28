from django import forms
from cars.models import Brand, cars

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = cars(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car


class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = cars
        fields = '__all__'

    # def clean_value(self):
    #     value = self.clean_value.get('value')
    #     if value < 20000:
    #         self.add_error('value',"O Valor do veiculo deve ser maior ou igual a R$20.000,00")
    #     return value
