from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm



# from .forms import NoteForm


def myapp(request):
    notes = [f'{note.title} {note.text}; ' for note in Note.objects.all()]
    return HttpResponse(notes)


def test(request):
    return render(request, 'add_note.html')


def index(request):
    return render(request, 'index.html')


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = NoteForm()

    return render(request, 'add_note.html', {'form': form})
