from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    posts = Post.objects.all() #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def get_time(request):
    if request.is_ajax(): 
        time = "ajax"
        import json
        return HttpResponse(json.dumps({'time':time}), 'application/json')
    return render(request, 'blog/post_list.html')



def post_list_test(request, msg):
    result = {}
    result['msg'] = msg
    result['msg1'] = 'aaa'
    result['msg2'] = 'bbb'
    result['arr'] = []
    result['arr'].append('1111')
    result['arr'].append('22222')
    result['arr'].append('3333')
    result['arr'].append('4444')
    result['bool'] = False
    print(result)
    return render(request, 'blog/post_list.html', {'result': result})

