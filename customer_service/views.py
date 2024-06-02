from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import  UserRegisterForm, ServiceRequestForm
from .models import Attachment, ServiceRequest


def home(request):
    return render(request, 'base_generic.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'customer_service/register.html', {'form': form})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()

            for file in request.FILES.getlist('attachments'):
                attachment = Attachment.objects.create(file=file, content_object=service_request)

            return redirect('track_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    for req in requests:
        req.created_at = timezone.localtime(req.created_at)
    return render(request, 'customer_service/track_requests.html', {'requests': requests})

@login_required
def account_info(request):
    user = request.user
    return render(request, 'customer_service/account_info.html', {'user': user})