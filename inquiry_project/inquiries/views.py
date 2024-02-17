from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import inquiries
from inquiries.models import enquiry
from .forms import EnquiryForm 
from django.contrib import messages

# Create your views here.


@login_required(login_url='login')

# def HomePage(request):
#     return render(request,'home.html')


def enquiry_view(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Enquiry submitted successfully!')
            return redirect('enquiry') 
    else:
        form = EnquiryForm() 
        return render(request, 'enquiry.html', {'form': form})


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("password does not match")
        
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')


    return render(request,'signup.html')

 
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username = username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            # return HttpResponse("username or password is incorrect!")
            error = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error': error})
    else:
        
        return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')








def index(request):
    return render(request, 'index.html')


def blank(request):
    return render(request, 'blank.html')


def table(request):
    return render(request, 'table.html')


def accept_inq(request):
    return render(request, 'accept_inq.html')




# show backend data on view page

def view_inq1(request):
    data = enquiry.objects.all()

    if request.method == 'GET':
        # Handle filter submission
        name_filter = request.GET.get('name', None)
        subject_type_filter = request.GET.get('subject_type', None)
        email_filter = request.GET.get('email', None)
        mobile_number_filter = request.GET.get('phone_number', None)

        if name_filter:
            data = data.filter(name__icontains=name_filter)
        if subject_type_filter:
            data = data.filter(subject_type=subject_type_filter)
        if email_filter:
            data = data.filter(email__icontains=email_filter)
        if mobile_number_filter:
            data = data.filter(mobile_number__icontains=mobile_number_filter)

    return render(request, 'blank.html', {'data': data})
    





# delete entry from database

def delete_data(request, data_id):
    try:
        # Retrieve the object from the database
        data = enquiry.objects.get(id=data_id)
        # Delete the object
        data.delete()
        # Redirect to a success page, or a page displaying the remaining data
        return redirect('blank')  # You need to define the URL name for the success page
    except enquiry.DoesNotExist:
        # Handle the case where the object does not exist
        return redirect('blank')  # You need to define the URL name for the error page


# delete data from accept_inq page
def delete_data_accept(request, data_id):
    try:
        # Retrieve the object from the database
        data = enquiry.objects.get(id=data_id)
        # Delete the object
        data.delete()
        # Redirect to a success page, or a page displaying the remaining data
        return redirect('accept_inq')  # You need to define the URL name for the success page
    except enquiry.DoesNotExist:
        # Handle the case where the object does not exist
        return redirect('accept_inq')  




# accept inquery 
    


def accept_inquiry(request, inquiry_id):
    inquiry = enquiry.objects.get(id=inquiry_id)
    inquiry.accepted = True
    inquiry.save()
    return redirect('blank')



def accepted_inquiries(request):
    accepted_inquiries = enquiry.objects.filter(accepted=True)
    return render(request, 'accept_inq.html', {'accepted_inquiries': accepted_inquiries})




