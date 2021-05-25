from django.forms import CheckboxSelectMultiple, ModelMultipleChoiceField, ModelForm, EmailField
from gpus.models import GPU
from subscribers.models import Subscriber
from phonenumber_field.formfields import PhoneNumberField


# Creates Subscription Form App Object
# Args:
#   ModelForm: current model to be populated
class SubscriptionForm(ModelForm):

    # Instantiate models for GPU to be subscribed
    gpus = ModelMultipleChoiceField(
        queryset=GPU.objects.all(),  # display all GPUs in db
        widget=CheckboxSelectMultiple
    )

    # Set input user information fields for user input
    class Meta:
        model = Subscriber
        fields = ['email', 'phone', 'gpus']