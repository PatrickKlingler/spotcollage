from django.shortcuts import render, redirect
from .collage import auth_url, create_collage
from .forms import EmailForm, TokenForm


def index(request):
    form = None
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['your_email']

            return redirect(auth_url())
    else:
        form = EmailForm()
    return render(request, 'generator/index.html', {'form': form})

def result(request):
    if request.method =='GET':
        form = TokenForm(request.GET)
        if form.is_valid():
            token = form.cleaned_data['code']
            contents = create_collage(token)

        return render(request, 'generator/result.html', {'contents': contents })
    pass
