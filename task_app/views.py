from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.


from django.views.generic import View,UpdateView

from task_app.forms import TaskForm

from task_app.models import TaskModel

from django.urls import reverse_lazy

from django.db.models import Q


class TaskAddView(View):

    def get(self,request):
         
         form = TaskForm()
  
         return render(request,"task_add.html",{"form":form})
    
    def post(self,request):
         
           print(request.POST)

           form = TaskForm(request.POST)  #It creates a ****form*** object (TaskForm) and fills it with the data that the user submitted from the HTML form.

           if form.is_valid():
                
                print(form.cleaned_data)

                task = form.save(commit=False)

                task.user = request.user #Assign the logged-in user

                task.save()

                form = TaskForm()
                
                return render(request, "task_add.html", {"form": form})

           

class TaskListView(View):

     def get(self,request):

          task = TaskModel.objects.filter(user = request.user)

          return render(request,"task_list.html",{"task":task})

class TaskUpdateView(UpdateView):

     model = TaskModel

     form_class = TaskForm

     template_name = "update.html"

     success_url =reverse_lazy("home")

     def get_queryset(self):

          return TaskModel.objects.filter(user = self.request.user)
     
     
class TaskDeleteView(View):

     def get(self,request,**kwargs):

          d_id = kwargs.get('pk')

          data = get_object_or_404(TaskModel,id=d_id,user = request.user)

          data.delete()

          return redirect("home")
            
class TaskCompleteView(View):

     def get(self,request,**kwargs):

          c_id =kwargs.get('pk')

          data = get_object_or_404(TaskModel,user = request.user,id = c_id)

          data.is_complete = True

          data.save()

          return redirect("home")

class SearchView(View):

     template_name = "search.html"

     def get(self,request):

          query = request.GET.get('q')

          task = TaskModel.objects.filter(user = request.user)

          if query:

               task = task.filter(Q(priority__icontains = query) | Q(task_name__icontains = query))

          return render(request,self.template_name,{"task":task})