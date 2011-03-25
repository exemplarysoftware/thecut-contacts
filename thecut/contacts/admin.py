from django.contrib import admin
from thecut.contacts.forms import PersonAdminForm, \
    OrganisationAdminForm
from thecut.contacts.models import Address, Email, InstantMessengerHandle, \
    Nickname, Organisation, Person, PersonOrganisation, Phone, Website
from thecut.core.admin import ModelAdmin


class NicknameInline(admin.TabularInline):
    extra = 0
    model = Nickname


class AddressInline(admin.StackedInline):
    extra = 0
    model = Address


class EmailInline(admin.TabularInline):
    extra = 0
    model = Email
    verbose_name_plural = 'Email addresses'


class InstantMessengerHandleInline(admin.TabularInline):
    extra = 0
    model = InstantMessengerHandle
    verbose_name_plural = 'Instant messaging'


class PhoneInline(admin.TabularInline):
    extra = 0
    model = Phone
    verbose_name_plural = 'Phone numbers / addresses'


class WebsiteInline(admin.TabularInline):
    extra = 0
    model = Website


class PersonOrganisationInline(admin.TabularInline):
    extra = 0
    model = PersonOrganisation
    verbose_name = 'Organisation'
    verbose_name_plural = 'Organisations'


class OrganisationPersonInline(admin.TabularInline):
    extra = 0
    model = PersonOrganisation
    verbose_name = 'Person'
    verbose_name_plural = 'People'


class PersonAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', ('first_name', 'last_name'),
            'suffix', 'image', 'date_of_birth', 'biography', 'notes',
            'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'),
            'expire_at', 'publish_by', 'is_featured',
            ('created_at', 'created_by'),
            ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = PersonAdminForm
    list_display = ['name', 'email', 'phone', 'location']
    list_filter = ['organisations']
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    inlines = [PersonOrganisationInline, NicknameInline, AddressInline,
        EmailInline, PhoneInline, InstantMessengerHandleInline,
        WebsiteInline]
    search_fields = ['first_name', 'last_name', 'nicknames__value',
        'emails__value', 'phones__value']
    
    def email(self, obj):
        email = obj.get_email()
        return email and '<a href="mailto:%(email)s" ' \
            'title="%(title)s">%(email)s</a>' %(
            {'email': email, 'title': email.name}) or ''
    email.allow_tags = True
    
    def location(self, obj):
        address = obj.get_address()
        return address and ', '.join([address.city,
            unicode(address.country.name)]) or ''
    
    def phone(self, obj):
        phone = obj.get_phone()
        return phone or ''

admin.site.register(Person, PersonAdmin)


class OrganisationAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'abn', 'image', 'biography',
            'notes', 'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'),
            'expire_at', 'publish_by', 'is_featured',
            ('created_at', 'created_by'),
            ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = OrganisationAdminForm
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    inlines = [NicknameInline, AddressInline, EmailInline, PhoneInline,
        InstantMessengerHandleInline, WebsiteInline,
        OrganisationPersonInline]
    search_fields = ['name', 'abn', 'nicknames__value',
        'emails__value', 'phones__value']

admin.site.register(Organisation, OrganisationAdmin)

