from userprofile.models import Pontaj

def get_company_name(request):
    if request.user.is_authenticated:
        return {'customer_name': request.user.userextend.customer.name}
    else:
        return {}

def is_ready_to_word(request):
    if request.user.is_authenticated:
        if Pontaj.objects.filter(user_id=request.user.id,  end_date=None).exists() is True:
            return {'ready_to_work': False}
        return {'ready_to_work': True}
    return {}
