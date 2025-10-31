from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.DisplayNotes.as_view(), name="DisplayNotesView"),
    path("notedetail/<int:pk>", views.DisplayNotesDetails.as_view(), name="DisplayNotesDetailsView"),
    path("notedetail/<int:pk>/edit/", views.UpdateNote.as_view(), name="UpdateNoteView"),
    path("notedetail/<int:pk>/delete/", views.DeleteNote.as_view() , name="DeleteNoteView"),
    path("notespopular/", views.DisplayPopularNotes.as_view(), name="DisplayPopularNotesView" ),  
    path("createnote/", views.CreateNote.as_view(), name="CreateNoteView"),
]