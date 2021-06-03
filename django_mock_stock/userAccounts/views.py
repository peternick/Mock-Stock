from django.shortcuts import render
from .forms import AccountForm
from .models import Account

def login(request):
    if request.method == 'POST':
        form = AccountForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {'bool_create_account': 'false'}
    return render(request, 'login.html', context)
# Create your views here.
