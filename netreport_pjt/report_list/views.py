from django.shortcuts import render

# Create your views here.

def index(request):
    # context = {
    #     'name': name
    # }

    return render(request, 'report_list/index.html')

def throw(request):
    return render(request, 'report_list/throw.html')

def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET)
    message = request.GET.get('message')
    context = {
        'message': message
    }

    return render(request, 'report_list/catch.html', context)
