from django.shortcuts import render

def index(request):
    title = "POLICE OFFENCE RECORDS"
    template = 'index.html'

    context = {
        'title':title
    }
    return render(request, template, context)