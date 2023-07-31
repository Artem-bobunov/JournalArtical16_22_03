import datetime
import numpy as np
import docxtpl as docxtpl
from django.http import request

from .models import *

def docx(obj):

    file_download = None
    date_now = None
    print('Метод выполнился')

    id_obj = np.array(obj.values_list('id', flat=True))

    """Отправлено актов (всего)"""
    actov = []

    for r in id_obj:
        r_obj = RegData.objects.get(pk=r)
        if r_obj.date_act_oks != None:
            actov.append(r_obj.date_act_oks)
    sum_actov = len(actov)

    """ОКС (всего)"""
    oks_1 = []

    for v in id_obj:
        v_obj = RegData.objects.get(pk=v)
        if v_obj.oks == 'ОКС':
            oks_1.append(v_obj.oks)
    sum_oks_1 = len(oks_1)

    """ЗУ (всего)"""
    zu_1 = []

    for h in id_obj:
        h_obj = RegData.objects.get(pk=h)
        if h_obj.zu == 'ЗУ':
            zu_1.append(h_obj.oks)
    sum_zu_1 = len(zu_1)

    """Полученных объектов (XML)  B & F"""
    poluch = []
    for p in id_obj:
        p_obj = RegData.objects.get(pk=p)
        poluch.append(p_obj.poluchenoOH_oks)
        poluch.append(p_obj.poluchenoOH_zu)
    poluch = [p_obj.poluchenoOH_zu, p_obj.poluchenoOH_zu]
    poluch = list(filter(None, poluch))  # filter out None values
    sum_poluch = sum(poluch)
    print(sum_poluch, 'Сумма полученых окс_зу')

    """Загружено объектов в АСОН (всего) A & D"""
    zagruzheno = []
    for d in id_obj:
        d_obj = RegData.objects.get(pk=d)
        zagruzheno.append(d_obj.zagruzhenoOH_zu)
        zagruzheno.append(d_obj.zagruzhenoOH_oks)
    zagruzheno = [d_obj.zagruzhenoOH_oks, d_obj.zagruzhenoOH_oks]
    zagruzheno = list(filter(None, zagruzheno))  # filter out None values
    sum_zagruzheno = sum(zagruzheno)

    """Объекты недвижимости, кадастровая стоимость которых определена  (Кол-во оцененных объектов_OKS + Кол-во оцененных объектов_ZU)"""
    count_ocenka = []
    for l in id_obj:
        l_obj = RegData.objects.get(pk=l)
        count_ocenka.append(l_obj.count_ocenka_obj_zu)
        count_ocenka.append(l_obj.count_ocenka_obj_oks)
    count_ocenka = [l_obj.count_ocenka_obj_zu, l_obj.count_ocenka_obj_oks]
    count_ocenka = list(filter(None, count_ocenka))  # filter out None values
    sum_count_ocenka = sum(count_ocenka)

    """ Объекты недвижимости, изменение сведений Единого государственного реестра недвижимости о которых не влечет за собой изменение их кадастровой стоимости НЕ(Кол-во оцененных объектов_OKS + Кол-во оцененных объектов_ZU)"""
    nocount_ocenka = []
    for y in id_obj:
        y_obj = RegData.objects.get(pk=y)
        nocount_ocenka.append(y_obj.count_not_ocenka_obj_zu)
        nocount_ocenka.append(y_obj.count_not_ocenka_obj_oks)
    nocount_ocenka = [l_obj.count_not_ocenka_obj_oks, l_obj.count_not_ocenka_obj_oks]
    nocount_ocenka = list(filter(None, nocount_ocenka))  # filter out None values
    sum_nocount_ocenka = sum(nocount_ocenka)

    datesearch = obj.values_list('date_output_oks', flat=True)
    print('sasasas', datesearch)
    date_res = []
    for i in datesearch:
        if i:
            date_res.append(i.strftime('%d.%m.%Y'))
    if date_res:
        date_first = str(date_res[0])
        print('sasasaas', date_first)
        date_last = str(date_res[-1])
        current_date_time = datetime.datetime.now()
        date_now = current_date_time.strftime('%d.%m.%Y %H:%M:%S')

        document = docxtpl.DocxTemplate(
            'C:\Projects\JournalArticle16_22_03\media\Отчет_шаблон.docx')
        context_doc = {'sum_poluch': sum_poluch, 'sum_zagruzheno': sum_zagruzheno, 'sum_count_ocenka': sum_count_ocenka, 'sum_nocount_ocenka': sum_nocount_ocenka,
                       'sum_actov': sum_actov, 'sum_oks_1': sum_oks_1, 'sum_zu_1': sum_zu_1, 'date_first':date_first,'date_last':date_last }
        document.render(context_doc)
        document.save('C:\Projects\JournalArticle16_22_03\media\Отчёт' + '.docx')
        file_download = 'Отчёт' + '.docx'
        # file_download = 'Отчет_шаблон222' + '.docx'

        return file_download