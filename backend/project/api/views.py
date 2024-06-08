from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import EmployeeIncomeTax, EmployeePayScale, EmployeeAttendance
from django.core.serializers import serialize
# Create your views here.
import json
import requests

month_days_mapping = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 31,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}


def get_gross_pay(request, employee_id):

    if request.method == "GET":
        base_url = "http://localhost:8000/api/get-employee-basic-pay-of-month/"+str(employee_id)
        response = requests.get(base_url)
        if response.status_code == 404:
            results = response.json()
            return HttpResponse(json.dumps({"message": results["message"]}), status=response.status_code, content_type="application/json")
        return HttpResponse(response, status=200, content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message":"Method not allowed"}), status=405, content_type="application/json")


def get_net_pay(request, employee_id, month):


    if request.method == "GET":
        base_url = "http://localhost:8000/api/get-gross-pay/"+str(employee_id)
        response = requests.get(base_url)
        results = response.json()
        if response.status_code == 404:
            return HttpResponse(json.dumps({"message": results["message"]}), status=response.status_code, content_type="application/json")
        basic_pay = results["basic_pay"]
        employee_tax_percentage = -1
        try:
            employee_tax_queryset = EmployeeIncomeTax.objects.get(employee_id=employee_id)
            employee_month_queryset = EmployeeAttendance.objects.get(month=month, employee_id=employee_id)
            employee_tax_percentage = employee_tax_queryset.e_tax_slab_percentage
            employee_month_attendance = employee_month_queryset.no_of_days_present
            total_month_salary = (basic_pay//month_days_mapping[month])*employee_month_attendance
            net_salary= total_month_salary * ((100-employee_tax_percentage)/100.00)
            data= {
                "gross_pay":total_month_salary,
                "net_pay":net_salary
            }
            print("retrieved data successfully", data)
            return HttpResponse(json.dumps(data), status=200,  content_type="application/json")

        except EmployeeIncomeTax.DoesNotExist:
            return HttpResponse(json.dumps({"message": "Tax information for employee with given ID does not exist"}), status=404,
                                content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message":"Method not allowed"}), status=405, content_type="application/json")


def get_employee_basic_pay_of_month(request, employee_id):

    if request.method == "GET":
        try:
            employee_queryset = EmployeePayScale.objects.get(employee_id=employee_id)
        except EmployeePayScale.DoesNotExist:
            return HttpResponse(json.dumps({"message": "Record with given ID does not exist"}), status=404,content_type="application/json")

        data = {
             "employee_id":employee_queryset.employee_id,
             "basic_pay":employee_queryset.e_pay_scale
         }
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message": "Method Not allowed"}), status=405,  content_type="application/json")


def add_employee_basic_pay_of_month(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        employee_pay = EmployeePayScale(e_pay_scale=body["employee_pay_scale"], employee_id=body["employee_id"])
        try:

            employee_pay.save()
            response = {
                "message": "Saved Data Successfully!"
            }
            return HttpResponse(json.dumps(response), status=201, content_type="application/json")
        except Exception:
            response = {
                "message": "Something went wrong ! Internal Server Error"
            }
            return HttpResponse(json.dumps(response), status=501, content_type="application/json")
    else:
        response = {
            "message": "Method not allowed"
        }
        return HttpResponse(json.dumps(response), content_type="application/json")


def add_employee_tax(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        employee_id = body["employee_id"]
        employee_tax = body["employee_tax"]
        tax = EmployeeIncomeTax(e_tax_slab_percentage=employee_tax, employee_id=employee_id)
        try:
            tax.save()
            response = {
                "message": "Saved Data Successfully!"
            }
            return HttpResponse(json.dumps(response), status=201, content_type="application/json")

        except Exception:
            response = {
                "message": "Something went wrong ! Internal Server Error"
            }
            return HttpResponse(json.dumps(response), status=501, content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message":"Method Not allowed"}), status=405, content_type="application/json")


def add_employee_attendance_for_month(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        employee_id = body["e_id"]
        month = body["month"]
        days_present = body["days_present"]
        employee_attendance = EmployeeAttendance(employee_id = employee_id, month = month, no_of_days_present = days_present)
        try:
            employee_attendance.save()
            response = {
                "message": "Saved Data Successfully!"
            }
            return HttpResponse(json.dumps(response), status=201, content_type="application/json")
        except Exception:
            response = {
                "message": "Something went wrong ! Internal Server Error"
            }
            return HttpResponse(json.dumps(response), status=501, content_type="application/json")




