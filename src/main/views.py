from django.shortcuts import render


def index(request):
    return render(request, 'main/home.html')


def about(request):
    # return render(request,'main/about.html')
    pass


def contact(request):
    pass
    # return render(request,'main/contact.html')


def page_not_found_view(request, exception):
    return render(request,
                  'main/errors/404.html',
                  status=404)
