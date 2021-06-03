from django.shortcuts import render
from .forms import AccountForm
from .models import Account

def login(request):
    bool_create_account = 'false'
    if request.method == 'POST':
        if request.POST.__contains__('create_accnt'):
            bool_create_account = 'true'
        else:
            form = AccountForm(request.POST or None)
            if form.is_valid():
                form.save()
                bool_create_account = 'false'
                
    context = {'bool_create_account': bool_create_account}
    return render(request, 'login.html', context)


