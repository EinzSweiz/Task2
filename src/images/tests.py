from django.test import TestCase
from s3.client import S3Client
from django.http import HttpResponse
import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def test_upload_view(request):
    if request.method == 'POST':
        image = request.FILES['image']
        logger.info(f'Testing upload: {image.name}, Size: {image.size}, Closed: {image.closed}')

        s3_client = S3Client()
        s3_client.client.upload_fileobj(image, s3_client.default_bucket_name, image.name)
        return HttpResponse('Uploaded successfully!')

    return render(request, 'images/upload_test.html')
