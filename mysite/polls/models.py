from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.shortcuts import get_object_or_404

class ListItem(models.Model):
    """
    Modèle pour stocker les courses favorites d'un utilisateur.

    Attributs:
        user (ForeignKey): Référence à l'utilisateur Django auth.User qui possède cet élément de liste.
        content (CharField): Le contenu de l'élément de liste, par exemple, le nom de la course.
        created_at (DateTimeField): Date et heure de la création de l'élément, définies automatiquement.

    La logique de gestion des requêtes HTTP (méthodes `get` et `post`) est normalement gérée dans les vues plutôt que dans le modèle.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get(self, request):
        """
        Récupère et affiche les éléments de la liste de l'utilisateur courant.

        Cette méthode est un exemple et devrait idéalement être déplacée dans un fichier views.py.

        Args:
            request: L'objet HttpRequest.

        Returns:
            HttpResponse: Le rendu du template avec la liste des éléments et un formulaire pour en ajouter de nouveaux.
        """
        user = request.user
        items = ListItem.objects.filter(user=user)
        form = self.form_class()
        context = {
            'items': items,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """
        Traite la soumission d'un formulaire pour ajouter un nouvel élément à la liste de l'utilisateur courant.

        Cette méthode est un exemple et devrait idéalement être déplacée dans un fichier views.py.

        Args:
            request: L'objet HttpRequest.

        Returns:
            HttpResponseRedirect: Redirige vers la vue de la liste après l'ajout de l'élément.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.content = f"{form.cleaned_data['title']}, {form.cleaned_data['city']}"
            item.save()
        return redirect(reverse('list'))

def delete_item_view(request, item_id):
    """
    Fonction pour supprimer un élément spécifique de la liste des favoris d'un utilisateur.

    Args:
        request: L'objet HttpRequest.
        item_id: L'ID de l'élément de la liste à supprimer.

    Returns:
        HttpResponseRedirect: Redirige vers la vue de la liste après la suppression de l'élément.
    """
    item = get_object_or_404(ListItem, id=item_id)
    item.delete()
    return redirect('list')

