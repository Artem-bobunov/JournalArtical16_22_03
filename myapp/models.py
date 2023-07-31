from django.db import models


# Отрицательная площадь таблица ОКС
class OtrSquaria_oks(models.Model):
    kh_OtrSquaria_oks = models.CharField('KH (ОКС)', max_length=245, null=True, blank=True)
    id_oks_otr = models.IntegerField('id отрицательной S (ОКС)', null=True, blank=True)

# Другой регион таблица ОКС
class DrugoiReg_oks(models.Model):
    kh_DrugoiReg_oks = models.CharField('KH (ОКС)', max_length=245, null=True, blank=True)
    adress = models.CharField('Адрес (ОКС)', max_length=4000, null=True, blank=True)
    id_oks_DrugoiReg = models.IntegerField('id Другого региона (ОКС)', null=True, blank=True)

# Условные таблица ОКС
class Uslovnye_oks(models.Model):
    kh_Uslovnye_oks = models.CharField('KH (ОКС)', max_length=245, null=True, blank=True)
    id_uslovnye_oks = models.IntegerField('id условный (ОКС)', null=True, blank=True)

# Без КН Таблица ОКС
class BezKn_oks(models.Model):
    kh_BezKn_oks = models.CharField('KH (ОКС)', max_length=245, null=True, blank=True)
    id_bezKn_oks = models.IntegerField('id без КН (ОКС)', null=True, blank=True)

# ЕНК таблица ОКС
class Enk_oks(models.Model):
    kh_Enk_oks = models.CharField('KH (ОКС)', max_length=245, null=True, blank=True)
    id_enk_oks = models.IntegerField('id ЕНК (ОКС)', null=True, blank=True)

# Отрицательная площадь (ЗУ)
class OtrSquaria_zu(models.Model):
    kh_OtrSquaria_zu = models.CharField('KH (ОКС)', max_length=245, null=True, blank=True)
    id_otrS_zu = models.IntegerField('id Отрицательной S (ЗУ)', null=True, blank=True)

# Другой регион (ЗУ)
class DrugoiReg_zu(models.Model):
    kh_DrugoiReg_zu = models.CharField('KH (ЗУ)', max_length=245, null=True, blank=True)
    adress_DrugoiReg_zu = models.CharField('Адрес (ЗУ)', max_length=4000, null=True, blank=True)
    id_zu_DrugoiReg = models.IntegerField('id Другого региона (ЗУ)', null=True, blank=True)

USER_SELECT = [
    ('Александров Александр Александрович', 'Александров Александр Александрович'),
    ('Бобунов Артем Владимирович','Бобунов Артем Владимирович'),
    ('Деточенко Юлия Андреевна', 'Деточенко Юлия Андреевна'),
    ('Меликян Сюзанна Кареновна', 'Меликян Сюзанна Кареновна'),
    ('Бакулин Алексей Алексеевич','Бакулин Алексей Алексеевич'),
    ('Султанов Денис Шакирович', 'Султанов Денис Шакирович'),
    ('Леонтьева Ольга Петровна','Леонтьева Ольга Петровна'),
    ('Алиева Раиса Александровна','Алиева Раиса Александровна'),
    ('Липин Евгений Александрович','Липин Евгений Александрович'),
    ('Кряжева Юлия Александровна','Кряжева Юлия Александровна'),
    ('Губарь Анна Александровна','Губарь Анна Александровна'),
    ('Петрухина Ирина Павловна','Петрухина Ирина Павловна'),
    ('Пикина Ирина Борисовна','Пикина Ирина Борисовна'),
    ('Сологубова Анастасия Романовна','Сологубова Анастасия Романовна'),
    ('Филюкова Мария Михайловна','Филюкова Мария Михайловна'),
    ('Чепцова Александра Николаевна','Чепцова Александра Николаевна'),
    ('Сербина Татьяна Александровна','Сербина Татьяна Александровна'),
    ('Селеменчук Елена Владимировна', 'Селеменчук Елена Владимировна'),
    ('Акинтикова Екатерина Владимировна','Акинтикова Екатерина Владимировна'),
    ('Горбатикова Яна Евгеньевна','Горбатикова Яна Евгеньевна'),
    ('Катасонова Инга Юрьевна','Катасонова Инга Юрьевна'),
    ('Бородина Екатерина Вячеславовна','Бородина Екатерина Вячеславовна'),
    ('Волкова Арина Алексеевна','Волкова Арина Алексеевна'),
    ('Леонтьева Наталия Петровна','Леонтьева Наталия Петровна'),
    ('Мелкумян Валерия Евгеньевна','Мелкумян Валерия Евгеньевна'),
    ('Сологубов Михаил Алексеевич', 'Сологубов Михаил Алексеевич'),
]

DEPARTAMENT_SELECT = [
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),
]

class UserName(models.Model):
    name = models.CharField(max_length=100, choices=USER_SELECT, null=True, blank=True)
    departament = models.CharField('Отдел',max_length=10, choices=DEPARTAMENT_SELECT, null=True,  blank=True)

    def __str__(self):
        return self.name



class RegData(models.Model):
    # Регистрация данных
    dateIshod = models.DateField('Дата исходящая', null=True, blank=True)
    numberIshod = models.CharField('Номер исходящего документа', max_length=50, blank=True, null=True, default='№')
    deteVoznikosnov = models.DateField('Дата возникновения основания', null=True, blank=True)
    dateVhod = models.DateField('Дата входящего', null=True, blank=True)
    numberVhod = models.CharField('Номер входящего документа', max_length=50, blank=True, null=True, default='№')
    dateOtpravkiPoFz = models.DateField('Дата отправки по ФЗ', null=True, blank=True)
    oks = models.CharField('ОКС галочка', max_length=50, null=True, blank=True)
    zu = models.CharField('ЗУ галочка', max_length=50, null=True, blank=True)


    # ОКС
    nameAson_oks = models.CharField('Название перечня в АСОН (ОКС)', max_length=180, null=True, blank=True)
    zagruzhenoOH_oks = models.IntegerField('Загружено ОН (ОКС)', null=True, blank=True, default=0)
    poluchenoOH_oks = models.IntegerField('Получено ОН (ОКС)', null=True, blank=True, default=0)
    povtornyhOH_oks = models.IntegerField('Потворных ОН (ОКС)', null=True, blank=True, default=0)
    otrS_oks = models.IntegerField('Отрицательная площадь (ОКС)', null=True, blank=True, default=0)
    drugoiReg_oks = models.IntegerField('Другой регион (ОКС)', null=True, blank=True, default=0)
    uslovnye_oks = models.IntegerField('Условные (ОКС)', null=True, blank=True, default=0)
    bezKn_oks =  models.IntegerField('Без КН (ОКС)', null=True, blank=True, default=0)
    enk_oks =  models.IntegerField('ЕНК (ОКС)', null=True, blank=True, default=0)
        # Ключ к таблице
    fk_OtrSquaria_oks = models.ManyToManyField(OtrSquaria_oks,  null=True, blank=True)
    fk_DrugoiReg_oks = models.ManyToManyField(DrugoiReg_oks, null=True, blank=True)
    fk_Uslovnye_oks = models.ManyToManyField(Uslovnye_oks, null=True, blank=True)
    fk_Kn_oks = models.ManyToManyField(BezKn_oks, null=True, blank=True)
    fk_Enk_oks = models.ManyToManyField(Enk_oks, null=True, blank=True)

        # ЗУ
    nameAson_zu = models.CharField('Название перечня в АСОН (ЗУ)', max_length=180, null=True, blank=True)
    zagruzhenoOH_zu = models.IntegerField('Загружено ОН (ЗУ)', null=True, blank=True, default=0)
    poluchenoOH_zu = models.IntegerField('Получено ОН (ЗУ)', null=True, blank=True, default=0)
    povtornyhOH_zu = models.IntegerField('Потворных ОН (ЗУ)', null=True, blank=True, default=0)
    categoriy_zu = models.CharField('Категории ЗУ - галочка', max_length=50, null=True, blank=True)

    sx = models.IntegerField('СХ (ЗУ)', null=True, blank=True, default=0)
    np = models.IntegerField('НП (ЗУ)', null=True, blank=True, default=0)
    oot = models.IntegerField('ООТ (ЗУ)', null=True, blank=True, default=0)
    vf = models.IntegerField('ВФ (ЗУ)', null=True, blank=True, default=0)
    nameSx = models.CharField('Название СХ (ЗУ)', max_length=180, null=True, blank=True)
    nameNp = models.CharField('Название НП (ЗУ)', max_length=180, null=True, blank=True)
    nameOot =  models.CharField('Название ООТ (ЗУ)', max_length=180, null=True, blank=True)
    nameVf =  models.CharField('Название ВФ (ЗУ)', max_length=180, null=True, blank=True)
    numberSx = models.CharField('номер акта СХ (ЗУ)', max_length=180, null=True, blank=True)
    numberNp = models.CharField('номер акта НП (ЗУ)', max_length=180, null=True, blank=True)
    numberOot = models.CharField('номер акта ООТ (ЗУ)', max_length=180, null=True, blank=True)
    numberVf = models.CharField('номер акта ВФ (ЗУ)', max_length=180, null=True, blank=True)
    date_Sx = models.DateField('дата СХ',null=True, blank=True)
    date_Np = models.DateField('дата НП',null=True, blank=True)
    date_Oot = models.DateField('дата ООТ',null=True, blank=True)
    date_Vf = models.DateField('дата ВФ',null=True, blank=True)



    prom = models.IntegerField('Пром (ЗУ)', null=True, blank=True, default=0)
    lf = models.IntegerField('ЛФ (ЗУ)', null=True, blank=True, default=0)
    zz = models.IntegerField('ЗЗ (ЗУ)', null=True, blank=True, default=0)
    bezCat = models.IntegerField('Без кат (ЗУ)', null=True, blank=True, default=0)
    otrS_zu = models.IntegerField('Отрицательная S (ЗУ)', null=True, blank=True, default=0)
    drugoiReg_zu = models.IntegerField('Другой регион (ЗУ)', null=True, blank=True, default=0)
    uslovnye_zu = models.IntegerField('Условные (ЗУ)', null=True, blank=True, default=0)
    obosoblennye = models.IntegerField('Обособленные (ЗУ)', null=True, blank=True, default=0)
            # Ключ к таблице ЗУ
    fk_OtrSquaria_zu = models.ManyToManyField(OtrSquaria_zu,  null=True, blank=True)
    fk_DrugoiReg_zu = models.ManyToManyField(DrugoiReg_zu,  null=True, blank=True)

    #
    number_act_oks = models.CharField('№ акта ОКС', max_length=150,null=True, blank=True)
    number_act_zu = models.CharField('№ акта ЗУ', max_length=150,null=True, blank=True)

    date_act_oks = models.DateField('Дата акта ОКС',null=True, blank=True)
    date_act_zu = models.DateField('Дата акта ЗУ',null=True, blank=True)

    count_ocenka_obj_oks = models.IntegerField('Количествол оцененных объектов ОКС', null=True, blank=True, default=0)
    count_ocenka_obj_zu = models.IntegerField('Количествол оцененных объектов ЗУ', null=True, blank=True, default=0)

    count_not_ocenka_obj_oks = models.IntegerField('Количествол неоцененных объектов ОКС', null=True, blank=True, default=0)
    count_not_ocenka_obj_zu = models.IntegerField('Количествол неоцененных объектов ЗУ', null=True, blank=True, default=0)

    date_output_oks = models.DateField('дата фактической отправки ОКС',null=True, blank=True)
    date_output_zu = models.DateField('дата фактической отправки ЗУ',null=True, blank=True)

    number_mail_oks = models.CharField('Номер сопроводительного письма ОКС',null=True, blank=True, max_length=150)
    number_mail_zu = models.CharField('Номер сопроводительного письма ЗУ',null=True, blank=True, max_length=150)


