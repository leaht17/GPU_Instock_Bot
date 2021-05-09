from django.forms import CheckboxSelectMultiple, ModelMultipleChoiceField, ModelForm, EmailField

from gpus.models import GPU
from subscribers.models import Subscriber
from phonenumber_field.formfields import PhoneNumberField


class SubscriptionForm(ModelForm):
    gpus = ModelMultipleChoiceField(
        queryset=GPU.objects.all(),
        widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Subscriber
        fields = ['email', 'phone', 'gpus']
