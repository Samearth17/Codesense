# projects/quotes/models.py

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote_text = models.TextField()


class UserQuote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

# projects/quotes/views.py

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    quotes = request.user.userquote_set.all()
    return render(request, 'quotes/index.html', {'quotes': quotes})

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            django_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'quotes/login.html', {'form': form})