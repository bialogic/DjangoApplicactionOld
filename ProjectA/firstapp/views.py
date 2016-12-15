"""
Application views - urls.py matches incoming requests and then directs them here.
The view then passes the request to the associated HTML page.
Matthew Weaver, 2016.
"""

from django.shortcuts import render

def home(request):
    """
    Handles requests for the home page if a match is found in urls.py
    """
    return render(request, 'home.html')

def about(request):
    """
    Handles requests for the about page if a match is found in urls.py
    """
    return render(request, 'about.html')

def sentiment(request):
    """
    Handles requests for the sentiment analysis page if a match is found in urls.py
    """
    return render(request, 'SentimentAnalysis.html')



