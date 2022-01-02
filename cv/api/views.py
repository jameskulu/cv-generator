from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser

from ..models import CV
from .serializer import CVSerializer


@api_view(
    [
        "GET",
    ]
)
@permission_classes([IsAdminUser])
def cv_view(request):
    skills = request.query_params.get("skills")
    paginator = PageNumberPagination()
    paginator.page_size = 10
    if skills is None:
        cvs = CV.objects.all()
    else:
        cvs = CV.objects.filter(skills__contains=skills)
    result_page = paginator.paginate_queryset(cvs, request)
    serializer = CVSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
