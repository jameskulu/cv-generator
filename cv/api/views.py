from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from ..models import CV
from .serializer import CVSerializer


@api_view(
    [
        "GET",
    ]
)
@permission_classes([IsAdminUser])
def cv_view(request):
    name = request.query_params.get("name")
    paginator = PageNumberPagination()
    paginator.page_size = 10
    # cvs = CV.objects.filter(name=name)
    cvs = CV.objects.all()
    result_page = paginator.paginate_queryset(cvs, request)
    serializer = CVSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
