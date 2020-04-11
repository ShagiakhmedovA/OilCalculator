from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
import math

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    edit_date = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Calculation(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    V1 = models.FloatField()
    V2 = models.FloatField()
    RZAB1 = models.FloatField()
    RZAB2 = models.FloatField()
    RPL = models.FloatField()
    DEP1 = models.FloatField(blank=True)
    DEP2 = models.FloatField(blank=True)
    RASH1 = models.FloatField(blank=True)
    RASH2 = models.FloatField(blank=True)
    B = models.FloatField(blank=True)
    A = models.FloatField(blank=True)


    def do_expression_DEP1(self):
        V1 = str(self.V1)
        V2 = str(self.V2)
        RZAB1 = str(self.RZAB1)
        RZAB2 = str(self.RZAB2)
        RPL = str(self.RPL)
        V1 = V1.replace(',', '.')
        V2 = V2.replace(',', '.')
        RZAB1 = RZAB1.replace(',', '.')
        RZAB2 = RZAB2.replace(',', '.')
        RPL = RPL.replace(',', '.')
        try:
            V1 = float(V1)
            V2 = float(V2)
            RZAB1 = float(RZAB1)
            RZAB2 = float(RZAB2)
            RPL = float(RPL)
        except ValueError:
            return {'MESSAGE':'Ошибка: вы ввели неверный тип данных'}
        try:
            DEP1 = math.pow(RPL, 2)-math.pow(RZAB1, 2)
            DEP2 = math.pow(RPL, 2)-math.pow(RZAB2, 2)
            RASH1 = DEP1/V1
            RASH2 = DEP2/V2
            B = ((RASH2)-(RASH1))/(V2-V1)
            A = (RASH1)-(B/V1)
            DEP1 = math.pow(RPL, 2)-math.pow(RZAB1, 2)
            DEP2 = math.pow(RPL, 2)-math.pow(RZAB2, 2)
            RASH1 = DEP1/V1
            RASH2 = DEP2/V2
            B = ((RASH2)-(RASH1))/(V2-V1)
            A = (RASH1)-(B*V1)
            self.DEP1 = round(DEP1, 3)
            self.DEP2 = round(DEP2, 3)
            self.RASH1 = round(RASH1, 3)
            self.RASH2 = round(RASH2, 3)
            self.B = round(B, 3)
            self.A = round(A, 3)
            self.save()
            return self.DEP1
        except ZeroDivisionError:
            return {'MESSAGE':'Ошибка: деление на ноль'}

