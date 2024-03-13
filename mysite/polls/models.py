from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.shortcuts import get_object_or_404

class ListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get(self, request):
        user = request.user
        items = ListItem.objects.filter(user=user)
        form = self.form_class()
        context = {
            'items': items,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.content = f"{form.cleaned_data['title']}, {form.cleaned_data['city']}"
            item.save()
        return redirect(reverse('list'))

def delete_item_view(request, item_id):
    item = get_object_or_404(ListItem, id=item_id)
    item.delete()
    return redirect('list')

