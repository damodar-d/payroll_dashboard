from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("get-gross-pay/<int:employee_id>", views.get_gross_pay),
    path("get-net-pay/<int:employee_id>/<slug:month>", views.get_net_pay),
    path("get-employee-basic-pay-of-month/<int:employee_id>", views.get_employee_basic_pay_of_month),
    path("add-employee-basic-pay-of-month", views.add_employee_basic_pay_of_month),
    path("add-employee-tax", views.add_employee_tax),
    path("add-employee-attendance-for-month", views.add_employee_attendance_for_month),
]