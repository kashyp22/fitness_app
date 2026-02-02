from datetime import datetime

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

# Create your views here.
from myapp.models import *


def logins(request):
    return render(request, 'admin/login_index.html')
def logout(request):
    return render(request, 'admin/login_index.html')

#
# def viewfeedback(request):
#     return render(request,'admin/vi.html')

def login_get(request):
    username=request.POST["username"]
    password=request.POST["pass"]
    user = authenticate(request,username=username,password=password)
    if user is not None:
        if user.groups.filter(name="Admin").exists():
            login(request,user)
            return redirect('/myapp/admin_home/')
        elif user.groups.filter(name="Trainer").exists():
            print("hhhhhhhhhhhhhhhhhhhhhhhhh")
            login(request,user)
            return redirect('/myapp/trainerindex/')
        else:
            return redirect('/myapp/loginindex/')
    return render(request,'admin/login_index.html')

#=====================================================================
#============================ADMIN====================================
#=====================================================================

def admin_home(request):
    return render(request, 'admin/admin_index.html')

def add_service_plan(request):
    return render(request, 'admin/add_service_plan.html')
def add_service_plan_post(request):
    servicename=request.POST['service']
    details=request.POST['details']
    fee=request.POST['Fee']
    a=service()
    a.service_name=servicename
    a.details=details
    a.fee=fee
    a.save()
    return redirect('/myapp/view_service_plans/')

def edit_service_plan(request,id):
    request.session['id']=id
    a=service.objects.get(id=id)
    return render(request, 'admin/edit_service_plan.html',{'data':a})

def edit_service_plan_post(request):
    servicename = request.POST['service']
    details = request.POST['details']
    fee = request.POST['Fee']
    a = service.objects.get(id=request.session['id'])
    a.service_name = servicename
    a.details = details
    a.fee = fee
    a.save()
    return redirect('/myapp/view_service_plans/')

def delete_service_plan(request,id):
    a=service.objects.get(id=id)
    a.delete()

    return redirect('/myapp/view_service_plans/')


def add_trainer(request):

    return render(request, 'admin/add_trainer.html')
def add_trainer_post(request):
    name=request.POST['name']
    email=request.POST['email']
    contact=request.POST['contact']
    qualification=request.POST['qualification']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    username=request.POST['username']
    password=request.POST['password']

    obj=User.objects.create_user(username=username,password=password,email=email,first_name=password)
    obj.save()
    obj.groups.add(Group.objects.get(name='Trainer'))
    b=trainer()
    b.name=name
    b.LOGIN=obj
    b.email=email
    b.phone=contact
    b.qualification=qualification
    b.place=place
    b.post=post
    b.pin=pin
    b.username=username
    b.password=password
    b.save()
    return redirect('/myapp/add_trainer/')

def edit_trainer(request,id):
    request.session['id']=id
    a=trainer.objects.get(id=id)
    return render(request, 'admin/edit_trainer.html',{'data':a})


def edit_trainer_post(request):
    name=request.POST['name']
    email=request.POST['email']
    contact=request.POST['contact']
    qualification=request.POST['qualification']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']

    b =trainer.objects.get(id=request.session['id'])
    b.name = name
    b.email = email
    b.phone = contact
    b.qualification = qualification
    b.place = place
    b.post = post
    b.pin = pin
    b.save()
    return redirect('/myapp/view_trainer/')

def edit_entiquette(request,id):
    request.session['id']=id
    a=entiquette.objects.get(id=id)
    return render(request, 'admin/edit_entiquette.html',{'data':a})



def edit_entiquette_post(request):
    rules=request.POST['rule']
    punishment=request.POST['punishment']

    b =entiquette.objects.get(id=request.session['id'])
    b.rules = rules
    b.punishment = punishment
    b.save()
    return redirect('/myapp/view_entiquette/')


def delete_trainer(request,id):
    a=trainer.objects.get(id=id)
    a.delete()
    return redirect('/myapp/view_trainer/')


def add_video(request):
    return render(request, 'admin/add_video.html')
def add_video_post(request):
    video=request.FILES['video']
    description=request.POST['description']
    c=workout_video()
    c.video=video
    c.description=description
    c.save()
    return redirect('/myapp/add_video/')


def delete_workout_video(request,id):
    workout_video.objects.filter(id=id).delete()
    return redirect('/myapp/view_workout_video/')

def assign_trainers(request):
    return render(request,'admin/assign_trainer.html')

def assign_trainer_post(request):
  from_time=request.POST['from_time']
  to_time=request.POST['to_time']
  day=request.POST['day']
  date=request.POST['date']
  trainers=request.session['tid']
  g=assign_trainer()
  g.from_time=from_time
  g.to_time=to_time
  g.day=day
  g.date=date
  g.TRAINER=trainer.objects.get(id=trainers)
  g.save()
  return redirect('/myapp/view_assigned_trainer/{trainers}')

def change_password(request):
    return render(request, 'admin/change_password.html')
def change_password_post(request):
    password = request.POST['current_password']
    password=request.POST['new password']
    password = request.POST['confirm password']
    d=password()
    d.password=password
    return redirect('/myapp/change_password/')


def send_reply(request):
    return render(request, 'admin/send_reply.html')
def send_reply_post(request):
    reply=request.POST['reply']
    e=reply()
    e.reply=reply
    e.save()
    return redirect('/myapp/send_reply/')

def view_assigned_trainer(request,id):
    request.session['tid']=id
    ab=assign_trainer.objects.all()
    return render(request, 'admin/view_assigned_trainer.html',{'data':ab})

def view_complaint(request):
    return render(request, 'admin/view_complaint.html')

def view_review(request):
    return render(request, 'admin/view_review.html')

def view_user(request):
    return render(request, 'admin/view_user.html')

def view_trainer(request):
    ab=trainer.objects.all()
    return render(request, 'admin/view_trainer.html',{'trainers':ab})

def view_service_plans(request):
    a=service.objects.all()
    return render(request, 'admin/view_service_plans.html',{'data':a})

def view_workout_plan(request):
    return render(request, 'admin/view_workout_plan.html')

def view_workout_video(request):
    a=workout_video.objects.all()
    return render(request, 'admin/view_workout_video.html',{"data":a})

def add_entiquette(request):
    return render(request, 'admin/add_entiquette.html')
def add_entiquette_post(request):
    rule=request.POST['rule']
    punishment=request.POST['punishment']
    f=entiquette()
    f.rules=rule
    f.punishment=punishment
    f.date=datetime.now()
    f.save()
    return redirect('/myapp/add_entiquette/')
def view_entiquette(request):
    a=entiquette.objects.all()
    return render(request, 'admin/view_entiquette.html',{"data":a})


def edit_assign_trainers(request):
    return render(request,'admin/assign_trainer.html')

def edit_assign_trainer_post(request):
  from_time=request.POST['from_time']
  to_time=request.POST['to_time']
  day=request.POST['day']
  trainers=request.session['tid']
  g=assign_trainer()
  g.from_time=from_time
  g.to_time=to_time
  g.day=day
  g.TRAINER=trainer.objects.get(id=trainers)
  g.save()
  return redirect('/myapp/view_assigned_trainer/{trainers}')



def delete_entiquette(request,id):
    entiquette.objects.filter(id=id).delete()
    return redirect('/myapp/view_entiquette/')



#########################trainer#########################



from django.shortcuts import render,redirect
from django.contrib.auth import update_session_auth_hash
from .models import *


#trainer views

def trainerindex(request):
    return render(request,'trainer/trainer_index.html')


def trainer_login_index(request):
    return render(request,'trainer/trainer_login_index.html')


def add_diet_plan(request):
    return render(request,'trainer/add_diet_plan.html')

def add_diet_plan_post(request):
  Date=request.POST['Date']
  Day_shift=request.POST['Day_shift']
  Plan_Name=request.POST['Plan_Name']
  category_type=request.POST['category_type']
  discription=request.POST['discription']
  duration=request.POST['duration']
  target_goal =request.POST['target_goal']
  g=diet_plan()
  g.Date=Date
  g.Day_shift=Day_shift
  g.Plan_Name=Plan_Name
  g.category_type=category_type
  g.discription=discription
  g.duration=duration
  g.target_goal=target_goal
  g.TRAINER=trainer.objects.get(LOGIN_id=request.user.id)
  g.save()
  return redirect('/myapp/add_diet_plan/')


def add_motivational_video(request):
    return render(request,'trainer/add_motivational_video.html')


def add_motivational_video_post(request):
  Video=request.FILES['Video']
  Title=request.POST['Title']
  g=motivated_video()
  g.video=Video
  g.title=Title
  g.date=datetime.now().today()
  g.TRAINER=trainer.objects.get(LOGIN_id=request.user.id)
  g.save()
  return redirect('/myapp/view_motivatioal_video/')




def delete_video(request,id):
    a=motivated_video.objects.get(id=id)
    a.delete()

    return redirect('/myapp/view_motivatioal_video/')



def view_tips(request):
    ab=tip.objects.filter(TRAINER__LOGIN_id=request.user.id)
    return render(request,'trainer/view_tips.html',{'data':ab})

def delete_tips(request,id):
    a=tip.objects.get(id=id)
    a.delete()

    return redirect('/myapp/view_tips/')


def add_tips(request):
    return render(request,'trainer/add_tips.html')


def add_tips_post(request):
    Title = request.POST['Title']
    Description=request.POST['Description']
    a=tip()
    a.title=Title
    a.date=datetime.now().today()
    a.description=Description
    a.TRAINER=trainer.objects.get(LOGIN_id=request.user.id)
    a.save()
    return redirect('/myapp/view_tips/')


def add_workoutplan(request):
    return render(request,'trainer/add_workoutplan.html')

def add_workoutplan_post(request):
    Date=request.POST['Date']
    Plan_Name=request.POST['Plan_Name']
    Video=request.POST['Video']
    Details=request.POST['Details']
    a=add_workoutplan()
    a.Date=Date
    a.Plan_Name=Plan_Name
    a.Video=Video
    a.Details=Details
    a.TRAINER=trainer.objects.get(id=trainer)
    a.save()
    return redirect('trainer/add_workoutplan/{trainer}')


def change_password(request):
    return render(request,'trainer/change_password.html')

def change_password_POST(request):
    Current_Password=request.POST['Current_Password']
    New_Password=request.POST['New_Password']
    Confirm_Password=request.POST['Confirm_Password']
    a=change_password()
    a.Current_Password=Current_Password
    a.New_Password=New_Password
    a.Confirm_Password=Confirm_Password
    a.TRAINER = trainer.objects.get(id=trainer)
    a.save()
    return redirect('trainer/change_password/{trainer}')



def edit_diet_plan(request):
    return render(request,'trainer/edit_diet_plan.html')

def edit_diet_plan_POST(request):
    Date = request.POST['Date']
    Day_shift = request.POST['Day_shift']
    Plan_Name = request.POST['Plan_Name']
    category_type = request.POST['category_type']
    discription = request.POST['discription']
    duration = request.POST['duration']
    target_goal = request.POST['target_goal ']
    g = edit_diet_plan()
    g.Date = Date
    g.Day_shift = Day_shift
    g.Plan_Name = Plan_Name
    g.category_type = category_type
    g.discription = discription
    g.duration = duration
    g.target_goal = target_goal
    g.TRAINER = trainer.objects.get(id=trainer)
    g.save()
    return redirect('/myapp/edit_diet_plan/{trainer}')


def edit_tips(request,id):
    request.session['tid']=id
    d=tip.objects.get(id=id)
    return render(request,'trainer/edit_tips.html',{'data':d})


def edit_tips_post(request):
    Title = request.POST['Title']
    Description=request.POST['Description']
    a=tip.objects.get(id=request.session['tid'])
    a.title=Title
    a.description=Description
    a.date=datetime.now().today()
    a.TRAINER=trainer.objects.get(LOGIN_id=request.user.id)
    a.save()
    return redirect('/myapp/view_tips/')


def view_accepted_request(request):
    return render(request,'trainer/view_accepted_request.html')


def view_assign(request):
    a=assign_trainer.objects.all()
    return render(request,'trainer/view_assign.html',{'data':a})

def view_diet_plan(request):
    ab=diet_plan.objects.all()
    return render(request,'trainer/view_diet_plan.html')

def view_fee_alert(request):
    return render(request,'trainer/view_fee_alert.html')

def view_gym_entiquette(request):
    a=entiquette.objects.all()
    return render(request,'trainer/view_gym_entiquette.html',{'data':a})

def view_motivatioal_video(request):
    ab=motivated_video.objects.filter(TRAINER__LOGIN_id=request.user.id)
    return render(request,'trainer/view_motivatioal_video.html',{'data':ab})

def view_profile(request):
    t=trainer.objects.get(LOGIN=request.user.id)
    return render(request,'trainer/view_profile.html',{'data':t})

def view_serviceplan(request):
    ab=service.objects.all()
    return render(request,'trainer/view_serviceplan.html',{'data':ab})


def view_user_request(request):
    return render(request,'trainer/view_user_request.html')

def view_user_serviceplan(request):
    ab=view_user_serviceplan.objects.all()
    return render(request, 'trainer/view_user_serviceplan.html')

def view_workoutplan(request):
    return render(request,'trainer/view_workoutplan.html')





##########################################flutter

def flutter_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.groups.filter(name="user").exists():
                return JsonResponse({"task": "valid","type": "user", "lid: user.id"})
            return JsonResponse({"task": "valid","type": "other", "lid: user.id"})
        return JsonResponse({"task": "invalid"})
    return JsonResponse({"task": "error", "message": "POST required"})




def user_view_trainers(request):
    l=[]
    a=trainer.objects.all()
    for i in a:
        l.append({
            'id':str(i.id),
            'name':str(i.name),
            'phone':str(i.phone),
            'email':str(i.email),
            'qualification':str(i.qualification),
            'place':str(i.place),
            'post':str(i.post),
            'pin':str(i.pin),
        })
    return JsonResponse({'status':'ok','data':l})



def user_view_service(request):
    l=[]
    a=service.objects.all()
    for i in a:
        l.append({
            'id':str(i.id),
            'service_name':str(i.service_name),
            'details':str(i.details),
            'fee':str(i.fee),

        })
    return JsonResponse({'status':'ok','data':l})

def user_view_workout_plans(request):
    l=[]
    a=workout_plans.objects.all()
    for i in a:
        l.append({
            'id':str(i.id),
            'goal':str(i.goal),
            'workout':str(i.workout),
            'time_per_day':str(i.time_per_day),

        })
    return JsonResponse({'status':'ok','data':l})


def user_view_diet_plan(request):
    l = []
    a = diet_plan.objects.all()
    for i in a:
        l.append({
            'id': str(i.id),
            'REQUEST': str(i.REQUEST),
            'day_shift': str(i.day_shift),
            'planname': str(i.planname),
            'category_type': str(i.category_type),

        })
    return JsonResponse({'status': 'ok', 'data': l})


def user_view_tip(request):
    l = []
    a = tip.objects.all()
    for i in a:
        l.append({
            'id': str(i.id),
            'title': str(i.title),
            'description': str(i.description),
            'TRAINER': str(i.TRAINER),

        })
    return JsonResponse({'status': 'ok', 'data': l})


def user_view_workout_video(request):
    l = []
    a = workout_video.objects.all()
    for i in a:
        l.append({
            'id': str(i.id),
            'video': str(i.video),
            'description': str(i.description),

        })
    return JsonResponse({'status': 'ok', 'data': l})

def user_view_motivated_video(request):
    l = []
    a = motivated_video.objects.all()
    for i in a:
        l.append({
            'id': str(i.id),
            'video': str(i.video),
            'title': str(i.title),
            'description': str(i.description),
            'date': str(i.date),

        })
    return JsonResponse({'status': 'ok', 'data': l})





