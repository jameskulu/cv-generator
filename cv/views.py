import io
import os
import platform
import subprocess
import sys

import pdfkit
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import CV


def home(request):
    return render(request, "cv/index.html")


@login_required
def list_of_cv(request):
    print(request.user.id)
    cvs = CV.objects.filter(user=request.user.id)
    return render(request, "cv/list.html", {"cvs": cvs})


if platform.system() == "Windows":
    pdfkit_config = pdfkit.configuration(
        wkhtmltopdf=os.environ.get("WKHTMLTOPDF_BINARY", "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    )
else:
    os.environ["PATH"] += os.pathsep + os.path.dirname(sys.executable)
    WKHTMLTOPDF_CMD = (
        subprocess.Popen(["which", os.environ.get("WKHTMLTOPDF_BINARY", "wkhtmltopdf")], stdout=subprocess.PIPE)
        .communicate()[0]
        .strip()
    )
    pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)


@login_required
def generate_cv(request, id):
    cv = CV.objects.get(id=id)
    template = loader.get_template("cv/cv.html")
    html = template.render({"cv": cv})

    options = {"page-size": "Letter", "encoding": "UTF-8"}
    # config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdf = pdfkit.from_string(html, False, options, configuration=pdfkit_config)
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = "attachments"
    return response
