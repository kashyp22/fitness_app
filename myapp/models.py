from django.db import models
from  django.contrib.auth.models import User

class user_table(models.Model):
    LOGIN = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob=models.DateField(default=True)
    gender = models.CharField(max_length=100)
    photo = models.FileField()
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()

class trainer(models.Model):
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()

class complaint(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    Complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    date=models.DateField()

class review(models.Model):
    TRAINER=models.ForeignKey(trainer,on_delete=models.CASCADE)
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    review=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    date=models.DateField()

class service(models.Model):
    service_name=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    fee=models.CharField(max_length=100)

class user_request(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    TRAINER = models.ForeignKey(trainer,on_delete=models.CASCADE)
    SERVICE = models.ForeignKey(service,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100)

class workout_plan(models.Model):
    REQUEST = models.ForeignKey(user_request,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    video = models.FileField()
    details=models.CharField(max_length=500)
    plan_name=models.CharField(max_length=200)

class assign_trainer(models.Model):
    TRAINER=models.ForeignKey(trainer,on_delete=models.CASCADE)
    day=models.CharField(max_length=100)
    from_time=models.TimeField()
    to_time=models.TimeField()
    date=models.DateField(auto_now_add=True)

class Chat(models.Model):
    FROM_ID = models.ForeignKey(User,on_delete=models.CASCADE,related_name="fr")
    TO_ID = models.ForeignKey(User,on_delete=models.CASCADE,related_name="to")
    date=models.DateField(auto_now_add=True)
    message=models.CharField(max_length=100)

class entiquette(models.Model):
    rules = models.CharField(max_length=100)
    punishment = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

class diet_plan(models.Model):
    REQUEST = models.ForeignKey(user_request,on_delete=models.CASCADE)
    date=models.DateField()
    day_shift=models.CharField(max_length=100)
    planname=models.CharField(max_length=100)
    category_type=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    discription=models.CharField(max_length=500)
    target_goal=models.CharField(max_length=500)


class Diet_table(models.Model):
    bmi=models.CharField(max_length=100)
    TRAINER=models.ForeignKey(trainer,on_delete=models.CASCADE)
    gender=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    age=models.IntegerField()
    height=models.IntegerField()
    weight=models.IntegerField()
    dietplan=models.CharField(max_length=1000)
    work_out=models.CharField(max_length=1000)


class tips(models.Model):
    TRAINER=models.ForeignKey(trainer,on_delete=models.CASCADE)
    tips=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)

class motivated_video(models.Model):
    TRAINER=models.ForeignKey(trainer,on_delete=models.CASCADE)
    video=models.FileField()
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)

class Payment_trainer(models.Model):
    REQUEST=models.ForeignKey(user_request,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default="paid")
    date=models.DateField(auto_now_add=True)
    amount=models.IntegerField()
    view_status=models.BooleanField(default=False)



































