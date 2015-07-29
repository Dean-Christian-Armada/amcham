try:
    from crew_viewer.asynchronous_mail import send_mail
except:
    from django.core.mail import send_mail
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from django.conf import settings
from .models import *
# Create your views here.

def navigation_autocomplete(request):
    q = request.GET.get('q', '')
    position = '';
    citizenship = '';
    company = '';
    gender = '';
    blood_type = '';
    suffix = '';
    city = '';
    country = '';
    state = '';
    nationality = ''; 

    if q:
    	first_name = Q(first_name__icontains=q)
        last_name = Q(last_name__icontains=q)
        company = Q(company__company__icontains=q)
        mobile = Q(mobile__icontains=q)
        telephone = Q(telephone__icontains=q)
        fax = Q(fax__icontains=q)
        personal_email = Q(personal_email__email__icontains=q)
        company_email = Q(company_email__email__icontains=q)

        
        members = Member.objects.filter(
            first_name |
            last_name |
            company |
            mobile |
            telephone |
            fax |
            personal_email |
            company_email
        ).distinct()

        if request.GET.get('position'):
        	position = request.GET.get('position')
        	members = app.filter(position__position__exact=position)
		if request.GET.get('citizenship'):
			citizenship = request.GET.get('citizenship')
			members = app.filter(citizenship__nationality__exact=citizenship)
		if request.GET.get('company'):
			company = request.GET.get('company')
			members = app.filter(company__company__exact=company)
		if request.GET.get('gender'):
			gender = request.GET.get('gender')
			members = app.filter(gender__gender__exact=gender)
		if request.GET.get('blood_type'):
			blood_type = request.GET.get('blood_type')
			members = app.filter(blood_type__blood_type__exact=blood_type)
		if request.GET.get('suffix'):
			suffix = request.GET.get('suffix')
			members = app.filter(suffix__suffix__exact=suffix)
		if request.GET.get('city'):
			city = request.GET.get('city')
			members = app.filter(company__city__city__exact=city)
		if request.GET.get('country'):
			country = request.GET.get('country')
			members = app.filter(company__country__country__exact=country)
		if request.GET.get('state'):
			state = request.GET.get('state')
			members = app.filter(company__state__state__exact=state)
		if request.GET.get('postal_code'):
			postal_code = request.GET.get('postal_code')
			members = app.filter(company__postal_code__postal_code__exact=postal_code)
		if request.GET.get('nationality'):
			nationality = request.GET.get('nationality')
			members = app.filter(company__nationality__nationality__exact=nationality)

        template='staff/autocomplete.html'
        context_dict = {'members': members}
        return render(request, template, context_dict)
    else:
        pass