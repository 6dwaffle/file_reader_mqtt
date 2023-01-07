from django.shortcuts import render
import csv
import os
#csv reading
file = open('home\\csv\\PhotomFile0.csv','r')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
details = []
for row in csvreader:
        details.append(row)
# Create your views here.
def index(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "header":header,
        'details':details
    }
    # return response with template and context
    return render(request, "index.html", context)