from django.shortcuts import render
from django.utils import timezone
from .models import Post
def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts':posts}) # this view is to get the data from database  

# Create your views here.
# the items writting in the views are actions(function) that is need to perform on the data , the data might need to write to data base or to retrive
# from the data base or to delete, update so on , here we have request , in the request we have the data to arrange. 
