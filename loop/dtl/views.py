from django.shortcuts import render

def new_view(request):
    # Context data (can include variables, lists, etc.)
    context = {
        'page_title': 'New View Page',
        'items': ['Apple', 'Banana', 'Cherry'],
        'show_message': True,
        'message': 'Welcome to the new view!'
    }
    return render(request, 'dtl/dtl.html', context)
