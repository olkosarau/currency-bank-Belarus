import requests
from bankcurrency.models import Auth
from datetime import datetime
from rest_framework.views import Response
import xml.etree.ElementTree as et


def alfabank(self):
    curr_req = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
    data = curr_req.json()
    cur_rur_sell = data['rates'][3]['buyRate']
    cur_rur_buy = data['rates'][3]['sellRate']
    cur_eur_sell = data['rates'][4]['buyRate']
    cur_eur_buy = data['rates'][4]['sellRate']
    cur_usd_sell = data['rates'][5]['buyRate']
    cur_usd_buy = data['rates'][5]['sellRate']
    date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

    cur_new = Auth.objects.create(company=Auth.ALPHABANK, eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
                                  usd_buy=cur_usd_buy, usd_sell=cur_usd_sell, rur_buy=cur_rur_buy,
                                  rur_sell=cur_rur_sell)
    cur_new.save()
    return Response({'company': Auth.ALPHABANK,
                     'usd_buy': cur_usd_buy,
                     'usd_sell': cur_usd_sell,
                     'eur_buy': cur_eur_buy,
                     'eur_sell': cur_eur_sell,
                     'rur_buy': cur_rur_buy,
                     'rur_sell': cur_rur_sell,
                     'date': date_time_obj
                     })


def belagro(self):
    curr_req = requests.get('https://belapb.by/ExCardsDaily.php?')
    print(curr_req.status_code)
    tree = et.ElementTree(et.fromstring(curr_req.text))
    root = tree.getroot()

    s_date = datetime.now().strftime("%d-%m-%Y %H:%M")
    s_eur_buy = root[1][3].text
    s_eur_sell = root[1][4].text
    s_usd_buy = root[0][3].text
    s_usd_sell = root[0][4].text
    s_rur_buy = root[2][3].text
    s_rur_sell = root[2][4].text

    cur_new = Auth.objects.create(company=Auth.BELAGROPROMBANK, eur_buy=s_eur_buy, eur_sell=s_eur_sell,
                                  usd_buy=s_usd_buy, usd_sell=s_usd_sell, rur_buy=s_rur_buy,
                                  rur_sell=s_rur_sell)
    cur_new.save()
    return Response({'company': Auth.BELAGROPROMBANK,
                     'usd_buy': s_usd_buy,
                     'usd_sell': s_usd_sell,
                     'eur_buy': s_eur_buy,
                     'eur_sell': s_eur_sell,
                     'rur_buy': s_rur_buy,
                     'rur_sell': s_rur_sell,
                     'date': s_date
                     })


def belarusbank(self):
    curr_req = requests.get('https://belarusbank.by/api/kursExchange?city=Минск')
    data = curr_req.json()
    cur_rur_buy = data[0]['RUB_in']
    cur_rur_sell = data[0]['RUB_out']
    cur_eur_buy = data[0]['EUR_in']
    cur_eur_sell = data[0]['EUR_out']
    cur_usd_buy = data[0]['USD_in']
    cur_usd_sell = data[0]['USD_out']

    date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

    cur_new = Auth.objects.create(company=Auth.BELARUSBANK, eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
                                  usd_buy=cur_usd_buy, usd_sell=cur_usd_sell, rur_buy=cur_rur_buy,
                                  rur_sell=cur_rur_sell)
    cur_new.save()
    response = Response({'company': Auth.BELARUSBANK,
                         'usd_buy': cur_usd_buy,
                         'usd_sell': cur_usd_sell,
                         'eur_buy': cur_eur_buy,
                         'eur_sell': cur_eur_sell,
                         'rur_buy': cur_rur_buy,
                         'rur_sell': cur_rur_sell,
                         'date': date_time_obj
                         })
    return response
