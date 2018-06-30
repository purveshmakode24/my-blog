from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from . models import Post , PostForm
from blog.forms import SubmissionForm
import requests

class BlogView(ListView):
    model  = Post
    template_name  =  'blogintro.html'

class DetailBlogView(DetailView):
    model  =  Post 
    template_name = 'detail_blog.html'

def submit(request):
    if request.method == 'POST':

        form  = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.verified = False
            obj.save()
        return render(request , 'aftersubmit.html',{})


    else :
        form = PostForm()
        return render(request   , 'submit.html' , {'form' : form})

def api(request):
    isvalid = False
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            response = requests.post('https://api.judge0.com/submissions?wait=true',
                                     {
                                         "source_code": text,
                                         "language_id": '10'
                                     }

                                     )
            info = response.json()
            isvalid = True

            return render(request , 'test.html' ,{'info':info,  'form' : form , 'isvalid':isvalid})
    else:
        form = SubmissionForm()
        return render(request , 'test.html' ,{'form':form , 'isvalid':isvalid,})