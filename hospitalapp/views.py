from django.shortcuts import render
from .forms import CitaForm

def registro_cita(request):
    form = CitaForm(request.POST or None)
    if request.method == 'POST':  # cuando se envía el formulario
        if form.is_valid():
            form.save()
            return render(request, 'hospitalapp/resultado.html')  # 👈 muestra la página resultado
    # si es GET o hay errores, vuelve a mostrar el formulario
    return render(request, 'hospitalapp/formulario.html', {'form': form})
