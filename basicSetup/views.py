# myapp/views.py
from django.shortcuts import render
import os

def home_view(request):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'hello.txt')
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
        else:
            content = "File not found."
    except Exception as e:
        content = f"An error occurred: {e}"

    return render(request, 'home.html', {'content': content})
