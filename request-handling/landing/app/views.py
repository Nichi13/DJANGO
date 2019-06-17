from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся

counter_show = Counter()
counter_click = Counter()


def index(request):
    test_arg = request.GET.get('from-landing')
    if test_arg == 'original':
        counter_click['original'] += 1
        print(counter_click)
    elif test_arg == 'test':
        counter_click['test'] += 1
        print(counter_click)
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    return render_to_response('index.html')


def landing(request):
    counter_show['original'] += 1
    print(counter_show)
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    return render_to_response('landing.html')


def landing_alternate(request):
    counter_show['test'] += 1
    print(counter_show)
    return render_to_response('landing_alternate.html')


def stats(request):
    test_click = int(counter_click['test'])
    test_show = int(counter_show['test'])
    if test_show != 0:
        res_coun = test_click / test_show
        res_t = round(res_coun, 3)
    else:
        res_t = 'на сайт не заходили ни разу'
    original_click = int(counter_click['original'])
    original_show = int(counter_show['original'])
    if original_show != 0:
        res_coun2 = original_click / original_show
        res_o = round(res_coun2, 3)
    else:
        res_o = 'на сайт не заходили ни разу'
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'test_conversion': res_t,
        'original_conversion': res_o,
    })
