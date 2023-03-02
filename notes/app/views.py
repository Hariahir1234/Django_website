from django.shortcuts import render,redirect
from .models import notes
from .forms import notesnew
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def main(request):
    abc=notes.objects.all()
    return render(request,'mains.html',{'notesdetail':abc})




def uploadnotes(request):
    abc=notesnew()
    if request.method == 'POST':
        abc=notesnew(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('index')
        else:
            HttpResponse ('data is wrong')
    
    else:
        
        return render (request,'uploadnotes.html',{'upload_note':abc})        
    

    
def updatenotes(request,note_id):
    note_id=int(note_id)
    try:
        abc=notes.objects.get(id=note_id)
        
    except notes.DoesNotExist:
        return redirect ('index')
        
    xyz=notesnew(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('index')
         
    return render(request,'uploadnotes.html',{'upload_note':xyz})        
    

        
def deletenotes(request,note_id):
    note_id=int(note_id)
    try:
        abc=notes.objects.get(id=note_id)
    except notes.DoesNotExist:
        return redirect('index')
    abc.delete()
    return redirect ('index')
        
            
