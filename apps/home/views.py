from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Provider
from .forms import *

###############################################################################
# VALIDAÇÃO DAS TELAS DE LOGIN
###############################################################################
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}

    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

###############################################################################
# BANK ACCOUNTS / Contas bancárias
###############################################################################
def list_banks(request):
    banks = Bank.objects.all()
    return render(request, 'home/bank.html', {'banks': banks } )

###############################################################################
# PROVIDERS / FORNECEDORES
###############################################################################
def list_providers(request):
    providers = Provider.objects.all()
    return render(request, 'home/providers.html', {'providers': providers } )

#------------------------------------------------------------------------------
def create_provider(request):
    form = ProviderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_providers')

    return render(request, 'providers-form.html', {'form': form })

#------------------------------------------------------------------------------
def update_provider(request, id):
    provider = Provider.objects.get(codigo  = id)
    form = ProviderForm(request.POST or None, instance=provider)

    if form.is_valid():
        form.save()
        return redirect('list_providers')
    return render(request, 'providers-form.html', {'form': form, 'provider': provider })

#------------------------------------------------------------------------------
def delete_provider(request, id):
    provider = Provider.objects.get(codigo =id)

    if request.method == 'POST':
        provider.delete()
        return redirect('list_providers')

    return render(request, 'providers-delete-confirm.html', {'provider': provider })

###############################################################################
# BANK ACCOUNTS / Contas bancárias
###############################################################################
def list_bank_accounts(request):
    bank_account = BankAccount.objects.all()
    return render(request, 'home/bank_accounts.html', {'bank_account': bank_account } )

#------------------------------------------------------------------------------
def create_bank_account(request):
    form = BankAccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_bank_accounts')
    return render(request, 'bank_accounts.html', {'form': form})

#------------------------------------------------------------------------------
def update_bank_account(request, id):
    bank_account = BankAccount.objects.get(codigo = id)
    form = BankAccountForm()

    if form.is_valid():
        form.save()
        return redirect('list_bank_accounts')
    return render(request, 'bank_accounts.html', { 'form': form, 'bank_account': bank_account } )

#------------------------------------------------------------------------------
def delete_bank_account(request, id):
    bank_account = BankAccount.objects.get(codigo =id)

    if request.method == 'POST':
        bank_account.delete()
        return redirect('list_bank_accounts')
        
###############################################################################
# CATEGORIAS
###############################################################################
def list_categorys(request):
    categorys = Category.objects.all()
    return render(request, 'home/categorys.html', {'categorys': categorys } )

#------------------------------------------------------------------------------
def create_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_categorys')

    return render(request, 'categorys-form.html', {'form': form })

#------------------------------------------------------------------------------
def update_category(request, id):
    category = category.objects.get(codigo  = id)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect('list_categorys')
    return render(request, 'categorys-form.html', {'form': form, 'category': category })

#------------------------------------------------------------------------------
def delete_category(request, id):
    category = Category.objects.get(codigo =id)

    if request.method == 'POST':
        category.delete()
        return redirect('list_categorys')

    return render(request, 'categorys-delete-confirm.html', {'category': category })