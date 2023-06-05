import datetime


def footer_context(request):
    return {
        'year': datetime.datetime.now().year,
        'mobile': '+7 (000) 699 86 56',
        'email': 'mail@mail546895.ru',

        'footer': 'Footer'
    }
