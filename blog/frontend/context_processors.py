from blog_api.models import Blog


def get_last_blog(request):
    last_blog = Blog.objects.last()
    return {'last_blog': last_blog}
