## Model
class Post(Model):
    author = CharField()
    title = CharField()
    content = TextField()
    num_comments = IntegerField()
    published_date = DateTimeField()

## View
def post_detail_view(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post_detail.html", {'post': post})

## Controller
def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {'posts': posts})