from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Home(request):
    speaker={"Person1":{ "id":1, "names":"IRUMVA Patrick","Role":"Host", "Email":"irupatrick253@gmail.com","Phone":"+250782471347","Country":"Rwandan"},
        "Persnal2":{"id":2, "names":"IRIHOSE Eric","Role":"Dean", "Email":"eric@mail.com", "Phone":"078000000", "Country":"Ugandan"}, }
    return render(request,'index.html',{'data':speaker})

def Ident(request,id):
    speaker={"Person1":{ "id":1, "names":"IRUMVA Patrick","Role":"Host", "Email":"irupatrick253@gmail.com","Phone":"+250782471347","Country":"Rwandan" },
        "Persnal2":{"id":2, "names":"IRIHOSE Eric","Role":"Dean", "Email":"eric@mail.com", "Phone":"078000000", "Country":"Ugandan"}, }
    data=speaker.get(id)

  
    return render(request,'identity.html',{'person':data})

def Register(request):
    return render(request,"Register.html")

def Update(request,id):
    speaker={"Person1":{ "id":1, "names":"IRUMVA Patrick","Role":"Host", "Email":"irupatrick253@gmail.com","Phone":"+250782471347", "Country":"Rwandan"},
        "Persnal2":{"id":2, "names":"IRIHOSE Eric","Role":"Dean", "Email":"eric@mail.com", "Phone":"078000000", "Country":"Burundian"}, }
    
    data=speaker.get(id)
    return render(request,'update.html',{'person':data})

def Delete(request,id):
    speaker={"Person1":{ "id":1, "names":"IRUMVA Patrick","Role":"Host", "Email":"irupatrick253@gmail.com","Phone":"+250782471347","Country":"Rwandan" },
        "Persnal2":{"id":2, "names":"IRIHOSE Eric","Role":"Dean", "Email":"eric@mail.com", "Phone":"078000000", "Country":"Burundian"}, }
    
    datas=speaker.get(id)
    return render(request,'delete.html',{'person':datas})
