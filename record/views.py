from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest

from .forms import DramaRecordForm
from .models import DramaRecord


def add_record(request: WSGIRequest):
    form = DramaRecordForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # success
            return redirect('/')
        else:
            # fail
            return render(request, 'add_record.html', {'form': form, 'status': 'fail'})
    elif request.method == 'GET':
        return render(request, 'add_record.html', {'form': form, 'status': ''})


def get_all_records(request: WSGIRequest):
    dramas = DramaRecord.objects.all()
    return render(request, 'all_records.html', {
        'dramas': dramas
    })


def edit_record(reqeust: WSGIRequest):
    print("do nothing")


def delete_record(request: WSGIRequest, id: int):
    if request.method == "POST":
        exists = DramaRecord.objects.filter(id=id)
        for exist in exists:
            exist.delete()
            print("id={} is deleted".format(id))

        return redirect('/')
    return redirect('/')
