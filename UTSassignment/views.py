from django.shortcuts import render
from django.http import HttpResponse
from .forms import ChatForm  # Import the ChatForm

def index(request):
    return HttpResponse ("Hello User")

def brain(request): 
    return HttpResponse ("Hello Brian!")

def send_message_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            # Here, you can process the message (e.g., save it to the database)
            return HttpResponse("Message sent successfully!")
    else:
        form = ChatForm()
    
    return render(request, 'send_message.html', {'form': form})
