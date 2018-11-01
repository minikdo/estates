from django.db import models
# from django.urls import reverse


class OfertyNazwa(models.Model):
    nazwa = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)
    nazwa_poz = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'oferty_nazwa'


class OfertyMiasto(models.Model):
    nazwa = models.CharField(max_length=25)
    opis = models.CharField(max_length=25, blank=True)
    prior = models.IntegerField()
    grupa = models.IntegerField()
    msc = models.CharField(max_length=25)
    nazwa_otodom = models.CharField(max_length=25)
    powiat = models.CharField(max_length=25)
    nazwa_flat = models.CharField(max_length=25)
    # biuro = models.IntegerField(default=0)
    # biuro = models.ForeignKey('OfertyBiuro', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_miasto'

    def __str__(self):
        return self.nazwa


# class OfertyBiuro(models.Model):
    # tel1 = models.CharField(max_length=25, null=True)
    # tel2 = models.CharField(max_length=25, null=True)
    # email = models.CharField(max_length=25, null=True)

    # class Meta:
        # managed = True
        # db_table = 'oferty_biuro'


class OfertyRodzaj(models.Model):
    '''
    Rodzaj transakcji: sprzedaż, wynajem
    '''
    nazwa = models.CharField(max_length=15)
    nazwa_msc = models.CharField(max_length=15)
    nazwa_d = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'oferty_rodzaj'


class OfertyTyp(models.Model):
    '''
    Typ nieruchomości: dom, mieszkanie, grunt, lokal handlowy, garaż,
    pensjonat
    '''
    nazwa = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'oferty_typ'

    def __str__(self):
        return self.nazwa


class OfertyEst(models.Model):
    '''
    Główna tabela ofert
    '''
    rodzaj = models.ForeignKey('OfertyRodzaj', on_delete=models.CASCADE)
    typ = models.ForeignKey('OfertyTyp', on_delete=models.CASCADE)
    status = models.IntegerField()
    data = models.DateField()
    nazwa = models.ForeignKey('OfertyNazwa', on_delete=models.CASCADE)
    miasto = models.ForeignKey('OfertyMiasto', on_delete=models.CASCADE)
    pow = models.IntegerField()
    cena = models.IntegerField()
    metr = models.BooleanField()
    opis = models.TextField(blank=True)
    stan = models.NullBooleanField()
    kto = models.IntegerField(blank=True, null=True)
    zdjecia = models.IntegerField(default='0')
    pdf = models.IntegerField(default='0', null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'oferty_est'


class OfertyEstPhoto(models.Model):
    '''
    Tabela zdjęć
    '''
    est = models.ForeignKey('OfertyEst', on_delete=models.CASCADE)
    filename = models.CharField(max_length=30)
    position = models.IntegerField(default='0')
    width = models.IntegerField(default='0')
    height = models.IntegerField(default='0')
    thumbnail = models.NullBooleanField()

    class Meta:
        managed = True
        db_table = 'oferty_est_photo'


class OfertyFpage(models.Model):
    est = models.OneToOneField('OfertyEst', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_fpage'


class OfertyOpisb(models.Model):
    '''
    Opis budynku
    '''
    est = models.OneToOneField(
        'OfertyEst', on_delete=models.CASCADE, null=True)
    rok_bud = models.CharField(max_length=350, blank=True, null=True)
    budulec = models.CharField(max_length=350, blank=True, null=True)
    stan = models.CharField(max_length=300, blank=True, null=True)
    dach = models.CharField(max_length=350, blank=True, null=True)
    poddasze = models.CharField(max_length=300, blank=True, null=True)
    piwnica = models.CharField(max_length=300, blank=True, null=True)
    ogrzew = models.CharField(max_length=300, blank=True, null=True)
    garaz = models.CharField(max_length=350, blank=True, null=True)
    ogrodz = models.CharField(max_length=350, blank=True, null=True)
    otoczenie = models.CharField(max_length=300, blank=True, null=True)
    pow = models.IntegerField(blank=True, null=True)
    parter = models.CharField(max_length=350, blank=True, null=True)
    ip = models.CharField(max_length=350, blank=True, null=True)
    stropy = models.CharField(max_length=350, blank=True, null=True)
    elewacja = models.CharField(max_length=350, blank=True, null=True)
    okna = models.CharField(max_length=350, blank=True, null=True)
    drzwi = models.CharField(max_length=350, blank=True, null=True)
    podlogi = models.CharField(max_length=350, blank=True, null=True)
    sciany = models.CharField(max_length=350, blank=True, null=True)
    gaz = models.CharField(max_length=350, blank=True, null=True)
    woda = models.CharField(max_length=350, blank=True, null=True)
    kan = models.CharField(max_length=350, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'oferty_opisb'


class OfertyOpism(models.Model):
    '''
    Opis mieszkań i lokali handlowych chyba
    '''
    est = models.OneToOneField(
        'OfertyEst', on_delete=models.CASCADE, null=True)
    pietro = models.IntegerField(blank=True, null=True)
    il_pie = models.IntegerField(blank=True, null=True)
    stan = models.CharField(max_length=150, blank=True, null=True)
    il_pok = models.IntegerField(blank=True, null=True)
    wc = models.NullBooleanField()
    wyp = models.CharField(max_length=300, blank=True, null=True)
    wyp_dod = models.CharField(max_length=300, blank=True, null=True)
    okna = models.CharField(max_length=150, blank=True, null=True)
    sciany = models.CharField(max_length=150, blank=True, null=True)
    podlogi = models.CharField(max_length=150, blank=True, null=True)
    balkon = models.CharField(max_length=150, blank=True, null=True)
    garaz = models.CharField(max_length=150, blank=True, null=True)
    lok = models.CharField(max_length=150, blank=True, null=True)
    ogrz = models.CharField(max_length=150, blank=True, null=True)
    czynsz = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'oferty_opism'


class OfertyDBBtName(models.Model):
    '''
    Typ budynku (built type)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)
    name_gratka = models.CharField(max_length=50, null=True)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_bt_name'


class OfertyDBTName(models.Model):
    '''
    Przeznaczenie budynku (target)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_t_name'


class OfertyDFbSName(models.Model):
    '''
    Stan techniczny (state)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_fb_s_name'


class OfertyDBGtName(models.Model):
    '''
    Typ garażu (garage type)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_gt_name'


class OfertyDBSsName(models.Model):
    '''
    Ilość kondygnacji (stories)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_ss_name'


class OfertyDFbtLtName(models.Model):
    '''
    Lokalizacja (location type)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_fbt_lt_name'


class OfertyDBGttName(models.Model):
    '''
    Poddasze (garet type)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_gtt_name'


class OfertyDBRdtName(models.Model):
    '''
    Dojazd (road type)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_rdt_name'


class OfertyDBRtName(models.Model):
    '''
    Dach (roof type)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_rt_name'


class OfertyDFbCmName(models.Model):
    '''
    Budulec
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_fb_cm_name'


class OfertyDFbFmName(models.Model):
    '''
    Podłogi (floors)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_fb_fm_name'


class OfertyDFbWmName(models.Model):
    '''
    Okna (windows)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_fb_wm_name'


class OfertyDFbtLmName(models.Model):
    '''
    Lokalizacja (location)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_fbt_lm_name'


class OfertyDBEmName(models.Model):
    '''
    Dodatki dom (extras)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_em_name'


class OfertyDFEmName(models.Model):
    '''
    Dodatki mieszkanie (extras)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_f_em_name'


class OfertyDBHmName(models.Model):
    '''
    Ogrzewanie (heating)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_hm_name'


class OfertyDBMmName(models.Model):
    '''
    Media
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_mm_name'


class OfertyDBFcmName(models.Model):
    '''
    Ogrodzenie (fence)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_fcm_name'


class OfertyDFBtName(models.Model):
    '''
    Tyb budynku (buildingtype)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_f_bt_name'


class OfertyDFFoName(models.Model):
    '''
    Rodzaj własności (flatownership)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_f_fo_name'


class OfertyDFHName(models.Model):
    '''
    Ogrzewanie (heating)
    '''
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_de = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'oferty_d_f_h_name'


class OfertyDFbCm(models.Model):
    '''
    Budulec
    '''
    est = models.ForeignKey('OfertyEst', on_delete=models.CASCADE)
    cm = models.ForeignKey('OfertyDFbCmName', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_d_fb_cm'


class OfertyDFbFm(models.Model):
    '''
    Podłogi (floors)
    '''
    est = models.ForeignKey('OfertyEst', on_delete=models.CASCADE)
    fm = models.ForeignKey('OfertyDFbFmName', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_d_fb_fm'


class OfertyDFbWm(models.Model):
    '''
    Okna (windows)
    '''
    est = models.ForeignKey('OfertyEst', on_delete=models.CASCADE)
    wm = models.ForeignKey('OfertyDFbWmName', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_d_fb_wm'


class OfertyDFbtLm(models.Model):
    '''
    Lokalizacja (location)
    '''
    est = models.ForeignKey('OfertyEst', on_delete=models.CASCADE)
    lm = models.ForeignKey('OfertyDFbtLmName', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_d_fbt_lm'


class OfertyDBEm(models.Model):
    '''
    Dodatki dom (extras)
    '''
    est = models.ForeignKey('OfertyEst', on_delete=models.CASCADE)
    em = models.ForeignKey('OfertyDBEmName', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_em'


class OfertyDFEm(models.Model):
    '''
    Dodatki mieszkanie (extras)
    '''
    est = models.ForeignKey('OfertyEst', on_delete=models.CASCADE)
    em = models.ForeignKey('OfertyDFEmName', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_d_f_em'


class OfertyDBHm(models.Model):
    '''
    Ogrzewanie (heating)
    '''
    est = models.ForeignKey('OfertyEst', on_delete=models.CASCADE)
    hm = models.ForeignKey('OfertyDBHmName', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_hm'


class OfertyDBMm(models.Model):
    '''
    Media
    '''
    est = models.ForeignKey('OfertyEst', on_delete=models.CASCADE)
    mm = models.ForeignKey('OfertyDBMmName', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_mm'


class OfertyDBFcm(models.Model):
    '''
    Ogrodzenie (fence)
    '''
    est = models.ForeignKey('OfertyEst', on_delete=models.CASCADE)
    fcm = models.ForeignKey('OfertyDBFcmName', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_d_b_fcm'


class OfertyDB(models.Model):
    '''
    Opis budynku
    '''
    est = models.OneToOneField('OfertyEst', on_delete=models.CASCADE)
    bt = models.ForeignKey('OfertyDBBtName', on_delete=models.CASCADE)
    builtyear = models.IntegerField()
    t = models.ForeignKey('OfertyDBTName', on_delete=models.CASCADE)
    s = models.ForeignKey('OfertyDFbSName', on_delete=models.CASCADE)
    roomnum = models.IntegerField()
    bathnum = models.IntegerField()
    garageplaces = models.IntegerField()
    gt = models.ForeignKey('OfertyDBGtName', on_delete=models.CASCADE)
    ss = models.ForeignKey('OfertyDBSsName', on_delete=models.CASCADE)
    lt = models.ForeignKey('OfertyDFbtLtName', on_delete=models.CASCADE)
    gtt = models.ForeignKey('OfertyDBGttName', on_delete=models.CASCADE)
    rdt = models.ForeignKey('OfertyDBRdtName', on_delete=models.CASCADE)
    rt = models.ForeignKey('OfertyDBRtName', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'oferty_d_b'


class OfertyDF(models.Model):
    '''
    Opis mieszkania
    '''
    est = models.OneToOneField('OfertyEst', on_delete=models.CASCADE)
    buildingtype = models.ForeignKey('OfertyDFBtName',
                                     on_delete=models.CASCADE)
    builtyear = models.IntegerField()
    flatownership = models.ForeignKey('OfertyDFFoName',
                                      on_delete=models.CASCADE)
    status = models.ForeignKey('OfertyDFbSName', on_delete=models.CASCADE)
    roomnum = models.IntegerField()
    floorno = models.IntegerField()
    floornum = models.IntegerField()
    heating = models.ForeignKey('OfertyDFHName', on_delete=models.CASCADE)
    locationtype = models.ForeignKey('OfertyDFbtLtName',
                                     on_delete=models.CASCADE)
    rent = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'oferty_d_f'
