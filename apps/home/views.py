from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Provider
from .forms import *

###############################################################################
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
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
# PROVIDERS
###############################################################################
def list_providers(request):
    providers = Provider.objects.all()
    return render(request, 'home/providers.html', {'providers': providers } )

def create_provides(request):
    form = ProviderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_providers')

    return render(request, 'providers-form.html', {'form': form })

def update_provider(request, id):
    provider = Provider.objects.get(codigo  = id)
    form = ProviderForm(request.POST or None, instance=provider)

    if form.is_valid():
        form.save()
        return redirect('list_providers')
    return render(request, 'providers-form.html', {'form': form, 'provider': provider })

def delete_provider(request, id):
    provider = Provider.objects.get(codigo =id)

    if request.method == 'POST':
        provider.delete()
        return redirect('list_providers')

    return render(request, 'providers-delete-confirm.html', {'provider': provider })

###############################################################################