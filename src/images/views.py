from uuid import uuid4
from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from s3.client import S3Client
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def create_image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()  # Save the form and create the image instance
            image_file = form.cleaned_data['image'] 
            
            try:
                # Logging for debug purposes
                logger.info(f'Image instance: {image_instance}, ID: {image_instance.id}')
                unique_file_name = f'{image_instance.get_prefix}{uuid4()}_{image_file.name}'

                if image_file.file.closed:
                    image_file.open() 
                
                # Upload to S3
                s3_client = S3Client()
                s3_client.client.upload_fileobj(
                    image_file.file,
                    s3_client.default_bucket_name,
                    unique_file_name
                )
                image = f'https://{s3_client.default_bucket_name}.s3.amazonaws.com/{unique_file_name}'
                

                image_instance.image = image

                image_instance.save()
                
                # Success message
                messages.success(request, 'Image uploaded successfully!')
                return redirect('images:image_list')
            except Exception as e:
                logger.error(f'Error uploading image: {e}')
                messages.error(request, f'Error uploading image: {e}')
    else:
        form = ImageForm()

    return render(request, 'images/upload_image.html', {'form': form})


def image_list_view(request):
    images = Image.objects.all() 
    return render(request, 'images/image_list.html', {'images': images})


def image_download_view(request):
    images = Image.objects.all()
    return render(request, 'images/download.html', {'images': images})