import pytest

from django.urls import reverse, resolve
import polls.views as views

@pytest.mark.django_db
def test_index():
    path = reverse('index')
    assert resolve(path).func == views.index




