from django.shortcuts import render
from .models import DreamTrip,Journey
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
# Create your views here.
def blogpost(request):
    model=DreamTrip.objects.all()
    context={
        'DreamTrip':model
    }
    return render(request,'blog/blog.html',context)
def blogdetail(request,pk):
    print(pk)
    model1=DreamTrip.objects.filter(pk=pk)
    print(model1)
    
    return render(request,'blog/details.html',{'DreamTrip':model1})

# class BlogListView(ListView):
#     model = DreamTrip
#     template_name = 'blog/blog.html'


# class BlogDetailView(DetailView):
#     model = DreamTrip
#     template_name = 'blog/details.html'

class BlogCreateView(CreateView):
    model = DreamTrip
    template_name = 'blog/create_trip.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = DreamTrip
    fields = '__all__'
    template_name = 'blog/post_edit.html'
    # success_url = reverse_lazy('details')


class BlogDeleteView(DeleteView):
    model = DreamTrip
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog')


            
