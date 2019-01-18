from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import Blog, ImagesForBlog, CommentsForBlog
from django.core.paginator import Paginator
from .forms import BlogForm,ImagesForBlogForm


def delete_blog(request,blog):
    Blog.objects.get(pk=blog).delete()
    return redirect('main:home')


def delete_image(request,image,blog):
    ImagesForBlog.objects.get(pk=image).delete()
    return redirect('main:editblog', blog)


class Main(View):
    template_name = 'main.html'


    def get(self, request, *args, **kwargs):
        blogs = []
        for blog in Blog.objects.all():
            blogs.append({
                'data': blog,
                'images': ImagesForBlog.objects.filter(blog=blog.id),
            })
        for blog in blogs:
            blog['comments'] = reversed(CommentsForBlog.objects.filter(blog=blog['data'].id))

        page = request.GET.get('page')
        if not page:
            page = 1

        p = Paginator(list(reversed(blogs)), 3)

        return render(request, self.template_name, {
            'page': 'home',
            'title': 'Блог | Главная',
            'blogs': p.page(page),
            'blogForm': BlogForm,
            'imagesForBlogForm': ImagesForBlogForm,
            'pagnav': p.page_range
        })

    def post(self,request, *args, **kwargs):
        if request.POST.get('is_comment', False):
            comment = CommentsForBlog(blog=Blog.objects.get(pk=request.POST['blog']), user=request.user, text=request.POST['text'])
            comment.save()
            return redirect('main:home')
        else:
            blog = Blog(title=request.POST['title'], description=request.POST['description'])
            blog.save()
            if request.FILES:
                for img in request.FILES.keys():
                    image = ImagesForBlog(image=request.FILES[img], blog=blog)
                    image.save()
            return redirect('main:home')

class EditBlog(View):
    template_name = 'blog/edit.html'

    def get(self, request, blog, *args, **kwargs):
        blog = Blog.objects.get(pk=blog)
        return render(request,self.template_name, {
            'title': 'Блог | {}'.format(blog.title),
            'blog': blog,
            'images': ImagesForBlog.objects.filter(blog=blog)
        })

    def post(self, request, blog, *args, **kwargs):
        b = Blog.objects.get(pk=blog)
        b.title = request.POST['title']
        b.description = request.POST['description']
        b.save()
        if request.FILES:
            for img in request.FILES.keys():
                image = ImagesForBlog(image=request.FILES[img], blog=b)
                image.save()
        return redirect('main:home')

