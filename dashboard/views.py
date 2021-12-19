from django.shortcuts import render
from.forms import *
from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic

# Create your views here.
def home(request):
     return render(request,'dashboard/home.html')          
def notes(request):
     if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
             notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
             notes.save()
             messages.success(request,f"Notes Added from{request.user.username}Successfully!")    
     else:
          form = NotesForm()
     notes=Notes.objects.filter(user=request.user)
     context={'notes':notes,'form':form}
     return render(request,'dashboard/notes.html',context)
def delete_note(request,pk=None):   
     Notes.objects.get(id=pk).delete()
     return redirect("notes")

class NotesDetailView(generic.DetailView):
     model=Notes 


def add_homework(request):
     if request.method == "POST":
          form = HomeworkForm(request.POST)
          if form.is_valid():
               try:
                    finished = request.POST['is_finished'] 
                    if finished == 'on':
                         finished=True

                    else:
                         finished=False
               except:
                    finished=False
               homework=Homework(
                     user=request.user,
                     subject=request.POST['subject'],
                     title=request.POST['title'],
                     description=request.POST['description'],
                     due=request.POST['due'],
                     is_finished=finished
                       
               )
               homework.save()  
                #messages.success(request,f"Homework Added from{request.user.username}Successfully!") 
     else:
          form = HomeworkForm() 
     homework = Homework.objects.filter(user=request.user)
     if len(homework) == 0:
          homework_done = True
     else: 
          homework_done = False   
     context={ 'homeworks':homework,
               'homeworks_done':homework_done,
               'form':form,}
     return render(request,'dashboard/homework.html', context) 


def update_homework(request,pk=None):
     homework= Homework.objects.get(id=pk)
     if homework.is_finished==True:
          homework.is_finished==False
     else:
          homework.is_finished==True  
     homework.save()
     return redirect("homework")    


def delete_homework(request,pk=None):
     Homework.objects.get(id=pk).delete()
     return redirect("homework")

#todo


def todo(request):
     if request.method == "POST":
          form = TodoForm(request.POST)
          if form.is_valid():
               try:
                    finished = request.POST['is_finished'] 
                    if finished == 'on':
                         finished=True

                    else:
                         finished=False
               except:
                    finished=False
               todos =Todo(
                     user=request.user,
                     title=request.POST['title'],
                     is_finished=finished
                       
               )
               todos.save()  
               #messages.success(request,f"Todo Added from{request.user.username}Successfully!") 
     else:
          form = TodoForm() 
     todo = Todo.objects.filter(user=request.user)
     if len(todo) == 0:
          todo_done = True
     else: 
          todo_done = False 
     context ={
          'form': form,
          'todos':todo,
          'todos_done': todo_done,}
     return render(request,'dashboard/todo.html', context) 


def update_todo(request, pk=None):
     todo= Todo.objects.get(id=pk)
     if todo.is_finished==True:
          todo.is_finished==False
     else:
          todo.is_finished==True  
     todo.save()
     return redirect("todo") 




def delete_todo(request,pk=None):
     Todo.objects.get(id=pk).delete()
     return redirect("todo") 



def register(request):  
     if request.method == "POST":
          form = UserRegistrationForm(request.POST)
          if form.is_valid():                
               form.save() 
               username =form.cleaned_data.get('username')
               #messages.success(request,f"Todo Added from{request.user.username}Successfully!")
               #redirect login

     else:
          form = UserRegistrationForm()
     context ={
               'form': form,
          }
     return render(request,'dashboard/register.html', context) 



def profile (request):
     homework = Homework.objects.filter(user=request.user)
     todo = Todo.objects.filter(user=request.user)
     if len(homework) == 0:
          homework_done = True
     else: 
          homework_done = False
     if len(todo) == 0:
          todo_done = True
     else: 
          todo_done = False 
     context ={
          'homeworks':homework,
          'homeworks_done':homework_done,
          'todos':todo,
          'todos_done': todo_done,} 

     
     return render(request,'dashboard/profile.html', context) 

    


     