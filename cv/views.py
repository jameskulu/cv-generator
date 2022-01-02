import io
import os
import platform
import subprocess
import sys
from io import BytesIO

import pdfkit
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.template.loader import get_template
from xhtml2pdf import pisa

from .forms import CVCreateForm
from .models import CV


def home(request):
    return render(request, "cv/index.html")


@login_required
def list_of_cv(request):
    cvs = CV.objects.filter(user=request.user.id)
    return render(request, "cv/list.html", {"cvs": cvs})


# if platform.system() == "Windows":
#     pdfkit_config = pdfkit.configuration(
#         wkhtmltopdf=os.environ.get("WKHTMLTOPDF_BINARY", "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
#     )
# else:
#     os.environ["PATH"] += os.pathsep + os.path.dirname(sys.executable)
#     WKHTMLTOPDF_CMD = (
#         subprocess.Popen(["which", os.environ.get("WKHTMLTOPDF_BINARY", "wkhtmltopdf")], stdout=subprocess.PIPE)
#         .communicate()[0]
#         .strip()
#     )
#     pdfkit_config = pdfkit.configuration(c=WKHTMLTOPDF_CMD)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None


# @login_required
# def generate_cv(request, id):
#     cv = CV.objects.get(id=id)
#     template = loader.get_template("cv/cv.html")
#     html = template.render({"cv": cv})
#     options = {"page-size": "Letter", "encoding": "UTF-8"}
#     # config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
#     pdf = pdfkit.from_string(html, False, options)
#     response = HttpResponse(pdf, content_type="application/pdf")
#     response["Content-Disposition"] = "attachments"
#     return response


@login_required
def generate_cv(request, id):
    cv = CV.objects.get(id=id)
    pdf = render_to_pdf("cv/cv.html", {"cv": cv})
    response = HttpResponse(pdf, content_type="application/pdf")
    # filename = "Invoice_%s.pdf" % ("12341231")
    # content = "attachment; filename='%s'" % (filename)
    response["Content-Disposition"] = "attachments"
    return response


@login_required
def delete_cv(request, id):
    cv = CV.objects.get(id=id)
    if request.user.id == cv.user.id:
        cv.delete()
        messages.success(request, "CV deleted successfully")
    else:
        messages.error(request, "You do not have permission to delete this CV")
    return redirect("list-of-cv")


@login_required
def create(request):
    form = CVCreateForm()
    if request.method == "POST":
        form = CVCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()
            messages.success(request, "CV saved successfully")
            return redirect("list-of-cv")
        messages.error(request, form.errors)
    return render(request, "cv/create.html", {"form": form})


@login_required
def edit_cv(request, id):
    cv = CV.objects.get(pk=id)
    if cv.user == request.user:
        if request.method == "POST":
            form = CVCreateForm(request.POST, instance=cv)
            if form.is_valid():
                cv = form.save(commit=False)
                cv.user = request.user
                cv.save()
                messages.success(request, "CV updated successfully")
                return redirect("list-of-cv")
        else:
            form = CVCreateForm(instance=cv)
    else:
        messages.success(request, "You are not authorized to view this page.")
        return redirect("list-of-cv")
    context = {"form": form}
    return render(request, "cv/edit.html", context)
