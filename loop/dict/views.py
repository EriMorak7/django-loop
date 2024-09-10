from django.shortcuts import render

def my_view(request):
    # Create a dictionary to be passed to the template
    my_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'Wonderland'
    }
    
    # Pass the dictionary to the template via context
    context = {
        'my_dict': my_dict
    }
    
    # Render the template with the context
    return render(request, 'dict/my_template.html', context)
