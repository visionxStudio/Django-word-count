from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')



def count(request):
    if(request.method == "POST"):
        data = request.POST.copy()
        fullText = data.get('fulltext')
        # splitting the text wtih the spaces
        wordlist = fullText.split(' ')
        sum = 0
        for i in wordlist : 
            for j in i:
                sum = len(j) + sum
        
        return render(request, 'count.html', {'count': len(wordlist), 'originalText': fullText, 'totalLetters': sum})
    else: 
        return render(request, 'index.html')
    