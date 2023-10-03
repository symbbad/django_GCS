from django.shortcuts import render
from django.views.generic import TemplateView
from utils.upload import upload_image
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

def main(request):
    return render(request, "main.html")

def testcase_1(request):
    return render(request, "testcase_1.html")

def write(request):
    return render(request, "write.html")

@api_view(["POST"])
def upload_test(request, path):
    image = request.FILES["image"]
    public_url = upload_image(image, path)
    return Response({"url": public_url})