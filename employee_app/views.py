import json
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Employee,Attendance
from .forms import EmployeeForm, SignupForm
from django.contrib import messages
from .forms import LoginForm
from django.http import Http404
import pandas as pd
from .forms import AttendanceUploadForm
import openpyxl
from django.db.models import Count
from django.contrib.auth.decorators import login_required



# @login_required(login_url='login')
# Create your views here.

def HomePage(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            # Ensure username is not empty
            if not username:
                form.add_error('username', 'Username is required.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    form.add_error(None, 'User authentication failed.')

        # Render the form again with errors if form is not valid or username is missing
        return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('add_emp')  # Redirect to add_emp if login is successful
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    
@login_required(login_url='login')
def emp_add(request):
    
    if request.method == 'POST':
        
        employees_id = request.POST.get("employee_id")
        employees_name = request.POST.get("employee_name")
        email = request.POST.get("employee_email")
        phone_number = request.POST.get("phone_number")
        job_title = request.POST.get("job_title")

        e = Employee()
        e.employee_id = employees_id
        e.employee_name = employees_name
        e.email = email
        e.phone_number = phone_number
        e.job_title = job_title
        e.save()
        return redirect("table")
    return render(request, "add_emp.html")

@login_required(login_url='login')
def ListPage(request):
    emp=Employee.objects.all()
    return render(request,"table.html",{'emp':emp})

def DeletePage(request,employee_id):
    e=Employee.objects.get(employee_id=employee_id)
    e.delete()
    return redirect("table")

@login_required(login_url='login')
def UpdatePage(request, employee_id):
    e = get_object_or_404(Employee, employee_id=employee_id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return redirect('table')  
    else:
        form = EmployeeForm(instance=e)
    
    return render(request, 'update.html', {'form': form, 'e': e})


def LogoutPage(request):
    if 'is_logged_in' in request.session:
        del request.session['is_logged_in']
    logout(request)
    return render(request,'logout.html')
@login_required(login_url='login')
def upload_attendance(request):
    if request.method == 'POST':
        form = AttendanceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                attendance_id, employee_id, date, present = row
                employee = Employee.objects.get(employee_id=employee_id)
                
                # Delete duplicates
                Attendance.objects.filter(attendance_id=attendance_id).delete()
                
                # Create 
                Attendance.objects.create(
                    attendance_id=attendance_id,
                    employee_id=employee,
                    date=date,
                    present=present,
                )
            return redirect('attendance_list')
    else:
        form = AttendanceUploadForm()
    return render(request, 'upload_attendance.html', {'form': form})


def employee_attendance(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    attendance_records = Attendance.objects.filter(employee_id=employee)
    
    # Prepare data for the chart
    attendance_data = attendance_records.values('date', 'present').annotate(present_count=Count('present'))
    dates = [record['date'].strftime('%Y-%m-%d') for record in attendance_data]
    present_counts = [record['present_count'] if record['present'] == 'Y' else 0 for record in attendance_data]
    absent_counts = [record['present_count'] if record['present'] == 'N' else 0 for record in attendance_data]
    
    return render(request, 'employee_attendance.html', {
        'employee': employee,
        'attendance_records': attendance_records,
        'dates': dates,
        'present_counts': present_counts,
        'absent_counts': absent_counts,
    })



