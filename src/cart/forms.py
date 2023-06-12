from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


def frange2(start, stop, step):
    curr = start - step
    while curr < stop:
        curr += step
        yield curr


SELECT_SIZE = [(str(i), str(i)) for i in frange2(4, 12, 0.5)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label='Количество',
                                      choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
    size = forms.TypedChoiceField(label='Размер', choices=SELECT_SIZE, coerce=str)
