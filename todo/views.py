from django.shortcuts import render, redirect
from .models import Assignment 
# Create your views here.
def index(request):
    assignment = Assignment.objects.all()
    if request.method == 'POST':
        new_assignment = Assignment(
            title = request.POST['title']
        )
        new_assignment.save()
        return redirect("/")
    return render(request, 'index.html', {'assignments': assignment})
def delete(request, pk):
    assignment = Assignment.objects.get(id=pk)
    assignment.delete()
    return redirect('/')