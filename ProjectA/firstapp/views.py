"""
Application views - urls.py matches incoming requests and then directs them here.
The view then passes the request to the associated HTML page.
Matthew Weaver, 2016.
"""

# pylint: disable=I0011, E0401, C0301
from django.shortcuts import render
from apiclient.discovery import build
import json

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
    sentiment_response = False
    text_data = request.POST.get('sent_text')

    if not text_data:
        text_data = 'I am very happy to meet you. I can only imagine this is a positive sentiment.'

    if text_data:
        api_key = 'AIzaSyB_Ycxdg5aIuJ8HiJTJj3gfIN-i8CguAZ4'
        service = build('language', 'v1', developerKey=api_key)
        sentiment_request = service.documents().analyzeSentiment(
            body={
                'document': {
                    'type': 'PLAIN_TEXT',
                    'content': text_data,
                    },
                }
        )

        sentiment_response = sentiment_request.execute()


        entity_request = service.documents().analyzeEntities(
            body={
                'document': {
                    'type': 'PLAIN_TEXT',
                    'content': text_data,
                    },
                }
        )

        entity_response = entity_request.execute()





    MattUtils.write_json_to_file(r'F:\dev\jsonData.txt', entity_response)
    return render(request, 'SentimentAnalysis.html',
                  {'sentiment_response':sentiment_response, 'text_data':text_data, 'entity_response':entity_response, 'range':range(10)})

def book(request):
    """
    Handles requests for the book page if a match is found in urls.py
    """
    book_response = False
    book_query = request.POST.get('book_query')

    if not book_query:
        book_query = 'Harry Potter'

    #Call the Google books API and return the first matches for the search string
    if book_query:
        api_key = 'AIzaSyA5VkrC_PKDQl_g9qHr_cBU80_PFBumrG8'
        service = build('books', 'v1', developerKey=api_key)
        book_request = service.volumes().list(source='public', q=book_query)
        book_response = book_request.execute()

    MattUtils.write_json_to_file(r'F:\dev\jsonData.txt', book_response)
    return render(request, 'BookQuery.html', {'book_data':book_response, 'book_query': book_query})




#==============================================================
#Needs to be moved to a separate module
#==============================================================
class MattUtils:
    @staticmethod
    def write_json_to_file(filename, data):
        target = open(filename, 'w+')
        target.truncate()
        json.dump(data, target)
        target.close()
        return
