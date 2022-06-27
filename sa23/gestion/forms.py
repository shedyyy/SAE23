from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class EtudiantForm(ModelForm):

    class Meta:
        model = models.Etudiant
        fields = ('nom','prenom','groupe','groupe','photo','email')
        labels = {
            'nom' : _('Nom') ,
            'prenom ': _('prenom '),
            'groupe': _('groupe'),
            'photo': _('photo'),
            'email': _('email'),
        }
class ExamensForm(ModelForm):

    class Meta:
        model = models.Examens
        fields = ('coefficient','date','titre','ressources')
        labels = {

            'coefficient': _('coefficient'),
            'date': _('date'),
            'titre': _('titre'),
            'ressources': _('ressources'),
        }
        localized_fields = ('date',)



class NotesForm(ModelForm):

    class Meta:
        model = models.Notes
        fields = ('examens','etudiant','note','appreciation')
        labels = {
            'examens' : _('examens') ,
            'etudiant': _('etudiant'),
            'note': _('note'),
            'appreciation': _('appreciation'),
        }





class UniteForm(ModelForm):

    class Meta:
        model = models.UE
        fields = ('code','nom','semestre','credit')
        labels = {
            'code' : _('code'),
            'nom': _('nom'),
            'semestre': _('semestre'),
            'credit': _('credit'),
        }


class RessourcesForm(ModelForm):

    class Meta:
        model = models.Ressources
        fields = ('code_ressource','nom','descriptif','coefficient','competence')
        labels = {
            'code_ressource' : _('code ressource'),
            'nom': _('nom'),
            'descriptif': _('descriptif'),
            'coefficient': _('coefficient'),
            'competence': _('competence'),

        }

class EnseignantForm(ModelForm):

    class Meta:
        model = models.Enseignant
        fields = ('nom','prenom',)
        labels = {
            'nom': _('nom'),
            'prenom': _('prenom'),
        }
