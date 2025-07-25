from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User  # Assuming you have a User model
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django import forms
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User
from django.shortcuts import render, redirect
from .models import User
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.shortcuts import render, redirect
import uuid
from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django import forms
from .models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from django.contrib.auth.models import User, Permission
from django.contrib.auth import login
import json
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Vehicle
from .serializers import VehicleSerializer
from .models import STS
from .serializers import STSSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import STS
from .serializers import STSSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Landfill
from .serializers import LandfillSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import STSEntry, STS, Vehicle, STSManager
import uuid
from rest_framework.parsers import JSONParser
from .serializers import LandfillManagerSerializer

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import LandfillManager, Landfill, User
from django.views.decorators.csrf import csrf_exempt
import uuid
from .serializers import LandfillManagerSerializer
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import STSManager, STS, User
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import STSSerializer, UserSerializer


from .serializers import STSSerializer

from django.shortcuts import redirect
from django.shortcuts import render, redirect, HttpResponse
from .models import LandfillEntry, Landfill, Vehicle, LandfillManager
import uuid
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import STSEntry, STS, Vehicle, STSManager
import uuid
from rest_framework.parsers import JSONParser
from .serializers import LandfillManagerSerializer

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import LandfillManager, Landfill, User
from django.views.decorators.csrf import csrf_exempt
import uuid
from .serializers import LandfillManagerSerializer
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import STSManager, STS, User
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import STSSerializer, UserSerializer


from .serializers import STSSerializer

from django.shortcuts import redirect

from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle

from django.shortcuts import render
from .models import Vehicle
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Vehicle

from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Vehicle
from datetime import datetime


from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Vehicle

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Vehicle
from datetime import datetime
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Vehicle
from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Vehicle
from datetime import datetime, timedelta
from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Vehicle
from datetime import datetime, timedelta
from django.http import HttpResponse
from reportlab.pdfgen import canvas



# Create your views here.


def index(request):
    return render(request, "index.html")


class SignupForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    gmail = forms.EmailField(label="Gmail")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            gmail = form.cleaned_data["gmail"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if password1 == password2:
                user = User.objects.create_user(
                    username=gmail, email=gmail, password=password1,
                    first_name=first_name, last_name=last_name
                )
                user.role = "admin"
                user.save()
                login(request, user)
                return redirect("dashboard")
            else:
                error = "Passwords do not match."
                return render(request, "signup.html", {"form": form, "error": error})
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})



User = get_user_model()


from django.contrib.auth import logout

@login_required

def logout_view(request):
    logout(request)
    return redirect("/")


from django.shortcuts import render, redirect

@login_required
def dashboard(request):
    if request.user.role != "admin":
        return redirect("index")

    user_info = {
        "id": request.user.user_id,
        "role": request.user.role,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
    }
    
    return render(request, "dashboard.html", {"user_info": user_info})


@login_required
def adminprofile(request):
    if request.user.role != "admin":
        return redirect("index")

    user_info = {
        "id": request.user.user_id,
        "role": request.user.role,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
    }
    return render(request,'adminprofile.html', {"user_info": user_info})



@login_required
def change_password_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("new_login")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {"form": form})


def generate_custom_id():

    return str(uuid.uuid4())

@login_required
@csrf_exempt
def create_new_user(request):
    if request.method == "POST":

        if request.META.get("CONTENT_TYPE") == "application/json":
            data = json.loads(request.body)

            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()
                user.role = data.get("role", user.role)

                if data.get("permissions") == "read":
                    read_permission = Permission.objects.get(codename="view_user_roles")
                    user.user_permissions.add(read_permission)

                user.save()

                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)

        else:
            role = request.POST.get("role")
            email = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            password = request.POST.get("password")
            permissions = request.POST.get("permissions")

            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            user.role = role if role else user.role

            if permissions == "read":
                read_permission = Permission.objects.get(codename="view_user_roles")
                user.user_permissions.add(read_permission)

            user.save()
            login(request, user)
            return redirect("dashboard")

    else:
        return render(request, "create_new_user.html")


User = get_user_model()



def new_login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)

            if user.role == "admin":
                return redirect("dashboard")
            elif user.role == "sts_manager":
                return redirect("sts_manager")
            elif user.role == "landfill_manager":
                return redirect("landfill_manager")
            elif user.role == "unassigned":
                return redirect("unassigned")
            else:

                return redirect("dashboard")
        else:
            error = "Invalid email or password."
            return render(request, "newlogin.html", {"error": error})
    else:
        return render(request, "newlogin.html")

@login_required

def see_all_user(request):

    users = User.objects.all()
    return render(request, "see_all_user.html", {"users": users})


@login_required
def datale_user(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")

        try:
            user = User.objects.get(user_id=user_id)
            user.delete()
            return redirect("datale_user")
        except User.DoesNotExist:
            pass

    users = User.objects.all()
    return render(request, "datale_user.html", {"users": users})


@login_required
def update_user_name(request):
    if request.method == "POST":
        for user in User.objects.all():
            user_id = user.user_id
         
            first_name = request.POST.get(f"first_name{user_id}")
            last_name = request.POST.get(f"last_name{user_id}")

            user_obj = User.objects.get(user_id=user_id)
           
            user_obj.first_name = first_name
            user_obj.last_name = last_name
            user_obj.save()

        return redirect("update_user_name")

    users = User.objects.all()
    return render(request, "update_user_name.html", {"users": users})


@login_required
def change_user_roll(request):
    if request.method == "POST":
        for user in User.objects.all():

            new_role_key = f"role{user.user_id}"
            new_role = request.POST.get(new_role_key, None)

            if new_role:
                user.role = new_role
                user.save()

        return redirect("change_user_roll")

    users = User.objects.all()
    roles = User.ROLES
    return render(request, "change_user_roll.html", {"users": users, "roles": roles})

@login_required

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            return redirect("dashboard")
        else:

            return render(request, "change_passwords.html", {"form": form})
    else:

        form = PasswordChangeForm(request.user)
        return render(request, "change_passwords.html", {"form": form})


def vehiclesuccess(request):
    return render(request, "vehicle_success.html")


def success(request):
    return render(request, "success.html")


@login_required

@csrf_exempt
def vehicle_create(request):
    if request.method == "POST":
        form_data = request.POST
        registration_number = form_data.get("registration_number")
        
        # Check if a vehicle with the same registration number already exists
        if Vehicle.objects.filter(registration_number=registration_number).exists():
            return render(request, "vehicle.html", {"error_message": "Registration number already existing in database"})
        
        vehicle = Vehicle(
            registration_number=registration_number,
            type=form_data.get("type"),
            capacity=form_data.get("capacity"),
            fuel_cost_loaded=form_data.get("fuel_cost_loaded"),
            fuel_cost_unloaded=form_data.get("fuel_cost_unloaded"),
        )

        serializer = VehicleSerializer(vehicle, data=form_data)
        if serializer.is_valid():
            serializer.save()
            return redirect("vehiclesuccess")
        else:
            return HttpResponse(serializer.errors, status=400)
    else:
        return render(request, "vehicle.html")

@login_required

@csrf_exempt
def sts_create(request):
    if request.method == "POST":

        form_data = {
            "ward_number": request.POST.get("ward_number"),
            "capacity": request.POST.get("capacity"),
            "latitude": request.POST.get("latitude"),
            "longitude": request.POST.get("longitude"),
        }

        serializer = STSSerializer(data=form_data)
        if serializer.is_valid():
            serializer.save()
            return redirect("success")
        else:
            return HttpResponse(serializer.errors, status=400)
    else:
        return render(request, "sts_create.html")


@login_required
@csrf_exempt
def landfill_create(request):
    if request.method == "POST":
        form_data = {
            "capacity": request.POST.get("capacity"),
            "operational_timespan": request.POST.get("operational_timespan"),
            "latitude": request.POST.get("latitude"),
            "longitude": request.POST.get("longitude"),
        }
        serializer = LandfillSerializer(data=form_data)
        if serializer.is_valid():
            serializer.save()
            return redirect("success")
        else:
            return HttpResponse(serializer.errors, status=400)
    else:
        return render(request, "landfill_create.html")


@login_required
@csrf_exempt
def sts_manager_create(request):
    if request.method == "POST":
        user_id = request.POST.get("user")
        sts_id = request.POST.get("sts")

        try:
            user = User.objects.get(id=user_id)
            sts = STS.objects.get(sts_id=sts_id)

            STSManager.objects.create(user=user, sts=sts)

           
            serializer = STSSerializer(sts)
            serialized_data = serializer.data

            return redirect("success")
        except ValueError as e:
            return HttpResponse(f"Invalid UUID format: {e}", status=400)
        except User.DoesNotExist:
            return HttpResponse("User not found.", status=404)
        except STS.DoesNotExist:
            return HttpResponse("STS not found.", status=404)
        except Exception as e:
            return HttpResponse(f"Error creating STS Manager: {e}", status=400)
    else:
        context = {"sts_list": STS.objects.all(), "user_list": User.objects.all()}
        return render(request, "sts_manager_create.html", context)

@login_required

def landfill_manager_create(request):
    if request.method == "POST":
        user_id = request.POST.get("user")
        landfill_id = request.POST.get("landfill")

        try:
            user = User.objects.get(id=user_id)
            landfill = Landfill.objects.get(landfill_id=landfill_id)

            LandfillManager.objects.create(user=user, landfill=landfill)
            return redirect("success")
        except User.DoesNotExist:
            return HttpResponse("User not found.", status=404)
        except Landfill.DoesNotExist:
            return HttpResponse("Landfill not found.", status=404)
        except Exception as e:
            return HttpResponse(f"Error creating Landfill Manager: {e}", status=500)
    else:
        context = {
            "landfill_list": Landfill.objects.all(),
            "user_list": User.objects.all(),
        }
        return render(request, "landfill_manager_create.html", context)



@login_required
@csrf_exempt
def create_sts_entry(request):
    if request.method == "POST":
        sts_id = request.POST.get("sts")
        vehicle_id = request.POST.get("vehicle")
        sts_manager_id = request.POST.get("sts_manager")
        weight_of_waste = request.POST.get("weight_of_waste")
        time_of_arrival = request.POST.get("time_of_arrival")
        time_of_departure = request.POST.get("time_of_departure")

        try:
            sts = STS.objects.get(sts_id=(sts_id))
            vehicle = Vehicle.objects.get(vehicle_id=(vehicle_id))
            sts_manager = STSManager.objects.get(
                sts_manager_id=uuid.UUID(sts_manager_id)
            )

            STSEntry.objects.create(
                sts=sts,
                vehicle=vehicle,
                sts_manager=sts_manager,
                weight_of_waste=weight_of_waste,
                time_of_arrival=time_of_arrival,
                time_of_departure=time_of_departure,
            )
            return redirect("success")
        except Exception as e:
            return HttpResponse(f"Error creating STS Entry: {e}", status=400)
    else:
        context = {
            "sts_list": STS.objects.all(),
            "vehicle_list": Vehicle.objects.all(),
            "sts_manager_list": STSManager.objects.all(),
        }
        return render(request, "create_sts_entry.html", context)


@login_required
@csrf_exempt
def create_landfill_entry(request):
    if request.method == "POST":
        landfill_id = request.POST.get("landfill")
        vehicle_id = request.POST.get("vehicle")
        landfill_manager_id = request.POST.get("landfill_manager")
        weight_of_waste = request.POST.get("weight_of_waste")
        time_of_arrival = request.POST.get("time_of_arrival")
        time_of_departure = request.POST.get("time_of_departure")

        try:
            landfill = Landfill.objects.get(pk=(landfill_id))
            vehicle = Vehicle.objects.get(pk=(vehicle_id))
            landfill_manager = LandfillManager.objects.get(
                pk=uuid.UUID(landfill_manager_id)
            )

            LandfillEntry.objects.create(
                landfill=landfill,
                vehicle=vehicle,
                landfill_manager=landfill_manager,
                weight_of_waste=weight_of_waste,
                time_of_arrival=time_of_arrival,
                time_of_departure=time_of_departure,
            )
            return redirect("success")
        except Exception as e:
            return HttpResponse(f"Error creating Landfill Entry: {e}", status=400)
    else:
        context = {
            "landfill_list": Landfill.objects.all(),
            "vehicle_list": Vehicle.objects.all(),
            "landfill_manager_list": LandfillManager.objects.all(),
        }
        return render(request, "create_landfill_entry.html", context)


@login_required
def sts_manager(request):

    if request.user.role != "sts_manager":
        return redirect("index")

    user_info = {
        "id": request.user.user_id,
        "role": request.user.role,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
    }

    return render(request, "sts_manager.html", {"user_info": user_info})


@login_required
def landfill_manager(request):

    if request.user.role != "landfill_manager":
        return redirect("index")

    user_info = {
        "id": request.user.user_id,
        "role": request.user.role,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
    }

    return render(request, "landfill_manager.html", {"user_info": user_info})


@login_required
def unassigned(request):
    if request.user.role != "unassigned":
        return redirect("index")

    user_info = {
        "id": request.user.user_id,
        "role": request.user.role,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
    }

    return render(request, "unassigned.html", {"user_info": user_info})


from django.contrib import messages


User = get_user_model()


@login_required
def user_profile_update(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name", user.first_name)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.save()
        messages.success(request, "Profile successfully updated!")
        return redirect("user_profile_update")
    else:
        return render(request, "user_profile_update.html", {"user": request.user})


def see_all_role(request):
    return render(request, "see_all_role.html")



@login_required
def calculate_cost(request):
    context = {'vehicles': Vehicle.objects.all()} 

    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle_id')
        load_str = request.POST.get('load')

      
        vehicle_attempts = request.session.get('vehicle_attempts', {})

       
        if vehicle_id in vehicle_attempts:
            vehicle_attempts[vehicle_id] = [datetime.strptime(attempt, '%Y-%m-%d %H:%M:%S.%f') for attempt in vehicle_attempts[vehicle_id]]

        
        recent_attempts = [attempt for attempt in vehicle_attempts.get(vehicle_id, []) if attempt > datetime.now() - timedelta(days=1)]
        vehicle_attempts[vehicle_id] = [attempt.strftime('%Y-%m-%d %H:%M:%S.%f') for attempt in recent_attempts]

        if len(recent_attempts) >= 3:
        
            context['alert'] = "A vehicle can come up to 3 times in a day. Please try after 1 day."
        else:
            try:
                load = float(load_str)
                vehicle = Vehicle.objects.get(pk=vehicle_id)
                c_unloaded = float(vehicle.fuel_cost_unloaded)
                c_loaded = float(vehicle.fuel_cost_loaded)
                capacity = float(vehicle.capacity)

             
                cost_per_kilometer = round((c_unloaded + (load / capacity) * (c_loaded - c_unloaded)), 2)
                
              
                context.update({
                    'vehicle': vehicle,
                    'load': load,
                    'cost_per_kilometer': cost_per_kilometer,
                    'pdf_url': reverse('generate_pdf', kwargs={'vehicle_id': vehicle_id}) + f"?load={load}&cost_per_kilometer={cost_per_kilometer}"
                })

               
                vehicle_attempts[vehicle_id].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                request.session['vehicle_attempts'] = vehicle_attempts

            except (ValueError, Vehicle.DoesNotExist) as e:
                context['error'] = 'Invalid input or vehicle not found.'

    return render(request, 'billingview.html', context)





@login_required
def generate_pdf(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    load = request.GET.get('load', 'Not provided')
    cost_per_kilometer = request.GET.get('cost_per_kilometer', 'Not calculated')
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="vehicle_{vehicle_id}_slip.pdf"'
    
    p = canvas.Canvas(response)
    p.drawString(100, 800, f"Vehicle ID: {vehicle.vehicle_id}")
    p.drawString(100, 780, f"Vehicle REG NO: {vehicle.registration_number}")
    p.drawString(100, 760, f"Vehicle Type: {vehicle.get_type_display()}")
    p.drawString(100, 740, f"Load: {load} Ton")
    p.drawString(100, 720, f"Cost per Kilometer: {cost_per_kilometer} Taka")
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    p.drawString(100, 700, f"Timestamp: {now}")
    
    p.showPage()
    p.save()
    return response



@login_required
def control_users_persimmon  (request):
    return render(request,'control_users_persimmon.html') 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class allusers(APIView):
    def get(self,request):
        users = User.objects.all()
        serializeruser = UserSerializer(users,many = True).data
        return Response(
            {"user":serializeruser},status=status.HTTP_200_OK
        )
    def post(self,request ):
        data =  request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            user.role = data.get("role", user.role)

            if data.get("permissions") == "read":
                read_permission = Permission.objects.get(codename="view_user_roles")
                user.user_permissions.add(read_permission)

            user.save()
            return Response({'user':serializer.data},status=status.HTTP_201_CREATED)
        
class createuser(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            user.role = data.get("role", user.role)

            if data.get("permissions") == "read":
                read_permission = Permission.objects.get(codename="view_user_roles")
                user.user_permissions.add(read_permission)

            user.save()

        
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
           
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Getuser(APIView):
    def get(self,request ,pk):
        users = User.objects.get(pk=pk)
        serializeruser = UserSerializer(users,many = False).data
        return Response(
            {"user":serializeruser},status=status.HTTP_200_OK
        )






