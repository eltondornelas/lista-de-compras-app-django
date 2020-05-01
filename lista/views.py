from django.shortcuts import render
from django.views.generic.list import ListView


class ListaIndex(ListView):

    def get(self, *args, **kwargs):
        return render(self.request, 'lista/index.html')
