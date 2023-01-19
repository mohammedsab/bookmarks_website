from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST, require_GET

from common.decorators import ajax_required

from .models import Image
from .forms import ImageCreateForm

# Create your views here.


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if is_ajax(request=request):
            # If the request is AJAX and the page is out of range
            # return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)

    if is_ajax(request=request):
        return render(request, 'images/image/list_ajax.html',
                      {'section': 'images', 'images': images})
    return render(request, 'images/image/list.html',
                  {'section': 'images', 'images': images})


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # assign the current user to the item
            new_item.user = request.user
            new_item.save()

            messages.success(request, 'Image added successfully')

            return redirect(new_item.get_absolute_url())

    else:
        form = ImageCreateForm(request.GET)

    return render(request, 'images/image/create.html', {'section': 'image', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html',
                  {'section': 'images', 'image': image})


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            
            if action == 'like':
                image.users_like.add(request.user)
                users_likes = list(image.users_like.all().values())
                # users_likes = 'liked'
                # print(image.users_like.all())

            else:
                image.users_like.remove(request.user)
                users_likes = list(image.users_like.all().values())
                
            return JsonResponse({'status': 'ok', 'users_likes': users_likes})
        except:
            pass

    return JsonResponse({'status': 'error'})

