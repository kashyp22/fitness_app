from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

# Create your views here.
from myapp.models import *


def logins(request):
    return render(request, 'admin/login_index.html')
def logout_get(request):
    logout(request)
    return redirect('/myapp/logins/')
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
            return redirect('/myapp/logins/')
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
    if service.objects.filter(service_name=servicename).exists():
        return HttpResponse('<script>alert("Not Success servicename Alreday exists please try another servicename");window.location="/myapp/add_service_plan/"</script>')
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
    sid=request.session['id']
    if service.objects.filter(service_name=servicename).exists():
        return HttpResponse(f'<script>alert("Not Success servicename Alreday exists please try another servicename");window.location="/myapp/edit_service_plan/{sid}"</script>')

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


    if User.objects.filter(username=username).exists():
        return HttpResponse('<script>alert("Not Success Username Alreday exists please try another username");window.location="/myapp/add_trainer/"</script>')
    if User.objects.filter(email=email).exists():
        return HttpResponse('<script>alert("Not Success Email Alreday exists please try another email");window.location="/myapp/add_trainer/"</script>')

    
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
    data=complaint.objects.all()
    return render(request, 'admin/view_complaint.html',{"data":data})

def view_review(request):
    data=review.objects.all()

    return render(request, 'admin/view_review.html',{"data":data})

def view_user(request):

    data=user_table.objects.all()

    return render(request, 'admin/view_user.html',{"data":data})

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


def add_diet_plan(request,id):
    request.session['did']=id
    return render(request,'trainer/add_diet_plan.html')

def add_diet_plan_post(req):
  Date=req.POST['Date']
  Day_shift=req.POST['Day_shift']
  Plan_Name=req.POST['Plan_Name']
  category_type=req.POST['category_type']
  discription=req.POST['discription']
  duration=req.POST['duration']
  target_goal =req.POST['target_goal']


  g=diet_plan()
  g.date=Date
  g.day_shift=Day_shift
  g.planname=Plan_Name
  g.category_type=category_type
  g.discription=discription
  g.duration=duration
  g.target_goal=target_goal
  g.REQUEST=user_request.objects.get(LOGIN_id=req.user.id)
  g.save()


  return redirect('/myapp/add_diet_plan/')


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
    g = diet_plan()
    g.date = Date
    g.day_shift = Day_shift
    g.planname = Plan_Name
    g.category_type = category_type
    g.discription = discription
    g.duration = duration
    g.target_goal = target_goal
    g.TRAINER = trainer.objects.get(id=trainer)
    g.save()
    return redirect('/myapp/edit_diet_plan/{trainer}')

# diet ====================

def adddiet(request):
    return render(request,"trainer/add_diet.html")


def adddiet_post(request,):
    BMI=request.POST['BMI']
    TYPE=request.POST['type']
    GENDER=request.POST['gender']
    AGE=request.POST['age']
    HEIGHT=request.POST['height']
    WEIGHT=request.POST['weight']
    DIETPLAN=request.POST['diet_plan']
    work_out=request.POST['work_out']

    obj=Diet_table()
    obj.bmi=BMI
    obj.type=TYPE
    obj.gender=GENDER
    obj.age=AGE
    obj.height=HEIGHT
    obj.dietplan=DIETPLAN
    obj.weight=WEIGHT
    obj.work_out=work_out
    obj.TRAINER=trainer.objects.get(LOGIN=request.user.id)
    obj.save()
    return redirect('/myapp/viewdiet/')

def viewdiet(request):
    h=Diet_table.objects.filter(TRAINER__LOGIN_id=request.user.id)
    return render(request,"trainer/view_diet.html",{'data':h})


def editdiet(request,id):
    a=Diet_table.objects.get(id=id)
    request.session['did']=id
    return render(request,"trainer/editdiet.html",{'data':a})



def editdiet_post(request):
    BMI=request.POST['BMI']
    TYPE=request.POST['type']
    GENDER=request.POST['gender']
    AGE=request.POST['age']
    HEIGHT=request.POST['height']
    WEIGHT=request.POST['weight']
    DIETPLAN=request.POST['diet_plan']
    work_out=request.POST['work_out']
    obj=Diet_table.objects.get(id=request.session['did'])


    obj.bmi=BMI
    obj.type=TYPE
    obj.gender=GENDER
    obj.age=AGE
    obj.height=HEIGHT
    obj.dietplan=DIETPLAN
    obj.weight=WEIGHT
    obj.work_out=work_out
    obj.TRAINER=trainer.objects.get(LOGIN=request.user.id)
    obj.save()
    return redirect('/myapp/viewdiet/')

def deletediet(request,id):
    Diet_table.objects.get(id=id).delete()
    return redirect('/myapp/viewdiet/')



#  ============= diet end






















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
    ab=tips.objects.filter(TRAINER__LOGIN_id=request.user.id)
    return render(request,'trainer/view_tips.html',{'data':ab})

def delete_tips(request,id):
    a=tips.objects.get(id=id)
    a.delete()
    return redirect('/myapp/view_tips/')

def add_tips(request):
    return render(request,'trainer/add_tips.html')

def add_tips_post(request):
    Title = request.POST['Title']
    Description=request.POST['Description']
    a=tips()
    a.tips=Title
    a.date=datetime.now().today()
    a.details=Description
    a.TRAINER=trainer.objects.get(LOGIN_id=request.user.id)
    a.save()
    return redirect('/myapp/view_tips/')

def add_workoutplan(request):
    request.session['wid']=id
    return render(request,'trainer/add_workoutplan.html')

def add_workoutplan_post(req):
    Date=req.POST['date']
    Plan_Name=req.POST['planname']
    Video=req.FILES['video']
    Details=req.POST['details']
    a=workout_plan()
    a.date=Date
    a.video=Video
    a.details=Details
    a.plan_name=Plan_Name
    a.REQUEST=user_request.objects.get(id=req.session['wid'])
    a.save()
    return redirect(f"/myapp/view_workoutplan/{req.session['wid']}")


def trainer_change_password(request):
    return render(request,'trainer/change_password.html')

def change_password_POST(request):
    Current_Password=request.POST['Current_Password']
    New_Password=request.POST['New_Password']
    Confirm_Password=request.POST['Confirm_Password']


 
    return redirect('trainer/change_password/{trainer}')

def edit_tips(request,id):
    request.session['tid']=id
    d=tips.objects.get(id=id)
    return render(request,'trainer/edit_tips.html',{'data':d})


def edit_tips_post(request):
    Title = request.POST['Title']
    Description=request.POST['Description']
    a=tips.objects.get(id=request.session['tid'])
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
    data=Payment_trainer.objects.filter(REQUEST__TRAINER__LOGIN_id=request.user.id)
    return render(request,'trainer/view_fee_alert.html',{"data":data})

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

def view_user_service_request(req,id):
    data=user_request.objects.filter(TRAINER__LOGIN_id=req.user.id,SERVICE_id=id)
    return render(req,'trainer/view_user_request.html',{"data":data})

def view_user_request(req):
    data=user_request.objects.filter(TRAINER__LOGIN_id=req.user.id)
    return render(req,'trainer/view_user_request.html',{"data":data})


def user_request_approve(req,id):
    data=user_request.objects.filter(id=id).update(status="accept")
    return redirect('/myapp/view_user_request/')

def user_request_reject(req,id):
    data=user_request.objects.filter(id=id).update(status="reject")
    return redirect('/myapp/view_user_request/')

def view_user_serviceplan(request):
    ab=service.objects.all()
    return render(request, 'trainer/view_user_serviceplan.html')

def view_workoutplan(request,id):
    ab=workout_plan.objects.filter(REQUEST_id=id)
    request.session['wid']=id
    return render(request,'trainer/view_workoutplan.html',{"data":ab})



##########################################flutter

def flutter_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username,password,"aaaaaa")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.groups.filter(name="User").exists():
                return JsonResponse({"status": "ok","type": "user", "lid": user.id})
            return JsonResponse({"status": "no","type": "other", "lid": user.id})
        return JsonResponse({"status": "no"})
    return JsonResponse({"status": "no", "message": "POST required"})


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

def request_trainer(req):
    lid = req.POST['lid']
    service_id = req.POST['service_id']
    trainer_id = req.POST['trainer_id']
    # if not lid or not service_id or not trainer_id:
    #     return JsonResponse({'status': 'error', 'message': 'Missing required fields'})
    try:
        user = user_table.objects.get(LOGIN_id=lid)
        trainer_obj = trainer.objects.get(id=trainer_id)
        service_obj = service.objects.get(id=service_id)
    except (user_table.DoesNotExist, trainer.DoesNotExist, service.DoesNotExist):
        return JsonResponse({'status': 'error', 'message': 'Invalid user/trainer/service'})

    # Check if request already exists
    if user_request.objects.filter(USER=user, TRAINER=trainer_obj, SERVICE=service_obj).exists():
        return JsonResponse({'status': 'error', 'message': 'Request already exists'})

    # Create new request
    user_request.objects.create(
        USER=user,
        TRAINER=trainer_obj,
        SERVICE=service_obj,
        status="pending"
    )

    return JsonResponse({'status': 'ok', 'message': 'Trainer requested successfully'})


# views.py




def view_request_status(request_obj):
    lid = request_obj.GET.get('lid')
    if not lid:
        return JsonResponse({'status': 'error', 'message': 'Missing user id'})

    try:
        user = user_table.objects.get(LOGIN_id=lid)
    except user_table.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User not found'})

    reqs = user_request.objects.filter(USER=user).select_related('TRAINER', 'SERVICE')
    data = []
    for r in reqs:
        data.append({
            'id': r.id,
            'trainer': r.TRAINER.name,
            'tlid': r.TRAINER.LOGIN.id,
            'service': r.SERVICE.service_name,
            'fees': r.SERVICE.fee,
            'date': str(r.date),
            'status': r.status,
        })

    return JsonResponse({'status': 'ok', 'data': data})



def user_view_workout_plans(request):
    rid=request.POST['rid']
    print(rid,"rid")
    l=[]
    a=workout_plan.objects.filter(REQUEST_id=rid)
    for i in a:
        l.append({
            'id':str(i.id),
            'date':str(i.date),
            'video':str(i.video.url),
            'details':str(i.details),
            'plan_name':str(i.plan_name),
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
    a = tips.objects.all()
    for i in a:
        l.append({
            'id': str(i.id),
            'tips': str(i.tips),
            'details': str(i.details),
            'date': str(i.date),
            't_name': str(i.TRAINER.name),

        })
    return JsonResponse({'status': 'ok', 'data': l})


def user_view_motivational_video(request):
    l = []
    a = motivated_video.objects.all()
    for i in a:
        l.append({
            'id': str(i.id),
            'video': str(i.video.url),
            'description': str(i.description),
            'title': str(i.title),
            'date': str(i.date),
            't_name': str(i.TRAINER.name),
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




def user_view_entiquette(request):
    l = []
    a = entiquette.objects.all()
    for i in a:
        l.append({
            'id': str(i.id),
            'rules': str(i.rules),
            'punishment': str(i.punishment),
            'date': str(i.date),
        })
    return JsonResponse({'status': 'ok', 'data': l})





from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import user_table

@csrf_exempt
def UserRegistration(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            dob = request.POST.get('dob')   # optional if you add DOB later
            gender = request.POST.get('gender')
            place = request.POST.get('place')
            district = request.POST.get('district')
            pincode = request.POST.get('pincode')
            email = request.POST.get('email')
            phone = request.POST.get('number')
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Handle photo upload
            photo = request.FILES.get('photo')
            photo_name = ""
            if photo:
                fs = FileSystemStorage(location="media/photos/")
                photo_name = fs.save(photo.name, photo)

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({"status": "error", "message": "Username already exists"})

            # Create Django User
            user = User.objects.create_user(username=username, password=password)

            user.groups.add(Group.objects.get(name="User"))
            user.save()

            # Save in user_table
            user_table.objects.create(
                LOGIN=user,
                name=name,
                dob=dob,
                gender=gender,
                photo=photo_name,
                email=email,
                phone=phone,
                place=place,
                post=district,
                pin=pincode
            )

            return JsonResponse({"status": "ok"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request"})



# =========================


import pandas as pd

def export_data(request):
    qs = Diet_table.objects.all().values()
    df = pd.DataFrame(qs)
    df.to_csv("diet_data.csv", index=False)
    return HttpResponse("Export complete")


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .predict_diet_ml import predict_diet

@csrf_exempt
@csrf_exempt
def predict_diet_api(request):
    if request.method == "POST":
        data = json.loads(request.body)

        print(data,"data")
        result = predict_diet(
            int(data["age"]),
            int(data["height"]),
            int(data["weight"]),
            data["gender"],
            food_preference=data.get("food_preference"),
            health_condition=data.get("health_condition")
        )
        print(result,"rrrrrr")
        return JsonResponse({
            "status": "success",
            "bmi": result["bmi"],
            "category": result["predicted_type"],
            "diet_plan": result["diet"],
            "workout_plan": result["workout"]
        })




from .utils import generate_health_plan


def generate_bmi_plan_api(request):
    if request.method == 'POST':
        # Matching the keys sent from Flutter
        bmi = float(request.POST.get('bmi', 0))
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        goal = request.POST.get('goal')
        weight = request.POST.get('weight')
        height = request.POST.get('height')

        # Call the Gemini function
        result = generate_health_plan(bmi, age, gender, goal, weight, height)

        print(result,"resulttttttttt")

        return JsonResponse(result)

    return JsonResponse({'error': 'Invalid request'}, status=400)



# =============chat =======


def chat1(request, id):
    if request.user.id!='':
        request.session["userid"] = id
        cid = str(request.session["userid"])
        request.session["new"] = cid
        qry = user_table.objects.get(LOGIN_id=cid)
        return render(request, "trainer/Chat.html", {'photo': qry.photo.url, 'name': qry.name, 'toid': cid})
    else:
        return HttpResponse('''<script>alert('You are not Logined');window.location='/myapp/login/'</script>''')


def chat_view(request):
    if request.user.id!='':
        fromid = request.user.id
        toid = request.session["userid"]
        qry = user_table.objects.get(LOGIN_id=request.session["userid"])
        from django.db.models import Q
        res = Chat.objects.filter(Q(FROM_ID_id=fromid, TO_ID_id=toid) | Q(FROM_ID_id=toid, TO_ID_id=fromid))
        l = []
        for i in res:
            l.append({
                "id": i.id,
                "message": i.message,
                "to": i.TO_ID_id,
                "date": i.date,
                "from": i.FROM_ID_id
            })
        return JsonResponse({'photo': qry.photo.url, "data": l, 'name': qry.name, 'toid': request.session["userid"]})
    else:
        return HttpResponse('''<script>alert('You are not Logined');window.location='/myapp/login/'</script>''')


def chat_send_web(request, msg):
    if request.user.id!='':
        lid = request.user.id
        toid = request.session["userid"]
        message = msg

        import datetime
        d = datetime.datetime.now().date()
        chatobt = Chat()
        chatobt.message = message
        chatobt.TO_ID_id = toid
        chatobt.FROM_ID_id = lid
        chatobt.date = d
        chatobt.save()
    else:
        return HttpResponse('''<script>alert('You are not Logined');window.location='/myapp/login/'</script>''')


    return JsonResponse({"status": "ok"})

# dart chat

def chat_send(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    msg=request.POST['message']
    print(FROM_id,TOID_id,"aaaaaaaaaa")

    from  datetime import datetime
    c=Chat()
    c.FROM_ID_id=FROM_id
    c.TO_ID_id=TOID_id
    c.message=msg
    c.date=datetime.now().date()
    c.time=datetime.now().time()
    c.save()
    return JsonResponse({'status':"ok"})

def chat_view_and(request):
    from_id=request.POST['from_id']
    to_id=request.POST['to_id']
    l=[]
    data1=Chat.objects.filter(FROM_ID_id=from_id,TO_ID_id=to_id).order_by('id')
    data2=Chat.objects.filter(FROM_ID_id=to_id,TO_ID_id=from_id).order_by('id')

    data= data1 | data2
    print(data)

    for res in data:
        l.append({'id':res.id,'from':res.FROM_ID.id,'to':res.TO_ID.id,'msg':res.message,'date':res.date})

    return JsonResponse({'status':"ok",'data':l})


# payment alert


from django.http import JsonResponse
from django.utils.timezone import now
from .models import user_request, Payment_trainer

def payment_alert(request):
    lid=request.POST['lid']
    try:
        # Get the user_request object
        req = user_request.objects.get(USER__LOGIN_id=lid)

        if req.status.lower() == "accept":
            fee = int(req.SERVICE.fee)

            # Check if payment already exists for this month
            exists = Payment_trainer.objects.filter(
                REQUEST=req,
                date__year=now().year,
                date__month=now().month
            ).exists()

            if not exists:
                payment = Payment_trainer.objects.create(
                    REQUEST=req,
                    amount=fee,
                    status="pending",
                    date=now().date()
                )
                data = {
                    "status": "ok",
                    "message": "Payment alert created",
                    "payment_id": payment.id,
                    "amount": payment.amount,
                    "service": req.SERVICE.service_name,
                    "user": req.USER.id,
                    "trainer": req.TRAINER.id,
                    "pstatus": payment.status,
                    "date": str(payment.date)
                }
            else:
                data = {
                    "success": False,
                    "message": "Payment alert already exists for this month",
                    "service": req.SERVICE.service_name,
                    "amount": fee
                }
        else:
            data = {
                "success": False,
                "message": "Request not accepted yet",
                "status": req.status
            }

    except user_request.DoesNotExist:
        data = {
            "success": False,
            "message": "User request not found"
        }
    print(data,"data")
    return JsonResponse(data)



from django.http import JsonResponse
from django.utils.timezone import now
from .models import Payment_trainer, user_request

def view_payment_alert(request):
    lid = request.POST.get('lid')
    try:
        # Get the user_request object
        req = user_request.objects.get(USER__LOGIN_id=lid)

        # Fetch all payment alerts that are pending and not yet viewed
        payments = Payment_trainer.objects.filter(
            REQUEST=req,
            status="pending",
            view_status=False
        ).order_by('-date')

        if payments.exists():
            alerts = []
            for p in payments:
                alerts.append({
                    "payment_id": p.id,
                    "amount": p.amount,
                    "service": req.SERVICE.service_name,
                    "trainer": req.TRAINER.id,
                    "user": req.USER.id,
                    "pstatus": p.status,
                    "date": str(p.date)
                })
                # Mark this alert as viewed
                p.view_status = True
                p.save(update_fields=["view_status"])

            data = {
                "status": "ok",
                "alerts": alerts
            }
        else:
            data = {
                "success": False,
                "message": "No payment alerts found"
            }

    except user_request.DoesNotExist:
        data = {
            "success": False,
            "message": "User request not found"
        }

    return JsonResponse(data)

from django.http import JsonResponse
from django.utils.timezone import now
from .models import Payment_trainer

def view_pending_payments(request):
    lid = request.POST.get('lid')  # login id from frontend
    payments = Payment_trainer.objects.filter(
        REQUEST__USER__LOGIN_id=lid,
        # status="pending"
    )

    data = []
    for p in payments:
        data.append({
            "payment_id": p.id,
            "amount": p.amount,
            "service": p.REQUEST.SERVICE.service_name,
            "user": p.REQUEST.USER.id,
            "trainer": p.REQUEST.TRAINER.id,
            "status": p.status,
            "date": str(p.date)
        })

    return JsonResponse({"data": data})



def user_payment(request):
    pid=request.POST['pid']
    Payment_trainer.objects.filter(id=pid).update(status="paid")
    return JsonResponse({"status":"ok"})






