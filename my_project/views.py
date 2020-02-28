# I have created this file - Varsha
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    # get the text
    djtext=request.GET.get('text','default')

    #check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps= request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover=request.GET.get('extraspaceremover', 'off')


    # Check which checkbox is on
    if removepunc=="on":
        analyzed = " "
        punctuations = '''!()-{}[]'";:/?.>,<\@#$%^&*_~`'''
        for char in djtext:
            if char not in punctuations:
               analyzed=analyzed+char
        params={'purpose':'remove punctuation' , 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n":
               analyzed = analyzed + char
        params = {'purpose': 'new line remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index , char in enumerate(djtext):
            if not(djtext[index]=="" and djtext[index+1]==""):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("remove new line")

def spaceremove(request):
    return HttpResponse('remove space <a href="/">back</a>')

def charcount(request):
    return HttpResponse("count character")