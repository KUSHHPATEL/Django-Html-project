from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request,"home.html")
def aboutpage(request):
	return render(request,'about.html')
def contactpage(request):
	return render(request,'contact.html')
def formpageview(request):
	return render(request,'form.html')


    
def formpageprocess(request):
    a = int(request.POST["txt1"])
    b = int(request.POST["txt2"])
    c = a + b
    return  render(request,"ans.html",{'mya':a,'myb':b,'sum':c})





        
        

# Create your views here.