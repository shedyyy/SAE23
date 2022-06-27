from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect ,HttpResponse
from .forms import EtudiantForm
from .forms import ExamensForm
from .forms import NotesForm
from fpdf import FPDF
from .forms import UniteForm
from .forms import RessourcesForm
from .forms import EnseignantForm
from django.http import FileResponse
from django.shortcuts import render
import csv



def etudiant(request):
    #etudiants = models.Etudiant.objects.get(pk=id)
    liste_etu = list(models.Etudiant.objects.all())
    #notes = list(models.Notes.objects.filter(etudiant=etudiants))
   # moyenne = 0
    #for i in notes:
    #  moyenne = moyenne + i.note
  # etudiant.moyenne = str(round((moyenne / len(notes)) * 100, 2)) + "%"

    return render(request, 'gestion/etudiant.html', {'liste_etu':liste_etu,})#'etudiants': etudiants,'notes': notes,"etudiant.moyenne":etudiant.moyenne

def home(request):
    liste = list(models.Etudiant.objects.all())
    liste2 = list(models.UE.objects.all())
    liste3 = list(models.Ressources.objects.all())
    liste4 = list(models.Enseignant.objects.all())
    return render(request,'gestion/home.html',{'liste': liste, 'liste2': liste2,'liste3': liste3,'liste4': liste4,})

def ajout(request):
    if request.method == "POST":
        form = EtudiantForm(request)
        if form.is_valid():
            etudiant = form.save()
            return render(request,"/gestion/affiche.html",{"etudiant" : etudiant})
        else:
            return render(request,"gestion/ajout.html",{"form": form})
    else :
        form = EtudiantForm()
        return render(request,"gestion/ajout.html",{"form" : form})

def traitement(request):
    form = EtudiantForm(request.POST, request.FILES)
    if form.is_valid():
        etudiant = form.save()
        return HttpResponseRedirect("/gestion/home")
    else:
        return render(request,"gestion/ajout.html",{"form": form})

# id = id d'un étudiant
def affiche(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    notes = list(models.Notes.objects.filter(etudiant=etudiant))
    moyenne = 0.0
    coeff = 0.0
    for i in notes:
        examen = models.Examens.objects.get(id=i.examens.id)

        moyenne = moyenne + i.note * float(examen.coefficient)
        coeff = coeff + float(examen.coefficient)
        print(f'{i.note} / {examen.coefficient}')

    if coeff != 0:
        moyenne = round(moyenne/coeff,2)
        print(f'{moyenne}')
    return render(request,"gestion/affiche.html",{'etudiants': etudiant,'notes': notes,"moyenne":moyenne,"examen": examen,"coefff":examen.coefficient,"coeff":coeff})



def update(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    eform = EtudiantForm(etudiant.dico())
    return render(request,"gestion/update.html",{"eform": eform,"id":id})

def traitementupdate(request, id):
    eform = EtudiantForm(request.POST, request.FILES)
    if eform.is_valid():
        etudiant = eform.save(commit=False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("/gestion/home/")
    else:
        return render(request,"gestion/update.html",{"eform": eform, "id": id})


def delete(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/gestion/etudiant/")





def examens(request):
    liste1 = list(models.Examens.objects.all())
    liste2 = list(models.Ressources.objects.all())
    return render(request,'gestion/examens.html',{'liste1': liste1,'liste2': liste2,})

def ajout_exa(request):
    if request.method == "POST":
        form = ExamensForm(request.POST)
        if form.is_valid():
            examens = form.save(commit=False)
            examens.save()
            return HttpResponseRedirect("/gestion/home/")

        else:
            return render(request,"gestion/ajout_exa.html",{"form": form})
    else:
        form = ExamensForm()
        return render(request,"gestion/ajout_exa.html",{"form": form})


def traitement_exa(request):
    form = ExamensForm(request.POST)
    ressources = models.Ressources.objects.get(pk=id)
    if form.is_valid():

        examens = form.save(commit=False)

        examens.ressources = ressources
        examens.ressoruces_id = id
        examens.save()
        return HttpResponseRedirect("/gestion/home/"+ str(id))
    else:
        return render(request,"gestion/ajout_exa.html",{"form": form})

def affiche_exa(request, id):
    examens = models.Examens.objects.get(pk=id)
    liste1 = list(models.Notes.objects.filter(examens=examens))
    return render(request,"gestion/affiche_exa.html",{"examens": examens ,"liste1":liste1})

def update_exa(request, id):
    examens = models.Examens.objects.get(pk=id)
    exform = ExamensForm(examens.dico())
    return render(request,"gestion/update_exa.html",{"exform": exform,"id":id})

def traitementupdate_exa(request, id):
    exform = ExamensForm(request.POST, request.FILES)
    if exform.is_valid():
        examens = exform.save(commit=False)
        examens.id = id
        examens.save()
        return HttpResponseRedirect("/gestion/examens")
    else:
        return render(request,"gestion/update_exa.html",{"exform": exform, "id": id})

def delete_exa(request, id):
    examens = models.Examens.objects.get(pk=id)
    examens_id = examens.ressources_id
    examens.delete()
    return HttpResponseRedirect(f"/gestion/affiche_res/{examens_id}")

def note(request):
    liste_note = list(models.Notes.objects.all())
    return render(request,'note/note.html',{'liste_note': liste_note})

def ajout_note(request):
    if request.method == "POST":

        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return HttpResponseRedirect("/gestion/home/")

        else:
            return render(request,"note/ajout_note.html",{"form": form})
    else :
        form = NotesForm()
        return render(request,"note/ajout_note.html",{"form" : form})

def traitement_note(request):
    form = NotesForm(request.POST, request.FILES)
    #examens = models.Examens.objects.get(pk=id)
    if form.is_valid():
        note = form.save(commit=False)
        #note.examens = examens
        #note.examens_id = id
        note.save()
        return HttpResponseRedirect("/gestion/note")
    else:
        return render(request,"note/ajout_note.html",{"form": form})

def affiche_note(request, id):
    note = models.Notes.objects.get(pk=id)
    return render(request,"note/affiche_note.html",{"note": note})

def update_note(request, id):
    note = models.Notes.objects.get(pk=id)
    nform = NotesForm(note.dico())
    return render(request,"note/update_note.html",{"nform": nform,"id":id})

def traitementupdate_note(request, id):
    nform = NotesForm(request.POST, request.FILES)
    if nform.is_valid():
        note = nform.save(commit=False)
        note.id = id
        note.save()
        return HttpResponseRedirect("/gestion/home/")
    else:
        return render(request,"note/update_note.html",{"nform": nform, "id": id})


def delete_note(request, id):
    note = models.Notes.objects.get(pk=id)
    note.delete()
    return HttpResponseRedirect("/gestion/note")




#############################################

def UE(request):
    UE =  list(models.UE.objects.all())
    return render(request,"gestion/UE.html",{"UE": UE})



def aUnite(request):
    if request.method == "POST":
        form = UniteForm(request.POST)
        if form.is_valid():
            UE = form.save(commit=False)
            UE.save()
            return HttpResponseRedirect("/gestion/home/" ,{"UE": UE})

        else:
            return render(request,"gestion/aUnite.html",{"form": form})
    else:
        form = UniteForm()
        return render(request,"gestion/aUnite.html",{"form": form})

def tUnite(request):
    form = UniteForm(request.POST, request.FILES)
    if form.is_valid():
        UE = form.save()
        return HttpResponseRedirect("/gestion/home")
    else:
        return render(request,"gestion/aUnite.html",{"form": form})

def UEupdate(request, id):
    UE = models.UE.objects.get(pk=id)
    form = UniteForm(UE.dico())
    return render(request,"gestion/UEupdate.html",{"form": form,"id":id})

def tuUE(request, id):
    eform = UniteForm(request.POST, request.FILES)
    if eform.is_valid():
        UE = eform.save(commit=False)
        UE.id = id
        UE.save()
        return HttpResponseRedirect("/gestion/home")
    else:
        return render(request,"gestion/UEupdate.html",{"eform": eform, "id": id})

def affiche_ue(request, id):
    UE = models.UE.objects.get(pk=id)
    ressources = list(models.Ressources.objects.filter(competence=UE))
    return render(request,"gestion/affiche_ue.html",{'UE': UE,'ressources':ressources})


def delUE(request, id):
    UE = models.UE.objects.get(pk=id)
    UE.delete()
    return HttpResponseRedirect("/gestion/home")

def ressourcess(request):
    return render(request,"gestion/ressources.html")

def ajoutressources(request):
    if request.method == "POST":
        form = RessourcesForm(request)
        if form.is_valid():
            ressources = form.save()
            return render(request,"/gestion/affiche_res.html",{"ressources": ressources})
        else:
            return render(request,"gestion/ajoutressources.html",{"form": form})
    else:
        form = RessourcesForm()
        return render(request,"gestion/ajoutressources.html",{"form": form})

def traitementressources(request):
    form = RessourcesForm(request.POST, request.FILES)
    if form.is_valid():
        ressources = form.save()
        return HttpResponseRedirect("/gestion/home")
    else:
        return render(request,"gestion/ajoutressources.html",{"form": form})

def updateressources(request, id):
    ressources = models.Ressources.objects.get(pk=id)
    rform = RessourcesForm(ressources.dico())
    return render(request,"gestion/updateressources.html",{"ressources": ressources,"rform": rform,"id":id})

def traitementupdateressources(request, id):
    rform = RessourcesForm(request.POST, request.FILES)
    if rform.is_valid():
        ressources = rform.save(commit=False)
        ressources.id = id
        ressources.save()
        return HttpResponseRedirect("/gestion/home")
    else:
        return render(request,"gestion/updateressources.html",{"rform": rform, "id": id})

def affiche_res(request, id):
    ressources = models.Ressources.objects.get(pk=id)
    liste7 = list(models.Examens.objects.filter(ressources=ressources))
    return render(request,"gestion/affiche_res.html",{"ressources": ressources,"liste7": liste7})

def deleteressources(request, id):
    ressources = models.Ressources.objects.get(pk=id)
    ressources.delete()
    return HttpResponseRedirect("/gestion/home/")

def enseignant(request):
    return render(request,"gestion/enseignant.html")

def ajoutenseignant(request):
    if request.method == "POST":

        form = EnseignantForm(request)
        if form.is_valid():
            enseignant = form.save()
            return render(request,"/gestion/affiche.html",{"enseignant": enseignant})

        else:
            return render(request,"gestion/ajoutenseignant.html",{"form": form})
    else:
        form = EnseignantForm()
        return render(request,"gestion/ajoutenseignant.html",{"form": form})

def traitementenseignant(request):
    form = EnseignantForm(request.POST, request.FILES)
    if form.is_valid():
        enseignant = form.save()
        return HttpResponseRedirect("/gestion/home")
    else:
        return render(request,"gestion/ajoutenseignant.html",{"form": form})

def updateenseignant(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    lform = EnseignantForm(enseignant.dico())
    return render(request,"gestion/updateenseignant.html",{"lform": lform,"id":id})

def traitementupdateenseignant(request, id):
    lform = EnseignantForm(request.POST, request.FILES)
    if lform.is_valid():
        enseignant = lform.save(commit=False)
        enseignant.id = id
        enseignant.save()
        return HttpResponseRedirect("/gestion/home/")
    else:
        return render(request,"gestion/updateenseignant.html",{"lform": lform, "id": id})

def deleteenseignant(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    enseignant.delete()
    return HttpResponseRedirect("/gestion/home")

def notes_pdf(request ,id):
    etudiant = models.Etudiant.objects.get(pk=id)
    notes = list(models.Notes.objects.filter(etudiant=etudiant))
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=16)
    moyenne = 0.0
    coeff = 0.0
    pdf.cell(200, 10, txt="Relever de note", ln=2, align='C')
    pdf.cell(200, 10, txt="Nom de l'etudiant "+ str(etudiant.nom),ln=2, align='C')
    for i in notes:
        examen = models.Examens.objects.get(id=i.examens.id)
        moyenne = moyenne + i.note * float(examen.coefficient)
        coeff = coeff + float(examen.coefficient)
        print(f'{i.note} / {examen.coefficient}')
        pdf.cell(200, 10, txt=f"note  {str(i.note)}", ln=2, align='C')
    if coeff != 0:
        moyenne = round(moyenne/coeff,2)
        print(f'{moyenne}')
    pdf.cell(200, 10, txt="Moyenne" + str(moyenne), ln=2, align='C')
    pdf.output('Note.pdf')
    response = FileResponse(open("Note.pdf"))
    return response




def note_csv(request,id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Dispostion'] = 'attachment; filename=note_csv.csv'

    writer = csv.writer(response)

    note = models.Notes.objects.all()

    writer.writerow(['examens','etudiant','note','appreciation'])


    for note in note:
        writer.writerow([note.etudiant,note.examens,note.note,note.appreciation])

    return response