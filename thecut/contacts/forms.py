from thecut.contacts.models import Person, Organisation
from thecut.core.forms import ModelAdminForm


class PersonAdminForm(ModelAdminForm):
    class Meta:
        model = Person


class OrganisationAdminForm(ModelAdminForm):
    class Meta:
        model = Organisation

