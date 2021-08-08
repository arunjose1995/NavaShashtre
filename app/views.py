from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.contrib.auth.models import User
from .models import Asset
from decimal import Decimal


@login_required(login_url="/login/")
def index(request):
    user_data = User.objects.all().count()
    asset_data = Asset.objects.all().count()
    context = {'segment': 'index', 'user_count': user_data, 'asset_count': asset_data}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def edit_profile(request):
    context = {'segment': 'edit-profile'}
    html_template = loader.get_template('edit-profile.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def save_profile(request):
    if request.method == 'POST':
        context = {'segment': 'profile'}
        user = User.objects.get(id=request.POST['user_id'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.save()
        html_template = loader.get_template('profile.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def view_asset(request):
    asset = Asset.objects.all()
    context = {'segment': 'add-asset', 'assets': asset}
    html_template = loader.get_template('laptops.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def add_asset(request):
    user = User.objects.all()
    context = {'segment': 'add-asset', 'users': user}
    html_template = loader.get_template('add-edit-laptop.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def save_asset(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['will_be_used_by'])
        asset = Asset.objects.create(
            name=request.POST['name'],
            model=request.POST['model'],
            memory=request.POST['ram'],
            cost=Decimal(round(float(request.POST['cost']), 2)),
            issuer=request.POST['owned_by'],
            asset_user=user
        )
        asset.save()
        return redirect('view-asset')


@login_required(login_url="/login/")
def edit_asset(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    user = User.objects.all()
    context = {'segment': 'edit-asset', 'asset': asset, 'users': user}
    html_template = loader.get_template('add-edit-laptop.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def update_asset(request, asset_id):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['will_be_used_by'])
        asset = Asset.objects.filter(id=asset_id)
        print(request.POST['name'], request.POST['name'])
        asset.update(
            name=request.POST['name'],
            model=request.POST['name'],
            memory=request.POST['ram'],
            issuer=request.POST['owned_by'],
            asset_user=user
        )
        return redirect('view-asset')


@login_required(login_url="/login/")
def delete_asset(request, asset_id):
    Asset.objects.filter(id=asset_id).delete()
    return redirect('view-asset')
