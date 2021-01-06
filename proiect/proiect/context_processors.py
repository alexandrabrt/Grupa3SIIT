

def get_company_name(request):
    if request.user.is_authenticated:
        return {'customer_name': request.user.userextend.customer.name}
    else:
        return {}