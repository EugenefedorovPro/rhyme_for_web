from django import forms


class InputWordToStressForm(forms.Form):
    user_input = forms.CharField(label="В каком слове поставить ударение?", strip=True)


class StressVariantsForm(forms.Form):
    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = choices
        self.fields["select"].widget = forms.RadioSelect(choices=self.choices)

    # self.fields['height'].widget = forms.TextInput(attrs={'size':site_id})
    # choices = make_tuple_of_stress_variants("облако")
    # select = forms.ChoiceField(widget=forms.RadioSelect, choices=choices, label="")
    select = forms.ChoiceField(label="")


class DepthTimeForm(forms.Form):
    scale = forms.IntegerField(
        label="",
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "step": "1",
                "min": "1",
                "max": "5",
                "oninput": "rangevalue.value = value",
            },
        ),
        required=False,
        initial=2,
    )


class InputWordWithoutStress(forms.Form):
    user_input_to_rhyme = forms.CharField(label="", strip=True)
