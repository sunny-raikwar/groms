from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import (StaffUser)


# Create your views here.
def index(request):
	return render(request,'grom/index.html')


def login(request):
    url = request.POST['url']
    loginid = request.POST['id']
    password = request.POST['password']
    try:
        userstored = StaffUser.objects.get(loginid=loginid)
        if password == userstored.password:
            user = {}
            user['full_name'] = userstored.fullname
            user['loginid'] = userstored.loginid
            user['contact_no'] = userstored.contact_no
            request.session['user'] = user
            return HttpResponseRedirect('/dashboard/')
        else:
            request.session['userinvaild'] = "true"
    except:
        request.session['userinvaild'] = "true"
    return HttpResponseRedirect(url)


def dashboard(request):
	return render(request,'grom/dashboard.html')


def clearsession(request):
	request.session.flush()
	return HttpResponseRedirect('/')


def staffmember(request):
	members = StaffUser.objects.all()
	return render (request,'grom/staffmember.html', {'members':members})


def add_staffmember_page(request):
	return render(request,'grom/add_staffmember_page.html')


def add_staffmember(request):
	url = request.POST['url']
	full_name = request.POST['full_name']
	login_id = request.POST['login_id']
	password = request.POST['password']
	address = request.POST['address']
	contact_no = request.POST['contact_no']
	alt_contact_no = request.POST['alt_contact_no']
	try:
		member = StaffUser.objects.get(loginid = login_id)
		return HttpResponseRedirect(url)
	except:
		StaffUser.objects.create(loginid = login_id, password = password,fullname = full_name,
			contact_no = contact_no, alternate_contact_no = alt_contact_no,address = address)
	return HttpResponseRedirect('/staffmember/')


def delete_staffmember(request,member_id):
	member = StaffUser.objects.get(id = member_id)
	member.delete()
	return HttpResponseRedirect('/staffmember/')	


def edit_staffmember_page(request,member_id):
	member = StaffUser.objects.get(id = member_id)
	return render(request,'grom/edit_staffmember_page.html', {'member':member} )


def edit_staffmember(request,member_id):
	full_name = request.POST['full_name']
	login_id = request.POST['login_id']
	password = request.POST['password']
	address = request.POST['address']
	contact_no = request.POST['contact_no']
	alt_contact_no = request.POST['alt_contact_no']
	StaffUser.objects.filter(id = member_id).update(loginid = login_id, password = password,fullname = full_name,
			contact_no = contact_no, alternate_contact_no = alt_contact_no,address = address)
	return HttpResponseRedirect('/staffmember/')