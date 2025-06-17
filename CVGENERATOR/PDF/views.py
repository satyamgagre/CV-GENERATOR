from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.

def accept(request):

    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work = request.POST.get("previous_work","")
        skills = request.POST.get("skills","")

        profile = Profile(
                        name=name,
                        email=email,
                        phone=phone,
                        summary=summary,
                        degree=degree,
                        school=school,
                        university=university,
                        previous_work=previous_work,
                        skills=skills
                    )
        profile.save() 

    return render(request, 'PDF/accept.html')  

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template =loader.get_template('PDF/resume.html')
    html = template.render({'user_profile':user_profile})
    
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }

    # ✅ Paste this block here
    path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    # Generate PDF using the specified wkhtmltopdf path
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)

    filename = "resume.pdf"  
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response

def list(request):
    profile = Profile.objects.all()
    return render(request,"PDF/list.html",{'profile':profile})