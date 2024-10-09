from django.shortcuts import render

# Create your views here.

def index(request ):
    return render(request, 'index.html')
def about(request ):
    return render(request, 'about.html')
def news(request ):
    return render(request, 'news.html')
def issuances(request ):
    return render(request, 'issuances.html')
def qms(request ):
    return render(request, 'qms.html')
def procurement(request ):
    return render(request, 'procurement.html')
def learningresources(request ):
    return render(request, 'learningresources.html')
def research(request ):
    return render(request, 'research.html')
def contact(request ):
    return render(request, 'contact.html')
def q1_view(request):
    return render(request, 'q1.html')
def q2_view(request):
    return render(request, 'q2.html')
def q3_view(request):
    return render(request, 'q3.html')
def q4_view(request):
    return render(request, 'q4.html')

