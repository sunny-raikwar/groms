from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import (
    StaffUser, CustomerDetail, AgentDetail, NominiDetail, AgentType,
    AgentAccount, ProjectDetail, PlotDetail)


# Create your views here.
def index(request):
    return render(request, 'grom/index.html')


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
    return render(request, 'grom/dashboard.html')


def clearsession(request):
    request.session.flush()
    return HttpResponseRedirect('/')


def staffmember(request):
    members = StaffUser.objects.all()
    return render(request, 'grom/staffmember.html', {'members': members})


def add_staffmember_page(request):
    return render(request, 'grom/add_staffmember_page.html')


def add_staffmember(request):
    url = request.POST['url']
    full_name = request.POST['full_name']
    login_id = request.POST['login_id']
    password = request.POST['password']
    address = request.POST['address']
    contact_no = request.POST['contact_no']
    alt_contact_no = request.POST['alt_contact_no']
    try:
        member = StaffUser.objects.get(loginid=login_id)
        return HttpResponseRedirect(url)
    except:
        StaffUser.objects.create(loginid=login_id, password=password, fullname=full_name,
                                 contact_no=contact_no, alternate_contact_no=alt_contact_no, address=address)
    return HttpResponseRedirect('/staffmember/')


def delete_staffmember(request, member_id):
    member = StaffUser.objects.get(id=member_id)
    member.delete()
    return HttpResponseRedirect('/staffmember/')


def edit_staffmember_page(request, member_id):
    member = StaffUser.objects.get(id=member_id)
    return render(request, 'grom/edit_staffmember_page.html', {'member': member})


def edit_staffmember(request, member_id):
    full_name = (request.POST['full_name']).strip()
    login_id = (request.POST['login_id']).strip()
    password = (request.POST['password']).strip()
    address = (request.POST['address']).strip()
    contact_no = (request.POST['contact_no']).strip()
    alt_contact_no = (request.POST['alt_contact_no']).strip()
    StaffUser.objects.filter(id=member_id).update(loginid=login_id, password=password, fullname=full_name,
                                                  contact_no=contact_no, alternate_contact_no=alt_contact_no, address=address)
    return HttpResponseRedirect('/staffmember/')


def staffmember_detail(request, member_id):
    member = StaffUser.objects.get(id=member_id)
    return render(request, 'grom/staffmember_detail.html', {'member': member})


def agentinfo(request):
    agent_list = AgentDetail.objects.all()
    context = {'agent_list': agent_list}
    return render(request, 'grom/agentinfo.html', context)


def add_agent_page(request):
    introducers = AgentDetail.objects.all()
    nomini_list = NominiDetail.objects.all()
    agent_types = AgentType.objects.all()
    account_list = AgentAccount.objects.all()
    context = {'introducers': introducers, 'nomini_list': nomini_list,
               'agent_types': agent_types, 'account_list': account_list}
    return render(request, 'grom/add_agent_page.html', context)


def add_agent(request):
    url = request.POST['url']
    first_name = request.POST['first_name']
    middle_name = request.POST['middle_name']
    last_name = request.POST['last_name']
    father_name = request.POST['father_name']
    mother_name = request.POST['mother_name']
    pancard = request.POST['pancard']
    address = request.POST['address']
    date_of_birth = request.POST['dob']
    contact_no = request.POST['contact_no']
    alternate_contact_no = request.POST['alt_contact_no']
    email = request.POST['email']
    date_of_joining = request.POST['date_of_joining']
    percentage_alloted = request.POST['percentage_alloted']
    nomini_id = NominiDetail.objects.get(id=request.POST['nomini'])
    type_id = AgentType.objects.get(id=request.POST['agent_type'])
    account_id = AgentAccount.objects.get(id=request.POST['account'])
    image = request.FILES['image']
    try:
        introducor_id = AgentDetail.objects.get(id=request.POST['introducer'])
        introducer_percentage = request.POST['introducer_percentage']
        AgentDetail.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name,
                                   father_name=father_name, mother_name=mother_name, pancard=pancard, address=address,
                                   date_of_birth=date_of_birth, contact_no=contact_no, alternate_contact_no=alternate_contact_no,
                                   email=email, date_of_joining=date_of_joining, percentage_alloted=percentage_alloted,
                                   nomini_id=nomini_id, type_id=type_id, introducor_id=introducor_id,
                                   introducer_percentage=introducer_percentage, account_id=account_id, image=image)
    except:
        AgentDetail.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name,
                                   father_name=father_name, mother_name=mother_name, pancard=pancard, address=address,
                                   date_of_birth=date_of_birth, contact_no=contact_no, alternate_contact_no=alternate_contact_no,
                                   email=email, date_of_joining=date_of_joining, percentage_alloted=percentage_alloted,
                                   nomini_id=nomini_id, type_id=type_id, account_id=account_id)
    return HttpResponseRedirect('/agentinfo/')


def edit_agent_page(request, agent_id):
    introducers = AgentDetail.objects.all()
    nomini_list = NominiDetail.objects.all()
    agent_types = AgentType.objects.all()
    account_list = AgentAccount.objects.all()
    agent = AgentDetail.objects.get(id=agent_id)
    context = {'introducers': introducers, 'nomini_list': nomini_list,
               'agent_types': agent_types, 'account_list': account_list, 'agent': agent}
    return render(request, 'grom/edit_agent_page.html', context)


def edit_agent(request, agent_id):
    url = request.POST['url']
    first_name = request.POST['first_name']
    middle_name = request.POST['middle_name']
    last_name = request.POST['last_name']
    father_name = request.POST['father_name']
    mother_name = request.POST['mother_name']
    pancard = request.POST['pancard']
    address = request.POST['address']
    date_of_birth = request.POST['dob']
    contact_no = request.POST['contact_no']
    alternate_contact_no = request.POST['alt_contact_no']
    email = request.POST['email']
    date_of_joining = request.POST['date_of_joining']
    percentage_alloted = request.POST['percentage_alloted']
    nomini_id = NominiDetail.objects.get(id=request.POST['nomini'])
    type_id = AgentType.objects.get(id=request.POST['agent_type'])
    account_id = AgentAccount.objects.get(id=request.POST['account'])
    try:
        introducor_id = AgentDetail.objects.get(id=request.POST['introducer'])
        introducer_percentage = request.POST['introducer_percentage']
        AgentDetail.objects.filter(id=agent_id).update(
            first_name=first_name, middle_name=middle_name, last_name=last_name,
            father_name=father_name, mother_name=mother_name, pancard=pancard, address=address,
            date_of_birth=date_of_birth, contact_no=contact_no, alternate_contact_no=alternate_contact_no,
            email=email, date_of_joining=date_of_joining, percentage_alloted=percentage_alloted,
            nomini_id=nomini_id, type_id=type_id, introducor_id=introducor_id,
            introducer_percentage=introducer_percentage, account_id=account_id)
    except:
        AgentDetail.objects.filter(id=agent_id).update(
            first_name=first_name, middle_name=middle_name, last_name=last_name,
            father_name=father_name, mother_name=mother_name, pancard=pancard, address=address,
            date_of_birth=date_of_birth, contact_no=contact_no, alternate_contact_no=alternate_contact_no,
            email=email, date_of_joining=date_of_joining, percentage_alloted=percentage_alloted,
            nomini_id=nomini_id, type_id=type_id, account_id=account_id)
    return HttpResponseRedirect('/agentinfo/')


def delete_agent(request, agent_id):
    agent = AgentDetail.objects.get(id=agent_id)
    agent.delete()
    return HttpResponseRedirect('/agentinfo/')


def agent_detail(request, agent_id):
    agent = AgentDetail.objects.get(id=agent_id)
    return render(request, 'grom/agent_detail.html', {'agent': agent})


def customer(request):
    customers = CustomerDetail.objects.all()
    return render(request, 'grom/dashboard.html', {'customers': customers})


def add_customer_page(request):
    return render(request, 'grom/add_customer_page.html')


def add_customer(request):
    url = request.POST['url']
    first_name = request.POST['first_name']
    middle_name = request.POST['middle_name']
    last_name = request.POST['last_name']
    date_of_birth = request.POST['date_of_birth']
    pancard = request.POST['pancard']
    address = request.POST['address']
    contact_no = request.POST['contact_no']
    alt_contact_no = request.POST['alt_contact_no']
    email = request.POST['email']
    gender = request.POST['gender']
    date_of_joining = request.POST['date_of_joining']

    try:
        customer = CustomerDetail.objects.get(pancard=pancard)
        return HttpResponseRedirect(url)
    except:
        CustomerDetail.objects.create(pancard=pancard, first_name=first_name, middle_name=middle_name, last_name=last_name, date_of_birth=date_of_birth,
                                      contact_no=contact_no, alternate_contact_no=alt_contact_no, address=address, email=email, gender=gender, date_of_joining=date_of_joining)
    return HttpResponseRedirect('/customer/')


def plots(request):
    plots = PlotDetail.objects.all()
    return render(request, 'grom/plots.html', {'plots': plots})


def projects(request):
    projects = ProjectDetail.objects.all()
    return render(request, 'grom/projects.html', {'projects': projects})


def billing(request):
    return render(request, 'grom/billing.html')