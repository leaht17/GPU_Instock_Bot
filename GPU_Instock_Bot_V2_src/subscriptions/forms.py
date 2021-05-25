from django.forms import CheckboxSelectMultiple, ModelMultipleChoiceField, ModelForm, EmailField

from gpus.models import GPU
from subscribers.models import Subscriber
from phonenumber_field.formfields import PhoneNumberField

# The form that takes in user contact info and selected GPUs to subscribe to.
class SubscriptionForm(ModelForm):  # directly populate model with form
    email = EmailField(required=False)
    phone = PhoneNumberField(required=False)
    # Models for GPU to be subscribed
    gpus = ModelMultipleChoiceField(
        queryset=GPU.objects.all(),  # display all GPUs in db
        widget=CheckboxSelectMultiple,
        required=False
    )

    # input user information (fields with boxes)
    class Meta:
        model = Subscriber
        fields = ['email', 'phone', 'gpus']
