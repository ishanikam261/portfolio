from django.shortcuts import  render , HttpResponse

def index(request):

   return render(request, template_name='website/index.html')
