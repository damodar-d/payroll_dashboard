from django.db import models


class EmployeePayScale(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    e_pay_scale = models.IntegerField()

    class Meta:
        db_table = "employee_pay_scale"


class EmployeeIncomeTax(models.Model):
    employee_id = models.IntegerField(primary_key=True, unique=True)
    e_tax_slab_percentage = models.IntegerField()

    class Meta:
        db_table = "employee_income_tax"


class EmployeeAttendance(models.Model):
    employee_id = models.IntegerField(blank=False, unique=False)
    month = models.CharField(unique=False, max_length=20, blank=False)
    no_of_days_present = models.IntegerField(unique=False, blank=False)


    class Meta:
        db_table = "employee_attendance"
