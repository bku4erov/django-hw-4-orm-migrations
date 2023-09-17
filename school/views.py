from django.shortcuts import render
from django.views.generic import ListView

from .models import Student


def students_list(request):
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    template = 'school/students_list.html'
    students = Student.objects.all().prefetch_related('teachers').order_by(ordering)
    context = {'object_list': students}

    return render(request, template, context)
