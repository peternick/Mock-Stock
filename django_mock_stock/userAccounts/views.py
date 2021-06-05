from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Account
from django.contrib import messages
import re

def login(request):
    bool_create_account = 'false' #sent to the login page to determine whether a new account will be created or not
    if request.method == 'POST':
        if request.POST.__contains__('create_accnt'):
            bool_create_account = 'true'
        elif request.POST.__contains__('login_btn'):
            user = request.POST.get("username")
            passwd = request.POST.get("password")
            accnt = Account.objects.all().filter(username=user, password=passwd)
            if accnt.exists():
                return redirect('home')
 
        else:
            print('here')
            user = request.POST.get("username")
            passwd = request.POST.get("password")
            form = AccountForm(request.POST or None)

            accnt_name_valid = (re.search("\w{6,}", user)) and (re.search("((\d)+)", passwd))
            if form.is_valid() and accnt_name_valid:
                form.save() 
                bool_create_account = 'false'
            else:
                messages.success(request, "Error in account creation. A username must have at least 6 characters and a password must have at least one number.")
                bool_create_account = 'true'
                
    context = {'bool_create_account': bool_create_account}
    return render(request, 'login.html', context)


