from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.db.models import Count, Q
from .models import Complaint
from django.shortcuts import render, redirect
from django.http import HttpResponse
from complaint.forms import ComplaintForm,statusupdate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from datetime import datetime
#page loading.
def index(request):
    return render(request,"complaint/home.html")



#get the count of all the submitted complaints,solved,unsolved.
def counter(request):
        total=Complaint.objects.all().count()
        unsolved=Complaint.objects.all().exclude(status='1').count()
        solved=Complaint.objects.all().exclude(Q(status='3') | Q(status='2')).count()
        dataset=Complaint.objects.values('Type_of_complaint').annotate(total=Count('status'),solved=Count('status', filter=Q(status='1')),
                  notsolved=Count('status', filter=Q(status='3')),inprogress=Count('status',filter=Q(status='2'))).order_by('Type_of_complaint')
        args={'total':total,'unsolved':unsolved,'solved':solved,'dataset':dataset,}
        return render(request,"complaint/counter.html",args)

def complaints(request):
  
    if request.method == 'POST':
        complaint_form=ComplaintForm(request.POST)
        if complaint_form.is_valid():
               instance=complaint_form.save(commit=False)
               instance.user=request.user
               mail=request.user.email
               print(mail)
               instance.save()
               return render(request,'complaint/comptotal.html',)
    else:
        
        complaint_form=ComplaintForm(request.POST)
    context={'complaint_form':complaint_form,}
    return render(request,'complaint/comptotal.html',context)
        


def list(request):
    c=Complaint.objects.filter(user=request.user).exclude(status='1')
    result=Complaint.objects.filter(user=request.user).exclude(Q(status='3') | Q(status='2'))
    #c=Complaint.objects.all()
    args={'c':c,'result':result}
    return render(request,'complaint/Complaints.html',args)

def slist(request):
    result=Complaint.objects.filter(user=request.user).exclude(Q(status='3') | Q(status='2'))
    #c=Complaint.objects.all()
    args={'result':result}
    return render(request,'complaint/solvedcomplaint.html',args)


def allcomplaints(request):
      
        
        c=Complaint.objects.all().exclude(status='1')
        comp=request.GET.get("search")
        drop=request.GET.get("drop")

        if drop:
                c=c.filter(Q(Type_of_complaint__icontains=drop))
        if comp:
                c=c.filter(Q(Type_of_complaint__icontains=comp)|Q(Description__icontains=comp)|Q(Subject__icontains=comp))
        if request.method=='POST':
                cid=request.POST.get('cid2')
                uid=request.POST.get('uid')
                print(uid)
                project = Complaint.objects.get(id=cid)
                
                forms=statusupdate(request.POST,instance=project)
                if forms.is_valid():
                        
                        obj=forms.save(commit=False)
                        mail = User.objects.filter(id=uid)
                        for i in mail:
                                m=i.email
                       
                      
                        print(m)
                        send_mail('Hi, Complaint has been Resolved ', 'Thanks for letting us know of your concern, Hope we have solved your issue. Dont Reply to this mail', 'testerpython13@gmail.com', [m],fail_silently=False)
                        obj.save()
                        messages.add_message(request,messages.SUCCESS, f'Complaint Updated!!!')
                        return HttpResponseRedirect(reverse('allcomplaints'))
                else:
                        return render(request,'complaint/AllComplaints.html')
                 #testing

        else:
                forms=statusupdate()
        #c=Complaint.objects.all().exclude(status='1')
           
        args={'c':c,'forms':forms,'comp':comp}
        return render(request,'complaint/allcomplaints.html',args)


def solved(request):
        
        cid=request.POST.get('cid2')
        c=Complaint.objects.all().exclude(Q(status='3') | Q(status='2'))
        comp=request.GET.get("search")
        drop=request.GET.get("drop")

        if drop:
                c=c.filter(Q(Type_of_complaint__icontains=drop))
        if comp:
               
                c=c.filter(Q(Type_of_complaint__icontains=comp)|Q(Description__icontains=comp)|Q(Subject__icontains=comp))
        if request.method=='POST':
                cid=request.POST.get('cid2')
                print(cid)
                project = Complaint.objects.get(id=cid)
                forms=statusupdate(request.POST,instance=project)
                if forms.is_valid():
                        
                        obj=forms.save(commit=False)
                        obj.save()
                        messages.add_message(request,messages.SUCCESS, f'Complaint Updated!!!')
                        return HttpResponseRedirect(reverse('solved'))
                else:
                        return render(request,'complaint/solved.html')
                 #testing

        else:
                forms=statusupdate()
        #c=Complaint.objects.all().exclude(Q(status='3') | Q(status='2'))
        
        args={'c':c,'forms':forms,'comp':comp}
        return render(request,'complaint/solved.html',args)

def pdf_viewer(request):
    detail_string={}
    #detailname={}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Complaint_id.pdf'
    p = canvas.Canvas(response,pagesize=A4)
    
    cid=request.POST.get('cid')
    uid=request.POST.get('uid')
    #print(cid)
    
    details = Complaint.objects.filter(id=cid).values('Description')
    name = Complaint.objects.filter(id=cid).values('user_id')
    '''Branch = Complaint.objects.filter(id=cid).values('Branch')'''
    Subject = Complaint.objects.filter(id=cid).values('Subject')
    Type = Complaint.objects.filter(id=cid).values('Type_of_complaint')
    Issuedate = Complaint.objects.filter(id=cid).values('Time')
    #date_format1 = "%Y-%m-%d %H:%M:%S.%f%z"
   
    
    for val in details:
            detail_string=("{}".format(val['Description']))
    for val in name:
           detailname=("User: {}".format(val['user_id']))
    '''for val in Branch:
            detailbranch=("Branch: {}".format(val['Branch']))'''
    for val in Subject:
            detailsubject=("Subject: {}".format(val['Subject']))
    for val in Type:
            detailtype=("{}".format(val['Type_of_complaint']))
            
    for val in Issuedate:
            ptime=("{}".format(val['Time']))
            detailtime=("Time of Issue/ Time of Solved: {}".format(val['Time']))
    #detail_string = u", ".join(("Desc={}".format(val['Description'])) for val in details) 
    date_format = "%Y-%m-%d"
    a = datetime.strptime(str(datetime.datetime.now().date()), date_format)
    b = datetime.strptime(str(ptime), date_format)
    delta = a - b
    print(b)
    print(a)
    print (delta.days )       
    if detailtype=='1':
            detailtype="Type of Complaint: ClassRoom"
    if detailtype=='3':
            detailtype="Type of Complaint: Management"
    if detailtype=='2':
            detailtype="Type of Complaint: Teacher"
    if detailtype=='4':
            detailtype="Type of Complaint: School"
    if detailtype=='5':
            detailtype="Type of Complaint: Other"

    p.drawString(25, 770,"Report:")
    p.drawString(30, 750,detailname)
    ''' p.drawString(30, 730,detailbranch)'''
    p.drawString(30, 710,detailtype)
    p.drawString(30, 690,detailtime)
    p.drawString(30, 670,detailsubject)
    p.drawString(30, 650,"Description:")
    p.drawString(30, 630,detail_string)

    p.showPage()
    p.save()
    return response


def pdf_view(request):
    detail_string={}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=complaint_id.pdf'
    
    p = canvas.Canvas(response,pagesize=A4)
    cid=request.POST.get('cid')
    #print(cid)
    details = Complaint.objects.filter(id=cid).values('Description')
    name = User.objects.filter(username=request.user.username).values('username')
    #Branch = Complaint.objects.filter(id=cid).values('Branch')
    Subject = Complaint.objects.filter(id=cid).values('Subject')
    Type = Complaint.objects.filter(id=cid).values('Type_of_complaint')
    Issuedate = Complaint.objects.filter(id=cid).values('Time')

    for val in details:
            detail_string=("{}".format(val['Description']))
    for val in name:
            detailname=("User: {}".format(val['username']))
    #for val in Branch:
            #detailbranch=("Branch: {}".format(val['Branch']))
    for val in Subject:
            detailsubject=("Subject: {}".format(val['Subject']))
    for val in Type:
            detailtype=("{}".format(val['Type_of_complaint']))
            
    for val in Issuedate:
            detailtime=("Time of Issue: {}".format(val['Time']))
    #detail_string = u", ".join(("Desc={}".format(val['Description'])) for val in details) 

    if detailtype=='1':
            detailtype="Type of Complaint: ClassRoom"
    if detailtype=='3':
            detailtype="Type of Complaint: Management"
    if detailtype=='2':
            detailtype="Type of Complaint: Teacher"
    if detailtype=='4':
            detailtype="Type of Complaint: School"
    if detailtype=='5':
            detailtype="Type of Complaint: Other"

    p.drawString(25, 770,"Report:")
    p.drawString(30, 750,detailname)
    #p.drawString(30, 730,detailbranch)
    p.drawString(30, 710,detailtype)
    p.drawString(30, 690,detailtime)
    p.drawString(30, 670,detailsubject)
    p.drawString(30, 650,"Description:")
    p.drawString(30, 630,detail_string)

    p.showPage()
    p.save()
    return response




             

