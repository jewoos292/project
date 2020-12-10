from django.forms import ModelForm

from prog.profileapp.models import Profile


class ProfileCreationFrom(ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "nickname", "message"]
