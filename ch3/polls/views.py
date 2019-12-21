from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'polls/index.html')
def index2(request):
    return render(request, 'polls/index2.html')
