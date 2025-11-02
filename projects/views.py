from django.views.generic import TemplateView

from tasks.models import Task

class IndexTemplateView(TemplateView):
    template_name = "projects/index.html"
