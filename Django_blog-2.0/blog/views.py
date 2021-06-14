from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post,Form
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

def knot_home(request):
    
    if request.method == 'POST':
            if request.POST.get('contact') and request.POST.get('fname') and  request.POST.get('lname') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('iname') and request.POST.get('comment'):
                post=Form()
                post.contact= request.POST.get('contact')
                post.fname= request.POST.get('fname')
                post.lname= request.POST.get('lname')
                post.email= request.POST.get('email')
                post.phone= request.POST.get('phone')
                post.iname= request.POST.get('iname')
                post.comment= request.POST.get('comment')
                post.save()
                return render(request,'knot_home.html')
                  

            else:
                return render(request,'knot_home.html')
    else:
            return render(request,'knot_home.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'



def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

# def form(request):
   # if request.method == 'POST':
   #         if request.POST.get('contact') and request.POST.get('fname') and  request.POST.get('lname') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('iname') and request.POST.get('comment'):
    #            post=Post()
     #           post.contact= request.POST.get('contact')
      #          post.fname= request.POST.get('fname')
       #         post.lname= request.POST.get('lname')
        #        post.email= request.POST.get('email')
         #       post.phone= request.POST.get('phone')
          #      post.iname= request.POST.get('iname')
           #     post.comment= request.POST.get('comment')
            #    post.save()
             #   return render(request,'form.html',{'post': post})
                  

         #   else:
          #      return render(request,'form.html',{'post': post})




     