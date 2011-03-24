from django.contrib import admin
from thecut.contacts.models import Address, Person
from thecut.core.admin import ModelAdmin


class AddressInline(admin.StackedInline):
    model = Address


class PersonAdmin(ModelAdmin):
    inlines = [AddressInline]
    exclude = ['addresses']

admin.site.register(Person, PersonAdmin)

