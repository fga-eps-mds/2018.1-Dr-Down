from django.shortcuts import render

# Create your views here.


def index(request):
    """
        Renders static homepage view
    """

    return render(request, 'homepage/index.html')
