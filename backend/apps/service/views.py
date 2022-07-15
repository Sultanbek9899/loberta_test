from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.http import  JsonResponse
# Create your views here.

import requests

from .models import URL
from .forms import URLAddForm
from .tasks import get_url_status_code, get_update_all_urls


class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        urls = URL.objects.filter(user=request.user)
        form = URLAddForm()
        context = {
            "form": form,
            "urls": urls,
        }
        return render(request, 'index.html', context)

    def post(self, request):
        form = URLAddForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            get_url_status_code(instance)
            messages.success(request, "URL successfully added!")
            return redirect("index")
        return redirect("index")


@login_required
def update_url(request, pk):
    url = get_object_or_404(URL, pk=pk)
    if url.user == request.user:
        get_url_status_code(url)
        return JsonResponse({"message":"Ok"}, status=200)
    return JsonResponse({"message": "Forbidden"}, status=404)


@login_required
def delete_url(request, pk):
    url = get_object_or_404(URL, pk=pk)
    if url.user == request.user:
        url.delete()
        return JsonResponse({"message":"Ok"}, status=200)
    return JsonResponse({"message": "Forbidden"}, status=404)

@login_required
def update_all_user_url(request):
    get_update_all_urls(request.user)
    return JsonResponse({"message":"Ok"}, status=200)
