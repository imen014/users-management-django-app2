from django.shortcuts import render , get_object_or_404
from model_app.forms import MyModelForm
from model_app.models import Users



def mymodelform1(request):
    myform1 = MyModelForm()
    return render(request,
                  'model_app/form1.html',
                  {'myform1':myform1})

def create_user(request):
    user = MyModelForm()
    user_saved = Users()
    if request.method == "POST":
        user = MyModelForm(request.POST)
        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']
            email = user.cleaned_data['email']
            user_saved.username = username
            user_saved.password = password
            user_saved.email = email
            user_saved.save()
            message = "user saved succefully !"
        else:
            user = MyModelForm()
            message = "user is not valid !"
    else:
        user = MyModelForm()
        message = "method is not post !"
    return render(request,
                  'model_app/form_result.html',
                  {'message':message,
                   'user':user})


def getUsersFromDb(request):
    users = Users.objects.all()
    return render(request,
                  'model_app/get_users.html',
                  {'users':users})

def getUser(request, id):
    user = Users.objects.get(id=id)
    return render(request,
                  'model_app/get_user.html',
                  {'user':user})

def deleteUser(request, id):
    user_to_delete = Users.objects.get(id=id)
    user_to_delete.delete()
    message = "user deleted succeffully !"
    return render(request,
                  'model_app/user_deleted.html',
                  {'user_to_delete':user_to_delete,
                   'message':message})

def update_user(request, id):
    user = get_object_or_404(Users, id=id)
    myform = MyModelForm(instance=user)
    if request.method == "POST":
        myform = MyModelForm(request.POST, instance=user)
        if myform.is_valid():
            myform.save()
            message = "user updated succefully !"
        else:
            message = "form is not valid !"
            myform = MyModelForm(instance=user)
    else:
        message="method is not post"
        myform = MyModelForm(instance=user)

    return render(request,
                  'model_app/modify_user.html',
                  {'myform':myform,
                   'message':message})

