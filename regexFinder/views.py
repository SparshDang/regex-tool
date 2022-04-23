from django.shortcuts import render
import re

# Create your views here.


def index(request):
    if request.method == 'POST':
        pattern = request.POST.get('regexExpression')
        text = request.POST.get('text')
        matches = list(re.findall(pattern, text))
        print(matches)

        return render(request, 'regexFinder/index.html', {
            'pattern': pattern,
            'text': text,
            'matches': matches
        })

    return render(request, 'regexFinder/index.html')
