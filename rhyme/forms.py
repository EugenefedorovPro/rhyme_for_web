from django import forms
<<<<<<< HEAD
from rhyme_rus.rhyme import stress_word_by_nn
=======
>>>>>>> 26e9964edea31fb01fb9c5e2190530ae0e3952f9


class StressVariantsForm(forms.Form):
    choices = ((1, "за'мок"), (2, "замо'к"))
    select = forms.ChoiceField(widget=forms.RadioSelect, choices=choices, label="")
<<<<<<< HEAD


class DepthTimeForm(forms.Form):
    scale = forms.IntegerField(
        label="",
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "step": "5",
                "min": "0",
                "max": "100",
                "oninput": "rangevalue.value = value",
                "list": "tickmarks",
            },
        ),
        required=False,
    )
=======
>>>>>>> 26e9964edea31fb01fb9c5e2190530ae0e3952f9
