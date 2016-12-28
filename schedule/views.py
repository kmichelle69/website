from .forms import NameForm
from django.shortcuts import render, redirect
from django.views.generic import FormView

def NewRepair(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NameForm()
    return render(request, 'new_repair.html', {'form': form})

class schedule(FormView):
    template_name = 'new_repair.html'
    form_class = 'NameForm'
