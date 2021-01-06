import datetime

from userprofile.models import Logs


class RefreshMiddlware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('refresh', datetime.datetime.now())
        print(request.method)
        print(request.path.isdigit())
        a = False
        list_ch = [True for item in str(request.path) if item.isdigit()]
        print(list_ch)
        if request.user.is_authenticated:
            if request.method == 'GET':
                Logs.objects.create(user_id=request.user.id, customer_id=request.user.userextend.customer.id, action='refresh', url=request.path)
            elif request.method == 'POST':
                if True in list_ch:
                    Logs.objects.create(user_id=request.user.id, customer_id=request.user.userextend.customer.id, action='updated', url=request.path)
                else:
                    Logs.objects.create(user_id=request.user.id, customer_id=request.user.userextend.customer.id, action='created', url=request.path)
        response = self.get_response(request)
        return response
