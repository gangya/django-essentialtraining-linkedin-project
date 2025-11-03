from django.shortcuts import render, get_object_or_404
from . import models
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView 
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm
# Create your views here.

"""
#This method for updating an specific attribute of the model isn't a good practice

class UpdateLikeNote(LoginRequiredMixin, UpdateView):
   model = Notes
   #fields = ["title","text"]
   #form_class = NotesForm
   context_object_name = "note"
   #template_name = "notes/update_note.html"
   
   success_url = "notes/display_note_details.html"
   login_url = "/admin/"
   
"""
"""
This methos is appropiated to update an attribute of the model  
"""
@login_required(login_url="/admin/")
def UpdateLikeNote(request, pk):
       #print(request.method)       
       if request.method == 'POST':
         try:
            #note = models.Notes.objects.get(pk=pk)
            note = get_object_or_404(Notes, pk=pk)
            note.likes+=1
            note.save()
            return HttpResponseRedirect(reverse("DisplayNotesDetailsView", args=(pk,)))
         except:
            raise Http404("Notes matching query, note does not exist!")   
       raise Http404("Only Post method for changing system!", request.method)


class DeleteNote(LoginRequiredMixin, DeleteView):
   model = Notes
   context_object_name = "note"
   template_name = "notes/delete_note.html"
   success_url = "/smart/notes/"
   login_url = "/admin/"


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