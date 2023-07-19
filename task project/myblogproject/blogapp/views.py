from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Blog, Comment
from django.core.mail import send_mail
from django.contrib import messages

from .forms import ShareByEmailForm

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj': page_obj})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    comment_count = comments.count()
    return render(request, 'blog_detail.html', {'blog': blog,'comment_count':comment_count})

def share_post(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.method == 'POST':
        form = ShareByEmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient_email = form.cleaned_data['recipient_email']
            comments = form.cleaned_data['comments']
            
            subject = f"Sharing: {blog.title}"
            from_email = email
            to_email = [recipient_email]
            
            message = f"Hi,\n\n{name} is sharing the blog post '{blog.title}' with you.\n\n"
            message += f"{blog.content}\n\nComments: {comments}\n\nRegards,\n{name}"
            
            send_mail(subject, message, from_email, to_email)
            
            
            messages.success(request, 'The email was sent successfully.')
            
           
            return redirect('share_success')

    else:
        form = ShareByEmailForm()

    return render(request, 'share_post.html', {'blog': blog, 'form': form})

def share_success(request):
    return render(request, 'share_success.html', )

def add_comment(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=blog_id)
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            body = request.POST.get('body')
            if name and email and body:  # Basic form validation
                comment = Comment(blog=blog, name=name, email=email, body=body)
                comment.save()
            
    return redirect('detail', blog_id=blog_id)

def like_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        user = request.user
        comment.likes.add(user)
    return redirect('detail', blog_id=comment.blog.id)