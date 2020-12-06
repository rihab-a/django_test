from django.shortcuts import render

# Create your views here.

posts = [
{
'author': 'Mohamed Jallouli',
'title': 'Computer science',
'review': 'This engineer is okay.',
'date_posted': 'December 6, 2020',
},
{
'author': 'Rihab Ammary',
'title': 'Electronics and communication',
'review': 'This engineer is excelent',
'date_posted': 'December 6, 2020', 
}]
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'reviews/home.html', context)
def about(request):
    return render(request, 'reviews/about.html', {'title':'about'})