from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import cars, CarInventory

def car_inventure_update():
    cars_count = cars.objects.all().count()
    cars_value = cars.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )

@receiver(pre_save,sender=cars)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = "Bio Gerada automaticamente"

@receiver(post_save, sender=cars)
def car_post_save(sender,instance, **kwargs):
    car_inventure_update()

@receiver(post_delete, sender=cars)
def car_post_delete(sender,instance, **kwargs):
    car_inventure_update()

