from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.template.defaultfilters import slugify
from .models import Chair

class GalleryPage(ListView):
    model = Chair
    template_name = 'chairitems/index.html'
    context_object_name = 'chairs'

class ChairPage(DetailView):
    model = Chair
    template_name = 'chairitems/chair.html'
    context_object_name = 'chair'

class ChairCreatePage(CreateView):
    model = Chair
    template_name = 'chairitems/chaircreate.html'
    fields = ['title', 'price', 'description', 'image']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.slug = slugify(form.instance.title) #TODO: unique slug
        return super().form_valid(form)

# def gallery_page(request):
#     return render(request, 'chairitems/index.html')
# Create your views here.
