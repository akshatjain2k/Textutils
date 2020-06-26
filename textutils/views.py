# i have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def about(request):   
    return HttpResponse("ohh yess")    

def analyze(request):
    dtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newline=request.POST.get('newline', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charcount=request.POST.get('charcount', 'off')
    none=request.POST.get('none', 'off')

    if (removepunc == "on"):
        punctuations = '''{}[](),.!@#:;'"/?\$%'''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations', 'analyzed_text':analyzed}
        dtext = analyzed
#        return render(request, 'analyze.html', params)     
      
    if(fullcaps=="on"):
        analyzed = ""
        for char in dtext:
             analyzed = analyzed + char.upper()
        params = {'purpose':'Capatalised Text', 'analyzed_text':analyzed}
        dtext = analyzed
#        return render(request, 'analyze.html', params)   

    if(newline=="on"):
        analyzed = ""
        for char in dtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'New line Remover', 'analyzed_text':analyzed}
        dtext = analyzed
#        return render(request, 'analyze.html', params)     
    
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(dtext):
            if not(dtext[index] == " " and dtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover', 'analyzed_text':analyzed}
#        dtext = analyzed
#        return render(request, 'analyze.html', params)     

    if(removepunc!="on")and(fullcaps!="on")and(newline!="on")and(extraspaceremover!="on"):
        return HttpResponse("Error")


    return render(request, 'analyze.html', params)     
        


