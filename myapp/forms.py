from django.forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class FormDateReg(ModelForm):
    class Meta:
        model = RegData
        fields = "__all__"
        widgets = {
                'dateIshod':TextInput(attrs={ 'class': 'form-control width__date','type': 'date','format':'%d.%m.%Y'}),
                'numberIshod':TextInput(attrs={'class': 'form-control width__text', 'placeholder':'Номер исх.'}),
                'deteVoznikosnov':TextInput(attrs={'class': 'form-control width__date','type': 'date','format':'%d.%m.%Y'}),
                'dateVhod':TextInput(attrs={'class': 'form-control width__date','type': 'date','format':'%d.%m.%Y'}),
                'numberVhod': TextInput(attrs={'class': 'form-control width__text', 'placeholder':'Номер вх.'}),
                'dateOtpravkiPoFz':TextInput(attrs={'class': 'form-control width__date','type': 'date','format':'%d.%m.%Y'}),
            # ОКС
                'nameAson_oks': TextInput(attrs={'class': 'form-control'}),
                'zagruzhenoOH_oks': NumberInput(attrs={'class': 'form-control','id':'zagr_on_oks'}),
                'poluchenoOH_oks': NumberInput(attrs={'class': 'form-control','id':'poluch_on_oks',}),
                'povtornyhOH_oks': NumberInput(attrs={'class': 'form-control','id':'povtor_on_oks'}),
                'otrS_oks': NumberInput(attrs={'class': 'form-control','id':'otr_s_oks1'}),
                'drugoiReg_oks': NumberInput(attrs={'class': 'form-control ','id':'drugoiReg_oks2'}),
                'uslovnye_oks': NumberInput(attrs={'class': 'form-control','id':'uslovnye_oks3'}),
                'bezKn_oks': NumberInput(attrs={'class': 'form-control','id':'bezKn_oks4'}),
                'enk_oks': NumberInput(attrs={'class': 'form-control','id':'enk_oks5'}),
                'number_act_oks': TextInput(attrs={'class': 'form-control'}),
                'date_act_oks': TextInput(attrs={'class': 'form-control ','type': 'date','format':'%d.%m.%Y'}),
                'count_ocenka_obj_oks': NumberInput(attrs={'class': 'form-control'}),
                'count_not_ocenka_obj_oks': NumberInput(attrs={'class': 'form-control'}),
                'date_output_oks': TextInput(attrs={'class': 'form-control ','type': 'date','format':'%d.%m.%Y'}),
                'number_mail_oks': TextInput(attrs={'class': 'form-control '}),

            # ЗУ
                'nameAson_zu': TextInput(attrs={'class': 'form-control'}),
                'zagruzhenoOH_zu': NumberInput(attrs={'class': 'form-control', 'id': 'zagr_on_zu'}),
                'poluchenoOH_zu': NumberInput(attrs={'class': 'form-control', 'id': 'poluch_on_zu'}),
                'povtornyhOH_zu': NumberInput(attrs={'class': 'form-control', 'id': 'povtor_on_zu'}),



                'sx': NumberInput(attrs={'class': 'form-control', 'id': 'sx_zu'}),
                'np': NumberInput(attrs={'class': 'form-control', 'id': 'np_zu'}),
                'oot': NumberInput(attrs={'class': 'form-control', 'id': 'oot_zu'}),
                'vf': NumberInput(attrs={'class': 'form-control', 'id': 'wf_zu'}),
                'nameSx': TextInput(attrs={'class': 'form-control'}),
                'nameNp': TextInput(attrs={'class': 'form-control'}),
                'nameOot': TextInput(attrs={'class': 'form-control'}),
                'nameVf': TextInput(attrs={'class': 'form-control'}),
                'numberSx': TextInput(attrs={'class': 'form-control'}),
                'numberNp': TextInput(attrs={'class': 'form-control'}),
                'numberOot': TextInput(attrs={'class': 'form-control'}),
                'numberVf': TextInput(attrs={'class': 'form-control'}),
                'date_Sx': TextInput(attrs={'class': 'form-control', 'type': 'date', 'format': '%d.%m.%Y'}),
                'date_Np': TextInput(attrs={'class': 'form-control', 'type': 'date', 'format': '%d.%m.%Y'}),
                'date_Oot': TextInput(attrs={'class': 'form-control', 'type': 'date', 'format': '%d.%m.%Y'}),
                'date_Vf': TextInput(attrs={'class': 'form-control', 'type': 'date', 'format': '%d.%m.%Y'}),

                'prom': NumberInput(attrs={'class': 'form-control', 'id': 'prom_zu'}),
                'lf': NumberInput(attrs={'class': 'form-control', 'id': 'lf_zu'}),
                'zz': NumberInput(attrs={'class': 'form-control', 'id': 'zz_zu'}),
                'bezCat': NumberInput(attrs={'class': 'form-control', 'id': 'bezcat_zu'}),
                'otrS_zu': NumberInput(attrs={'class': 'form-control','id':'otr_s_zy'}),
                'drugoiReg_zu': NumberInput(attrs={'class': 'form-control','id':'drygoi_reg_zy'}),
                'uslovnye_zu': NumberInput(attrs={'class': 'form-control', 'id': 'usl_zu'}),
                'obosoblennye': NumberInput(attrs={'class': 'form-control', 'id': 'obosoblennye_zu'}),
                'number_act_zu': TextInput(attrs={'class': 'form-control'}),
                'date_act_zu': TextInput(attrs={'class': 'form-control', 'type': 'date', 'format': '%d.%m.%Y'}),
                'count_ocenka_obj_zu': NumberInput(attrs={'class': 'form-control'}),
                'count_not_ocenka_obj_zu': NumberInput(attrs={'class': 'form-control'}),
                'date_output_zu': TextInput(attrs={'class': 'form-control ', 'type': 'date', 'format': '%d.%m.%Y'}),
                'number_mail_zu': TextInput(attrs={'class': 'form-control '}),

        }


    # npp, number + 1
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     last_document = RegData.objects.order_by('-id').first()
    #     if last_document:
    #         last_number_act_oks = last_document.number_act_oks.split('АОКС-34/2023/')[-1].strip()
    #         self.fields['number_act_oks'].initial = str(int(last_number_act_oks) + 1)
    #     else:
    #         self.fields['number_act_oks'].initial = '1'
    #

# Отрицательная площадь таблица ОКС
class FormOtrSquaria_oks(ModelForm):
    class Meta:
        model = OtrSquaria_oks
        fields = "__all__"
        widgets = {
            'kh_OtrSquaria_oks':TextInput(attrs={'class': 'form-control width__text'}),
        }


# Другой регион таблица ОКС
class FormDrugoiReg_oks(ModelForm):
    class Meta:
        model = DrugoiReg_oks
        fields = "__all__"
        widgets = {
            'kh_DrugoiReg_oks': TextInput(attrs={'class': 'form-control width__text','id':'id_kh'}),
            'adress': TextInput(attrs={'class': 'form-control width__text','id':'id_adress'}),
        }

# Условные таблица ОКС
class FormUslovnye_oks(ModelForm):
    class Meta:
        model = Uslovnye_oks
        fields = "__all__"
        widgets = {
            'kh_Uslovnye_oks': TextInput(attrs={'class': 'form-control width_Uslov_BezNK_ENK'}),
        }

# Без КН Таблица ОКС
class FormBezKn_oks(ModelForm):
    class Meta:
        model = BezKn_oks
        fields = "__all__"
        widgets = {
            'kh_BezKn_oks': TextInput(attrs={'class': 'form-control width_Uslov_BezNK_ENK'}),
        }

# ЕНК таблица ОКС
class FormEnk_oks(ModelForm):
    class Meta:
        model = Enk_oks
        fields = "__all__"
        widgets = {
            'kh_Enk_oks': TextInput(attrs={'class': 'form-control width_Uslov_BezNK_ENK'}),
        }

# Отрицательная площадь (ЗУ)
class FormOtrSquaria_zu(ModelForm):
    class Meta:
        model = OtrSquaria_zu
        fields = "__all__"
        widgets = {
            'kh_OtrSquaria_zu': TextInput(attrs={'class': 'form-control width__text'}),
        }

# Другой регион (ЗУ)
class FormDrugoiReg_zu(ModelForm):
    class Meta:
        model = DrugoiReg_zu
        fields = "__all__"
        widgets = {
            'kh_DrugoiReg_zu': TextInput(attrs={'class': 'form-control width__text'}),
            'adress_DrugoiReg_zu': TextInput(attrs={'class': 'form-control width__text'}),
        }

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'username': TextInput(attrs={}),
            'password': PasswordInput(attrs={})
        }