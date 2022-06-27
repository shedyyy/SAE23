from django.urls import path
from . import views
from django.contrib import admin
from .views import *

urlpatterns = [
    path('etudiant/', views.etudiant),
    path('', views.home),
    path('home/', views.home),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('traitementupdate/<int:id>/',views.traitementupdate),
    path("update/<int:id>",views.update),
    path("delete/<int:id>", views.delete),


    path('examens/', views.examens),
    path('ajout_exa/', views.ajout_exa),
    path('traitement_exa/', views.traitement_exa),
    path('affiche_exa/<int:id>/', views.affiche_exa),
    path('traitementupdate_exa/<int:id>', views.traitementupdate_exa),
    path("update_exa/<int:id>", views.update_exa),
    path("delete_exa/<int:id>", views.delete_exa),


    path('note/', views.note),
    path('ajout_note/', views.ajout_note),
    path('traitement_note/', views.traitement_note),
    path('affiche_note/<int:id>/', views.affiche_note),
    path('traitementupdate_note/<int:id>/', views.traitementupdate_note),
    path("update_note/<int:id>", views.update_note),
    path("delete_note/<int:id>", views.delete_note),

    path('UE/', views.UE),
    path('aUnite/', views.aUnite),
    path('tUnite/', views.tUnite),
    path("UEupdate/<int:id>", views.UEupdate),
    path("UEdelete/<int:id>", views.delete),
    path("delUE/<int:id>", views.delUE),
    path('tuUE/<int:id>', views.tuUE),
    path('affiche_ue/<int:id>', views.affiche_ue),


    path('ressourcess/', views.ressourcess),
    path('ajoutressources/', views.ajoutressources),
    path('traitementressources/', views.traitementressources),
    path('traitementupdateressources/<int:id>', views.traitementupdateressources),
    path("updateressources/<int:id>/", views.updateressources),
    path("deleteressources/<int:id>", views.deleteressources),
    path('affiche_res/<int:id>/', views.affiche_res),


    path('enseignant/', views.enseignant),
    path('ajoutenseignant/', views.ajoutenseignant),
    path('traitementenseignant/', views.traitementenseignant),
    path('traitementupdateenseignant/<int:id>/', views.traitementupdateenseignant),
    path("updateenseignant/<int:id>", views.updateenseignant),
    path("deleteenseignant/<int:id>", views.deleteenseignant),


    path("notes_pdf/<int:id>", views.notes_pdf),
    path("note_csv/<int:id>", views.note_csv),

]
