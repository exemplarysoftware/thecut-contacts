from thecut.contacts.models import ContactGroup, Person, Organisation
from thecut.core.forms import ModelAdminForm


class ContactGroupAdminForm(ModelAdminForm):
    class Meta:
        model = ContactGroup


class PersonAdminForm(ModelAdminForm):
    class Meta:
        model = Person


class OrganisationAdminForm(ModelAdminForm):
    class Meta:
        model = Organisation

