from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html', {'name':'Gautam'})

# def contact(request):
#     return HttpResponse('<h1>Contact Page</h1> <br> <p>Saharanpur</p>')

def count(request):
    data = request.GET['fulltextarea']
    # print(data)
    word_list = data.split()
    list_length = len(word_list)
    worddictionary = {}
    for word in word_list:
        if word in worddictionary:
            #increase value by one
            worddictionary[word] += 1

        else:
            #add to dictionary value set to 1
            worddictionary[word] = 1
    sorted_list = sorted(worddictionary.items() , key = operator.itemgetter(1))

    return render(request, 'count.html', {'fulltext': data, 'length': list_length ,'worddictionary': sorted_list})

def about(request):
    return render(request , 'about.html')