from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm
# Create your views here.

class CreateNote(LoginRequiredMixin, CreateView):
   model = Notes
   #fields = ["title","text"]
   form_class = NotesForm   
   context_object_name = "note"
   template_name = "notes/create_note.html"
   success_url = "/smart/notes/"
   login_url = "/admin/"

class UpdateNote(LoginRequiredMixin, UpdateView):
   model = Notes
   #fields = ["title","text"]
   form_class = NotesForm
   context_object_name = "note"
   template_name = "notes/update_note.html"
   success_url = "/smart/notes/"
   login_url = "/admin/"


class DisplayPopularNotes(LoginRequiredMixin, ListView):
   model = Notes
   context_object_name = "all_notes"
   template_name = "notes/display_notes.html"
   queryset = model.objects.filter(likes__gte=1)
   #queryset = Notes.objects.filter(likes__gte=1)
   login_url = "/admin/"

class DisplayNotes(LoginRequiredMixin, ListView):
   model = Notes
   context_object_name = "all_notes"
   template_name = "notes/display_notes.html"
   login_url = "/admin/"

"""
@login_required(login_url="../admin/")
def display_all_notes(request):
    return (render(request, "notes/display_notes.html", {"all_notes": models.Notes.objects.all()}))
"""
class DisplayNotesDetails(LoginRequiredMixin, DetailView):
   model = Notes
   context_object_name = "note"
   template_name = "notes/display_note_details.html"
   login_url = "/admin/"

"""
@login_required(login_url="../admin/")
def display_note_details(request, pk):
    try:
      note = models.Notes.objects.get(pk=pk)
      print(request)
    except:
       raise Http404("Notes matching query does not exist!")   
    return (render(request, "notes/display_note_details.html", {"note": note}))
"""