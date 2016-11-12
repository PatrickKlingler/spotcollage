from django.shortcuts import render
from forms import EmailForm
def index(request):
    form = None
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['your_email']
            return render(request, 'generator/result.html', {'email':email})
    else:
        form = EmailForm()
    return render(request, 'generator/index.html', {'form': form})