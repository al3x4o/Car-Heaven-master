from django.shortcuts import render, redirect

from car_collection.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from car_collection.web.models import Car
from car_collection.accounts.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def get_cars():
    if Car.objects.count():
        return 'car'
    else:
        return None


def get_price():
    price_sum = 0
    for car in Car.objects.all():
        price_sum += car.price
    return price_sum


def index(request):
    profile = get_profile()
    if profile is not None:
        return render(request, 'index.html', context={'profile':profile})

    context = {
        'hide_nav_links': True,
        'profile': profile
    }

    return render(
        request,
        'index.html',
        context=context,
    )


def details_profile(request):
    profile = get_profile()
    price = get_price()

    context = {
        'profile': profile,
        'price': price,
    }

    return render(
        request,
        'profile-details.html',
        context,
    )


def catalogue(request):
    profile = get_profile()
    car = get_cars()
    if car is None:
        return render(request, 'catalogue.html', context={'profile': profile})

    context = {
        'profile': profile,
        'cars': Car.objects.all(),
    }

    return render(
        request,
        'catalogue.html',
        context,
    )


def create_car(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(
        request,
        'car-create.html',
        context,
    )


def details_car(request, pk):
    profile = get_profile()
    car = Car.objects \
        .filter(pk=pk) \
        .get()

    context = {
        'profile':profile,
        'car': car,
    }

    return render(
        request,
        'car-details.html',
        context,
    )


def edit_car(request, pk):
    profile = get_profile()
    car = Car.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile':profile,
        'form': form,
        'car': car,
    }

    return render(
        request,
        'car-edit.html',
        context,
    )


def delete_car(request, pk):
    profile = get_profile()
    car = Car.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        # Album.objects.filter(pk=pk).delete() # Don't do this!
        # Do it in the `form`
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile':profile,
        'form': form,
        'car': car,
    }

    return render(
        request,
        'car-delete.html',
        context,
    )
