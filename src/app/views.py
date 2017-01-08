from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import json
from django.core import serializers
# Create your views here.

from .forms import ImageForm
from .models import Image


def immage_add(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            qs = Image.objects.all()
            print("qs___________")
            print(qs)
            ajaxData = {}
            ajaxData['msg'] = 'Created a new blog post!'
            ajaxData['data'] = serializers.serialize('json', qs)
            # ajaxData['data'] = str(qs) //for image
            # json.dumps(qs.__dict__)
            return HttpResponse(json.dumps(ajaxData))
        else:
            ajaxData = {}
            ajaxData['msg'] = 'Sorry no data saved!'
            return HttpResponse(json.dumps(ajaxData))
    template = "image_add.html"
    return render(request, template, context)
