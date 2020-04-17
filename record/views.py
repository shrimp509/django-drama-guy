from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from .forms import DramaRecordForm


def add_record(request: WSGIRequest):
    form = DramaRecordForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # success
            return render(request, 'add_record.html', {'status': 'success'})
        else:
            # fail
            return render(request, 'add_record.html', {'status': 'fail'})
    elif request.method == 'GET':
        return render(request, 'add_record.html', {'form': form, 'status': ''})


def edit_record(reqeust: WSGIRequest):
    print("do nothing")