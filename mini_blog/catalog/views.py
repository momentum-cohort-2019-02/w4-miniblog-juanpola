from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, blog/mini_blog/catalog/templates/post_list.html, {})