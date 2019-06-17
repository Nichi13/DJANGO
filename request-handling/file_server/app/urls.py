from django.urls import path
from app.views import file_list, file_content
# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
# вот тут у меня вышла загвоздка. p.s. взял только один файл из списка, чтоб легче было продумать логику


urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    path('<date>', file_list, name='file_list'),
    path('<name>/', file_content, name='file_content'),
    # path(..., name='file_list'),
    # path(..., name='file_content'),
]
