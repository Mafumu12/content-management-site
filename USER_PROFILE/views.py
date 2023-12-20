from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm
from django.http import HttpResponseForbidden
import logging
from django.contrib.auth.decorators import login_required
from django.contrib import messages

logger = logging.getLogger(__name__)
# Create your views here.

# Create your views here.



def UserProfile(request, profile_id):
    

     profile = Profile.objects.get(pk = profile_id)
     context = {'profile':profile}
     return render(request,'profile.html',context)

def account(request):
   account = request.user.profile
   context = {'account':account}
    
   return render(request,'account.html',context)


@login_required
def UpdateProfile(request,profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id)
        
        # Check if the logged-in user has permission to edit this profile
        if request.user.profile == profile:
            if request.method == 'POST':
                form = ProfileForm(request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    form.save()
                    # Redirect to the profile page after successful update
                    return redirect('profile',profile_id=profile_id)
            else:
                form = ProfileForm(instance=profile)

            context = {'form': form}
            return render(request, 'update-profile.html', context)
        else:
            return HttpResponseForbidden("You don't have permission to update this profile.")
    except Profile.DoesNotExist:
        # Handle the case where the profile doesn't exist.
        logger.error(f"Profile with ID {profile_id} does not exist.")
        # You can return an appropriate response here.

@login_required
def CreateProfile(request):
         
    
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                 
                profile.name = request.user
                profile.save()
                return redirect('home')
            else:
                messages.error(request,"Form is not valid.")

        else:
            form = ProfileForm()
            context = {'form':form}
            return render(request,'createprofile.html',context)
     

def DeleteProfile(request,profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id)
        
        # Check if the logged-in user has permission to delete this profile
        if request.user.profile == profile:
            profile.delete()
            request.user.delete()
            return redirect('signup')
        else:
            return HttpResponseForbidden("You don't have permission to delete this profile.")
    except Profile.DoesNotExist:
        logger.error(f"Profile with ID {profile_id} does not exist.")