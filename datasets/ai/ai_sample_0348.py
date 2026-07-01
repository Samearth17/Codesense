from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def get_user_records(request):
    page_num = request.GET.get('page', 1)
    page_size = int(request.GET.get('page_size', 10))

    users = User.objects.all().order_by('user_id')
    paginator = Paginator(users, page_size)
    page_data = paginator.page(page_num)
    response_data = {
        'data': [
            {
                'user_id': user.user_id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'age': user.age,
                'email': user.email
            } for user in page_data
        ]
    }
    return JsonResponse(response_data)