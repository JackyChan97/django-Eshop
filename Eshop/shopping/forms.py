from django import forms

class AddForm(forms.Form):
    category = (
        ("MW", "Men's wear"),
        ("WW", "Women's wear"),
        ("CW", "Children's wear"),
    )
    name = forms.CharField(label="Name", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(label="Price",max_digits=6,decimal_places=2,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    introduction = forms.CharField(label="Introduction", max_length=1024, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #imagePath = forms.ImageField(label="ImagePath", required=False, widget=forms.FileInput({'class': 'form-control'}))
    kind = forms.ChoiceField(label="Kind", choices=category)

