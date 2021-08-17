import requests
from bankcurrency.models import UnAuth
from datetime import datetime
from rest_framework.views import Response
import xml.etree.ElementTree as et


def alfabankun(self):
    curr_req = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
    data = curr_req.json()
    cur_rur_sell = data['rates'][3]['buyRate']
    cur_eur_sell = data['rates'][4]['buyRate']
    cur_usd_sell = data['rates'][5]['buyRate']
    date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

    cur_new = UnAuth.objects.create(company=UnAuth.ALPHABANK, eur=cur_eur_sell,
                                    usd=cur_usd_sell, rur=cur_rur_sell)
    cur_new.save()
    return Response({'company': UnAuth.ALPHABANK,
                     'usd': cur_usd_sell,
                     'eur': cur_eur_sell,
                     'rur': cur_rur_sell,
                     'date': date_time_obj
                     })


def belagroun(self):
    curr_req = requests.get('https://belapb.by/ExCardsDaily.php?')
    print(curr_req.status_code)
    tree = et.ElementTree(et.fromstring(curr_req.text))
    root = tree.getroot()

    s_date = datetime.now().strftime("%d-%m-%Y %H:%M")
    s_eur_sell = root[1][4].text
    s_usd_sell = root[0][4].text
    s_rur_sell = root[2][4].text

    cur_new = UnAuth.objects.create(company=UnAuth.BELAGROPROMBANK, eur=s_eur_sell,
                                    usd=s_usd_sell, rur=s_rur_sell)
    cur_new.save()
    return Response({'company': UnAuth.BELAGROPROMBANK,
                     'usd': s_usd_sell,
                     'eur': s_eur_sell,
                     'rur': s_rur_sell,
                     'date': s_date
                     })


def belarusbankun(self):
    curr_req = requests.get('https://belarusbank.by/api/kursExchange?city=Минск')
    data = curr_req.json()
    cur_rur_sell = data[0]['RUB_out']
    cur_eur_sell = data[0]['EUR_out']
    cur_usd_sell = data[0]['USD_out']

    date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

    cur_new = UnAuth.objects.create(company=UnAuth.BELARUSBANK, eur=cur_eur_sell,
                                    usd=cur_usd_sell, rur=cur_rur_sell)
    cur_new.save()
    return Response({'company': UnAuth.BELARUSBANK,
                     'usd': cur_usd_sell,
                     'eur': cur_eur_sell,
                     'rur': cur_rur_sell,
                     'date': date_time_obj
                     })
