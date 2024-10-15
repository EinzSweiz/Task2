from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from django.contrib import messages

def create_image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('image_list')
    else:
        form = ImageForm()
    
    return render(request, 'images/upload_image.html', {'form': form})
