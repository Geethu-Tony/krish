from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class Booklistview(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'book_list'

class Bookdetailview(DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'

class Bookupdateview(UpdateView):
    model=Book
    template_name = 'update.html'
    context_object_name = 'book'
    fields=('title', 'author', 'genre', 'publication_date', 'avilability')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Bookdeleteview(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')

def index(request):
    book=Book.objects.all()
    context ={
        'book_list':book
    }
    return render(request,'home.html',context)

def detail(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'detail.html',{'book':book})  

def delete(request,id):
    if request.method=='POST':
        book=Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request, id):
    book=Book.objects.get(id=id)
    form=BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html', {'form': form, 'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
    return render(request, 'add.html', {'form': form})






