from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
 def __init__(self, *args, **kwargs):
  super().__init__(*args, **kwargs)
 
  self.fields['username'].label = 'Display Name'
  self.fields['email'].label = 'Email Address'
  
form = SignUpForm(data=request.POST or None)

if form.is_valid():
 new_user = form.save(commit=False)
 new_user.save()

return render(request, 'register.html', {'form': form})