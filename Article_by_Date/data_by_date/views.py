from django.shortcuts import render,redirect
from .forms import data
from .models import article
from django.contrib import messages
# Create your views here.
def main(request):
    return render(request, 'main.html')

 # Import the model class

def main(request):
    if request.method == 'POST':
        form = data(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'article submitted successfully!')
            return redirect('main') 
            
    else:
        form = data()
    return render(request, 'main.html', {'form': form})




def view_article(request):
    return render(request, 'view_article.html')



# views.py
from django.http import JsonResponse
from .models import article

def fetch_articles(request):
    date = request.GET.get('date')
    articles = article.objects.filter(date=date)
    # Process articles as needed
    # Return JSON response or HTML fragment
    articles_data = [
        {'title': article.name, 'content': article.description}  # Example fields
        for article in articles
    ]
    return JsonResponse({'articles': articles_data})
