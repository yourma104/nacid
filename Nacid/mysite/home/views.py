from django.shortcuts import render

# Create your views here.
def home(request):
    pagename = "Nacid"
    context = {'pagename': pagename}
    return render(request, 'home/home.html', context)


from django.shortcuts import render

def about(request):
    pagename = "About"
    context = {'pagename': pagename}
    return render(request, 'home/about.html', context)


def contact(request):
    pagename = "Contact"
    context = {'pagename': pagename}
    return render(request, 'home/contact.html', context)


