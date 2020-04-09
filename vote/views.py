from django.shortcuts import render, get_object_or_404,redirect
from .models import Questions, Choice
# Create your views here.
def home(request):
    questions = Questions.objects
    return render(request,'home.html',{"questions":questions})

def vote(request, question_id):
    question = get_object_or_404(Questions, pk = question_id)
    return render(request,'vote.html', {'question':question})

def vote_submit(request):
    select_choice_id = request.GET['choice']
    choice = get_object_or_404(Choice,pk = select_choice_id)
    print("출력 출력   ", choice.question.id)
    choice.votes+=1
    choice.save()
    return redirect("/result/" + str(choice.question.id))

def result(request, question_id):
    question = get_object_or_404(Questions,pk = question_id)
    return render(request,'result.html' , {"question" : question})
