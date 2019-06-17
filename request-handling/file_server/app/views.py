import datetime
from django.conf import settings
from django.shortcuts import render
import os
from datetime import datetime




def file_list(request, date=0):
    template_name = 'index.html'
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    files = []
    for file in os.listdir(settings.FILES_PATH):
        info = os.stat('%s\%s' % (settings.FILES_PATH, file))
        ctime = datetime.fromtimestamp(info.st_ctime).strftime("%Y-%m-%d %H:%M")
        mtime = datetime.fromtimestamp(info.st_mtime).strftime("%Y-%m-%d %H:%M")
        datetime_object = datetime.fromtimestamp(info.st_ctime).strftime("%Y-%m-%d")
        files.append({
                'name': file,
                'ctime': ctime,
                'mtime': mtime,
                'date': datetime_object})
    print(files)
    if date == 0:
        context = {'files': files}
    else:
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        context = {'files': files,
                   'date': datetime.date(datetime_object)}
    return render(request, template_name, context)

def file_content(request, name):
    if name in os.listdir(settings.FILES_PATH):
        text_str = ''
        path = settings.FILES_PATH
        fi = open('%s\\%s' % (path, name), 'r')
        for line in fi:
            text_str += line
        return render(
            request,
            'file_content.html',
            context={'file_name': name, 'file_content': text_str}
    )

