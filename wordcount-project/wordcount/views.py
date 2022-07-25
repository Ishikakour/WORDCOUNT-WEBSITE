from ast import operator
from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist = fulltext.split()
    worddic ={}
    for w in wordlist:
        if w in worddic:
            worddic[w] +=1
        else:
            worddic[w]=1    
    sortedword =sorted(worddic.items(),key =operator.itemgetter(1) , reverse= True)
    
    return render(request,'count.html',{'fulltext': fulltext,'count':len(wordlist),'sortedword':sortedword})

def about(request):
    return render(request,'about.html')
