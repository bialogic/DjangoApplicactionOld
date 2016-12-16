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
    if request.method == 'POST':
        # request.POST.get()
        # Need to call the cognitive service here.

        #
        text_data = request.POST.get('sent_text')

        return render(request, 'SentimentAnalysis.html', {'sentiment_text':text_data,})






    text_prompt = 'Please enter text here'
    return render(request, 'SentimentAnalysis.html', {'text_prompt':text_prompt})



