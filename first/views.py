from django.shortcuts import render
from forms import SignUpForm
from models import Medicament, Localitate
# Create your views here.


def list_medicine(request):
    medicine_list = Medicament.objects.all()
    return render(request, "medicamente.html", {"medicines": medicine_list})


def home(request):
    medicamente_prim = Medicament.objects.all()[:3]
    print(medicamente_prim[0].image.name)
    return render(request,
                  'home.html',
                  {'med': medicamente_prim}
                  )


def meds(request):
    search = request.GET.get('search', None)
    qs_filter = {}
    if search:
        qs_filter['name__icontains'] = search
    medicamente = Medicament.objects.filter(**qs_filter)
    return render(request, 'meds.html', {'medicamente': medicamente})


def drugstore(request):
    locations = Localitate.objects.all()
    return render(request, 'drugstore.html', {'localitati': locations})


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save
            return redirect('/')
    return render(request, 'signup.html', {'form': form})


def login(request):
    return render(request, 'login.html')


def diseases(request):
    return render(request, 'diseases.html')


def blog(request):
    return render(request, 'blog.html')
