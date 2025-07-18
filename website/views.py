from django.shortcuts import  render , HttpResponse


def index(request):

   return render(request, template_name='website/index.html')


def about(request):

   return render(request, template_name='website/about.html')


def portfolio(request):
   
   return render(request, template_name='website/portfolio.html')


def resume(request):
   
   return render(request, template_name='website/resume.html')


def contact(request):
   
   return render(request, template_name='website/contact.html')


def starter_page(request):
   
   return render(request, template_name='website/starter-page.html')


def blog(request):
   
   return render(request, template_name='website/blog.html')

def project(request):
   
   return render(request, template_name='website/project.html')


