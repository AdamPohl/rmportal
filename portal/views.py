from urllib.request import HTTPRedirectHandler
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import School, User

def index(request):
    open_schools = School.objects.filter(status="Open")
    template = loader.get_template("portal/index.html")
    context = {'open_schools_list': [{'urn': school.urn, 'name': school.name} for school in open_schools]}

    return HttpResponse(template.render(context, request))


def auth_view(request):
    username = request.POST.get('username', '')
    school_id = request.POST.get('school', '')
    user = User.objects.get(
        Q(email=username) & Q(school=school_id)
    )

    if user is not None:
        school = School.objects.get(urn=school_id)
        template = loader.get_template("portal/welcome.html")
        context = {
            'name': user.name,
            'surname': user.surname,
            'school': school,
        }

        return HttpResponse(template.render(context, request))

def logout(request):
    return HttpResponseRedirect('portal/')

def create_user(request):
    name = request.POST.get('name', '')
    surname = request.POST.get('surname', '')
    email = request.POST.get('email', '')
    school_id = request.POST.get('school', '')
    dob = request.POST.get('dob', '')

    User.objects.create(
        name=name,
        surname=surname,
        email=email,
        school=school_id,
        dob=dob
    )

    school = School.objects.get(urn=school_id)
    template = loader.get_template("portal/welcome.html")
    context = {
        'name': name,
        'surname': surname,
        'school': school,
    }

    return HttpResponse(template.render(context, request))


def register_user(request):
    open_schools = School.objects.filter(status="Open")
    template = loader.get_template("portal/register.html")
    context = {'open_schools_list': [{'urn': school.urn, 'name': school.name} for school in open_schools]}

    return HttpResponse(template.render(context, request))


# Leaving this in as it was part of my original plan to have the registration & login views redirect to /welcome
# which would send it through to this view but I couldn't get the uiser to pass through so have resorted to
# rendiering the page myself in the end. This has sadly caused another issue that is that the URl is no longer
# /welcome but /user/auth or /create_user now annoyingly. I have solved this before but con not find it within
# the timelimit.

# def welcome_page(request):
#     username = request.GET.get('username', '')
#     user = User.objects.get(email=username)
#     school = School.objects.get(urn=user.school)

#     template = loader.get_template("portal/welcome.html")
#     context = {
#         'name': user.name,
#         'surname': user.surname,
#         'school': school,
#     }

#     return HttpResponse(template.render(context, request))