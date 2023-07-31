from django.db.models import Q
from .models import *
import django_filters
from django import forms
from django.forms import *
from django_filters import DateFromToRangeFilter, OrderingFilter
from django_filters.widgets import RangeWidget, LinkWidget




class MRFilter(django_filters.FilterSet):
    objectType_oks = (
        ('ОКС', 'ОКС'),
    )
    objectType_zu = (
        ('ЗУ', 'ЗУ'),
    )


    CHOICES = (
        ('', objectType_oks),
        ('', objectType_zu),
    )


    dropdown = django_filters.ChoiceFilter( empty_label='Вид обьекта' ,choices=CHOICES, widget=Select(attrs={'class': 'btn btn-outline-secondary dropdown-toggle'}), method='filter_dropdown')

    def filter_dropdown(self, queryset, name, value):
        if value == '':
            return queryset
        if value == 'ОКС':
            return queryset.filter(oks='ОКС')
        if value == 'ЗУ':
            return queryset.filter(zu='ЗУ')


    dateOtpravkiPoFz = DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control','type':'date','format':'%d.%m.%Y'}))
    dateIshod = DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control','type':'date','format':'%d.%m.%Y'}))
    dateVhod = DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control','type':'date','format':'%d.%m.%Y'}))
    deteVoznikosnov = DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control','type':'date','format':'%d.%m.%Y'}))
    date_output_oks = DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control','type':'date','format':'%d.%m.%Y'}))

    ORDER_CHOICES = (
        ('number_act_oks', 'Номер акта ОКС (возр.)'),
        ('-number_act_oks', 'Номер акта ОКС (убыв.)'),
        ('number_act_zu', 'Номер акта ЗУ (возр.)'),
        ('-number_act_zu', 'Номер акта ЗУ (убыв.)'),
    )

    order_by = django_filters.OrderingFilter(choices=ORDER_CHOICES,widget=Select,
                                             empty_label='№ акта',
        fields=(
            ('number_act_oks', 'number_act_oks'),
            ('number_act_zu', 'number_act_zu'),

        ),
        field_labels={
            'number_act_oks': 'Номер акта ОКС',
            'number_act_zu': 'Номер акта ЗУ',
        })
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["order_by"].field.widget.attrs = {
            "class": "btn btn-outline-secondary dropdown-toggle"
        }


    class Meta:
        model = RegData
        fields = ['zu', 'oks', 'dateOtpravkiPoFz', 'dateIshod', 'dateVhod', 'deteVoznikosnov', 'date_output_oks', 'number_act_oks', 'number_act_zu']
        widgets = {
            'oks': TextInput(attrs={'class': 'oks-field'}),
            'zu': TextInput(attrs={'class': 'zu-field'}),
        }


        # oks = django_filters.ChoiceFilter(widget = Select(attrs={'class': 'form-control'}),choices = objectType_oks ,method='filter_oks')
        # zu = django_filters.ChoiceFilter(widget = Select(attrs={'class': 'form-control'}),choices = objectType_zu ,method='filter_zu')
        # zu_oks = django_filters.ChoiceFilter(widget = Select(attrs={'class': 'form-control'}), choices=objectType_oks_zu, method='filter_oks_zu')

        # def filter_oks(self, queryset, name, value):
        #     if value == 'ОКС':
        #         return queryset.filter(oks='ОКС', zu=None)
        #     return queryset
        #
        # def filter_zu(self, queryset, name, value):
        #     if value == 'ЗУ':
        #         return queryset.filter(zu='ЗУ', oks=None)
        #     return queryset
        #
        # def filter_oks_zu(self, queryset, name, value):
        #     if value == 'ОКС+ЗУ':
        #         return queryset.filter(zu='ЗУ', oks='ОКС')
        #     return queryset

















        # oks = django_filters.CharFilter(field_name='oks', lookup_expr='exact')
    # zu = django_filters.CharFilter(field_name='zu', lookup_expr='exact')
    #
    # class Meta:
    #     model = RegData
    #     fields = ['oks', 'zu']
    #
    # def filter_queryset(self, queryset):
    #     queryset = super().filter_queryset(queryset)
    #
    #     if self.cleaned_data['oks'] == 'ОКС' and not self.cleaned_data['zu']:
    #         queryset = queryset.filter(zu__isnull=True)
    #     elif self.cleaned_data['zu'] == 'ЗУ' and not self.cleaned_data['oks']:
    #         queryset = queryset.filter(oks__isnull=True)
    #     elif self.cleaned_data['oks'] == 'ОКС' and self.cleaned_data['zu'] == 'ЗУ':
    #         queryset = queryset.filter(oks='ОКС', zu='ЗУ')
    #
    #     return queryset





    # def filter_queryset(self, queryset):
    #     queryset = super().filter_queryset(queryset)
    #
    #     # if self.is_valid() and self.cleaned_data['oks'] == 'ОКС' and not self.cleaned_data['zu']:
    #     #     queryset = queryset.filter(zu__isnull=True)
    #     # elif self.is_valid() and self.cleaned_data['zu'] == 'ЗУ' and not self.cleaned_data['oks']:
    #     #     queryset = queryset.filter(oks__isnull=True)
    #     # elif self.is_valid() and self.cleaned_data['oks'] == 'ОКС' and self.cleaned_data['zu'] == 'ЗУ':
    #     #     queryset = queryset.filter(oks='ОКС', zu='ЗУ')
    #     #
    #     # return queryset
    #     #



