# I have created this file and doesn't comes by default with django-admin startproject
import string
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('<h1>Home</h1>')


def contact(request):
    return render(request, 'contact.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    removeNewLine = request.POST.get('removeNewLine', 'off')
    countWords = request.POST.get('countWords', 'off')

    if (removepunc == 'on'):
        analyzed = ""
        punctuations = string.punctuation
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        # Analyse the text
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyzetext.html', params)
    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Text Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyzetext.html', params)
    if (lowercase == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Text Lowercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyzetext.html', params)
    if (removeNewLine == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyzetext.html', params)
    if (countWords == 'on'):
        analyzed = ""
        wordSplit = djtext.split()
        analyzed = len(wordSplit)
        params = {'purpose': 'Words Count', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyzetext.html', params)
    if(removepunc != "on" and lowercase != "on" and removeNewLine != "on" and fullcaps != "on" and countWords != "on"):
        return HttpResponse("Please select any operation and try again")
    return render(request, 'analyzetext.html', params)
