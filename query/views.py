from django.shortcuts import render
from .models import Asked

# Create your views here.
def ask_world(request):
    if request.method =="POST":
        owner=request.POST["owner"]
        title=request.POST['title']
        question=request.POST['question']

        new_question=Asked(owner=owner,title=title,question=question)
        new_question.save()

    return render(request, "query.html", {})