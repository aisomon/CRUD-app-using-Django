from django.shortcuts import render, redirect
from .models import CrudModel

from django.http.response import JsonResponse,HttpResponse,HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")

        sql=CrudModel(name=name,email=email,age=age)
        sql.save()
    return render(request,'index.html')

def viewData(request):
    if request.method == "GET":
        result = CrudModel.objects.all()
        makedictionary={
            "ourdata":result,
        }
        return render(request, 'read.html',context= makedictionary)
    # else:
    #     result = CrudModel.objects.all()
    #     makedictionary={
    #         "ourdata":result,
    #     }
    #     return render(request, 'read.html',context= makedictionary)
    

def editData(request, id):
    if request.method=="GET":
        my_single_data= CrudModel.objects.filter(id=id).values()
        print(my_single_data)
        my_single_data2 = CrudModel.objects.filter(id=id).first()
        print(my_single_data2)
        mydictionary = {
            "single_data":my_single_data2
        }
        return render(request, 'edit.html', context=mydictionary)
    if request.method=="POST":
        new_name = request.POST["name"]
        new_email222 = request.POST["email"]
        new_age4444 = request.POST['age']

        update = CrudModel.objects.filter(id=id).update(name=new_name, email=new_email222, age=new_age4444)

        my_single_data2 = CrudModel.objects.all()
        mydictionary = {
            "single_data": my_single_data2
        }
        return redirect(request, 'read.html', context=mydictionary)
    
def delateData(request, id):
    if request.method=="GET":
        my_single_data = CrudModel.objects.filter(id=id).delete()
        result = CrudModel.objects.all()
        make_dictionary = {
            "our_data": result
        }
        return render(request, 'read.html', context=make_dictionary)

def registration(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username, email, password)
        user.save()

        return JsonResponse({"message":"I am from post."})

# def login(request):
#     if request.method =="GET":
#         return render(request, 'login.html')

#     if request.method =="POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(username=username, password=password)


#         if user is None:
#             return HttpResponseBadRequest({"message":"not valid user"})
#         else:
#             request.session["user_info"] = user.username
#             return JsonResponse({"message":"successfully logged in", "status_code":"200"})