from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class trainer(models.Model):
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()

class service(models.Model):
    service_name=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    fee=models.CharField(max_length=100)

class user_table(models.Model):
    LOGIN = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100),
    gender = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()


class workout_plans(models.Model):
    TRAINER=models.ForeignKey(trainer,on_delete=models.CASCADE)
    goal=models.CharField(max_length=100)
    workout=models.CharField(max_length=100)
    time_per_day=models.TimeField()


class complaint(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    Complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    date=models.DateField()


class review(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    review=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    date=models.DateField()

class workout_video(models.Model):
    video = models.FileField()
    description = models.CharField(max_length=100)


class assign_trainer(models.Model):
    TRAINER=models.ForeignKey(trainer,on_delete=models.CASCADE)
    day=models.CharField(max_length=100)
    from_time=models.TimeField()
    to_time=models.TimeField()
    date=models.DateField()

class entiquette(models.Model):
    rules = models.CharField(max_length=100)
    punishment = models.CharField(max_length=100)
    date = models.DateField()


class tips(models.Model):
    TRAINER=models.ForeignKey(trainer,on_delete=models.CASCADE)
    tips=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    date=models.DateField()


class motivated_video(models.Model):
    TRAINER=models.ForeignKey(trainer,on_delete=models.CASCADE)
    video=models.FileField()
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    date=models.DateField()


class request(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    TRAINER = models.ForeignKey(trainer,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100)


class diet_plan(models.Model):
    REQUEST = models.ForeignKey(request,on_delete=models.CASCADE)
    TRAINER = models.ForeignKey(trainer,on_delete=models.CASCADE)
    date=models.DateField()
    day_shift=models.CharField(max_length=100)
    planname=models.CharField(max_length=100)
    category_type=models.CharField(max_length=100)

# class motivational_video(models.Model):
#     video=models.FileField()
#     title=models.CharField(max_length=100)


class tip(models.Model):
    title=models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    TRAINER = models.ForeignKey(trainer,on_delete=models.CASCADE)
    date=models.DateField()


class workoutplan(models.Model):
    date=models.DateField()
    planname=models.CharField(max_length=100)
    video=models.FileField()
    details=models.CharField(max_length=100)
    DIET_PLAN = models.ForeignKey(diet_plan,on_delete=models.CASCADE)



class user_request(models.Model):
    Sno=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    photo=models.FileField()
    DoB=models.DateField()
    Gender=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Contact= models.BigIntegerField()
    Type=models.CharField(max_length=100)

#
#
# class serviceplan(models.Model):
#
#     Sno=models.CharField(max_length=100)
#     Service_Name=models.CharField(max_length=100)
#     Amount=models.IntegerField()
#     Duration=models.TimeField()
#     Details=models.CharField(max_length=100)
#


class fee_alert(models.Model):
    Sno=models.CharField(max_length=100)
    Fee=models.IntegerField()
    Username=models.CharField(max_length=100)




































