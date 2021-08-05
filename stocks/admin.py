from django.contrib import admin
from .models import Stock, Request, Equipment
from django.core.exceptions import ValidationError
from django.contrib import messages
from django import forms
from django.contrib.auth import get_user_model
# Register your models here.
User = get_user_model()


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag',)


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

    def clean(self):
        status = self.cleaned_data.get('accepted')
        equipment = self.cleaned_data.get('equipment')
        quantity = self.cleaned_data.get('quantity')

        if status == True:
            superuser = User.objects.get(is_superuser=True)
            superuser_equipment = superuser.stock_set.all().get(equipment=equipment)

            if quantity <= superuser_equipment.quantity:
                superuser_equipment.quantity -= quantity
                superuser_equipment.save()

            else:

                raise forms.ValidationError(
                    f'Stock over! You "{equipment}" quantity is {superuser_equipment.quantity}.')
            return self.cleaned_data
        return self.cleaned_data


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    form = RequestForm
    list_display = ('user', 'equipment', 'image_tag', 'quantity',
                    'message', 'created', 'accepted')
    list_display_links = ('user', 'equipment', 'message',
                          'created',)
    search_fields = ('user__username', 'equipment__name', 'message')
    list_filter = (('user__username'), ('equipment__name'))

    # def save_model(self, request, obj, form, change):

    #     if obj.accepted == True:
    #         superuser_equipment = request.user.stock_set.all().get(
    #             equipment=obj.equipment)
    #         if obj.quantity <= superuser_equipment.quantity:
    #             superuser_equipment.quantity -= obj.quantity
    #             superuser_equipment.save()
    #             return super().save_model(request, obj, form, change)
    #         else:
    #             messages.error(request, 'Central Stock Over!')
    #             obj.accepted = False
    #     return super().save_model(request, obj, form, change)


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

    def clean(self):
        user = self.cleaned_data.get('user')
        if user.is_superuser is not True:
            equipment = self.cleaned_data.get('equipment')
            quantity = self.cleaned_data.get('quantity')
            superuser = User.objects.get(is_superuser=True)
            try:
                superuser_equipment = superuser.stock_set.all().get(equipment=equipment)
                if quantity <= superuser_equipment.quantity:
                    superuser_equipment.quantity -= quantity
                    superuser_equipment.save()
                else:
                    raise forms.ValidationError(
                        f'Stock over! You "{equipment}" quantity is {superuser_equipment.quantity}.')
                return self.cleaned_data
            except:
                raise forms.ValidationError(
                    f'Stock of "{equipment}" not added yet in Admin!"')
        return self.cleaned_data


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    form = StockForm
    list_display = ('user', 'equipment', 'image_tag', 'quantity', 'created')
    list_display_links = ('user', 'equipment', 'quantity', 'created')
    search_fields = ('user__username', 'equipment__name',)
    list_filter = (('user__username'), ('equipment__name'),)

    # def save_model(self, request, obj, form, change):
    #     if obj.user != request.user:
    #         # print(equipment)
    #         superuser_equipment = request.user.stock_set.all().get(
    #             equipment=obj.equipment)
    #         if obj.quantity < superuser_equipment.quantity:
    #             superuser_equipment.quantity -= obj.quantity
    #             superuser_equipment.save()
    #             return super().save_model(request, obj, form, change)

    #         else:
    #             messages.error(request, 'Central Stock Over')


admin.site.site_header = "Pendemic Supply Management"
admin.site.site_title = "Pendemic Supply Management"
admin.site.index_title = "Pendemic Supply Management"
