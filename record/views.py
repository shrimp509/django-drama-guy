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
        return render(request, 'add_record.html', {'form': form, 'status': 'add'})


def get_all_records(request: WSGIRequest):
    dramas = DramaRecord.objects.all()
    return render(request, 'all_records.html', {
        'dramas': dramas
    })


def edit_record(request: WSGIRequest, id: int):
    # find object with id
    exists = DramaRecord.objects.filter(id=id)

    if request.method == 'GET':
        for exist in exists:
            form = DramaRecordForm(initial={
                'name': exist.name,
                'source': exist.source,
                'episode': exist.episode,
                'max_episode': exist.max_episode,
                'timestamp': exist.timestamp})

            # return result
            return render(request, 'add_record.html', {'form': form})
    elif request.method == 'POST':
        form = DramaRecordForm(request.POST or None)
        if form.is_valid():
            for exist in exists:
                exist.name = form.cleaned_data['name']
                exist.episode = form.cleaned_data['episode']
                exist.max_episode = form.cleaned_data['max_episode']
                exist.timestamp = form.cleaned_data['timestamp']
                exist = resolve_source(exist, form)
                exist.save()
                return redirect('/')
            return redirect('/edit/{}/'.format(id))
        else:
            return redirect('/edit/{}/'.format(id))

    return redirect('/record/')


def delete_record(request: WSGIRequest, id: int):
    if request.method == "POST":
        exists = DramaRecord.objects.filter(id=id)
        for exist in exists:
            exist.delete()
            print("id={} is deleted".format(id))

        return redirect('/')
    return redirect('/')


def resolve_source(record: DramaRecord, form: DramaRecordForm):
    source = form.cleaned_data['source']
    record.source = source
    return record
