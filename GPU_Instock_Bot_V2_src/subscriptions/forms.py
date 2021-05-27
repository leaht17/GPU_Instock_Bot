from django.forms import CheckboxSelectMultiple, ModelMultipleChoiceField, ModelForm, EmailField
from gpus.models import GPU
from subscribers.models import Subscriber
from phonenumber_field.formfields import PhoneNumberField

# Instantiate models for GPU to be subscribed
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
    
    # Set input user information fields for user input
    class Meta:
        model = Subscriber
        fields = ['email', 'phone', 'gpus']