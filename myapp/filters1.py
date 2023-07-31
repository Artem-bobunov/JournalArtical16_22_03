from datetime import date, datetime, timedelta
from urllib import request

from django.db.models import Q
from .models import *

def filter_list(obj, request_params):
    # Поиск
    query = request_params.get('q')
    if query:
        obj = obj.filter(
            Q(numberIshod__icontains=query) |
            Q(numberVhod__icontains=query) |
            Q(nameAson_oks__icontains=query) |
            Q(nameAson_zu__icontains=query) |
            Q(number_act_oks__icontains=query) |
            Q(number_act_zu__icontains=query) |
            Q(number_mail_oks__icontains=query) |
            Q(oks__icontains=query) |
            Q(number_mail_zu__icontains=query)
        )

                                 # Фильтрация по дате
        # Дата исходящая
    if 'calendar' in request_params:
        today = date.today()
        if request_params['calendar'] == 'today':
            obj = obj.filter(dateIshod=today)
        elif request_params['calendar'] == 'yesterday':
            yesterday = today - timedelta(days=1)
            obj = obj.filter(dateIshod=yesterday)
        elif request_params['calendar'] == 'week':
            last_week = today - timedelta(weeks=1)
            obj = obj.filter(dateIshod__gte=last_week, dateIshod__lte=today)
        elif request_params['calendar'] == 'month':
            last_month = today.replace(day=1) - timedelta(days=1)
            obj = obj.filter(dateIshod__gte=last_month, dateIshod__lte=today)
        elif request_params['calendar'] == 'year':
            last_year = today.replace(day=1, month=1) - timedelta(days=1)
            obj = obj.filter(dateIshod__gte=last_year, dateIshod__lte=today)
    if 'start_date' in request_params and 'end_date' in request_params:
        start_date = datetime.strptime(request_params['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request_params['end_date'], '%Y-%m-%d').date()
        obj = obj.filter(dateIshod__range=[start_date, end_date])

        # Дата входящего
    if 'calendar' in request_params:
        today = date.today()
        if request_params['calendar'] == 'today_vhod':
            obj = obj.filter(dateVhod=today)
        elif request_params['calendar'] == 'yesterday_vhod':
            yesterday = today - timedelta(days=1)
            obj = obj.filter(dateVhod=yesterday)
        elif request_params['calendar'] == 'week_vhod':
            last_week = today - timedelta(weeks=1)
            obj = obj.filter(dateVhod__gte=last_week, dateVhod__lte=today)
        elif request_params['calendar'] == 'month_vhod':
            last_month = today.replace(day=1) - timedelta(days=1)
            obj = obj.filter(dateVhod__gte=last_month, dateVhod__lte=today)
        elif request_params['calendar'] == 'year_vhod':
            last_year = today.replace(day=1, month=1) - timedelta(days=1)
            obj = obj.filter(dateVhod__gte=last_year, dateVhod__lte=today)
    if 'start_date_vhod' in request_params and 'end_date_vhod' in request_params:
        start_date = datetime.strptime(request_params['start_date_vhod'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request_params['end_date_vhod'], '%Y-%m-%d').date()
        obj = obj.filter(dateVhod__range=[start_date, end_date])

        # Дата фактической отправки окс
    if 'calendar' in request_params:
        today = date.today()
        if request_params['calendar'] == 'today_output':
            obj = obj.filter(date_output_oks=today)
        elif request_params['calendar'] == 'yesterday_output':
            yesterday = today - timedelta(days=1)
            obj = obj.filter(date_output_oks=yesterday)
        elif request_params['calendar'] == 'week_output':
            last_week = today - timedelta(weeks=1)
            obj = obj.filter(date_output_oks__gte=last_week, date_output_oks__lte=today)
        elif request_params['calendar'] == 'month_output':
            last_month = today.replace(day=1) - timedelta(days=1)
            obj = obj.filter(date_output_oks__gte=last_month, date_output_oks__lte=today)
        elif request_params['calendar'] == 'year_output':
            last_year = today.replace(day=1, month=1) - timedelta(days=1)
            obj = obj.filter(date_output_oks__gte=last_year, date_output_oks__lte=today)
    if 'start_date_output' in request_params and 'end_date_output' in request_params:
        start_date = datetime.strptime(request_params['start_date_output'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request_params['end_date_output'], '%Y-%m-%d').date()
        obj = obj.filter(dateVhod__range=[start_date, end_date])

    # Дата фактической отправки ЗУ
    if 'calendar' in request_params:
        today = date.today()
        if request_params['calendar'] == 'today_output_zu':
            obj = obj.filter(date_output_oks=today)
        elif request_params['calendar'] == 'yesterday_output_zu':
            yesterday = today - timedelta(days=1)
            obj = obj.filter(date_output_oks=yesterday)
        elif request_params['calendar'] == 'week_output_zu':
            last_week = today - timedelta(weeks=1)
            obj = obj.filter(date_output_oks__gte=last_week, date_output_oks__lte=today)
        elif request_params['calendar'] == 'month_output_zu':
            last_month = today.replace(day=1) - timedelta(days=1)
            obj = obj.filter(date_output_oks__gte=last_month, date_output_oks__lte=today)
        elif request_params['calendar'] == 'year_output_zu':
            last_year = today.replace(day=1, month=1) - timedelta(days=1)
            obj = obj.filter(date_output_oks__gte=last_year, date_output_oks__lte=today)
    if 'start_date_output_zu' in request_params and 'end_date_output_zu' in request_params:
        start_date = datetime.strptime(request_params['start_date_output_zu'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request_params['end_date_output_zu'], '%Y-%m-%d').date()
        obj = obj.filter(dateVhod__range=[start_date, end_date])



    # Фильтрация по полю zu
    oks = request_params.get('oks')
    zu = request_params.get('zu')


    if oks == 'ОКС' and zu == None:
        obj = obj.filter(oks='ОКС', zu=None)

    if zu == 'ЗУ' and oks == None:
        obj = obj.filter(zu='ЗУ', oks=None)

    if oks == 'ОКС' and zu == 'ЗУ':
        obj = obj.filter(oks='ОКС', zu='ЗУ')
    # elif oks == 'ОКС':
    #     obj = obj.filter(oks='ОКС')
    # elif zu == 'ЗУ':
    #     obj = obj.filter(zu='ЗУ')
    return obj

