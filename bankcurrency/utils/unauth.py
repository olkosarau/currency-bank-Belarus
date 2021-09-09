import requests
from bankcurrency.models import CurrencyUnAuthUser
import xml.etree.ElementTree as ET

from bankcurrency.serializers import CurrencyUnAuthUserSerializer


def alfabankun():
    curr_req = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
    data = curr_req.json()
    cur_rur_sell = data['rates'][3]['buyRate']
    cur_eur_sell = data['rates'][4]['buyRate']
    cur_usd_sell = data['rates'][5]['buyRate']

    queryset = CurrencyUnAuthUser.objects.create(company=CurrencyUnAuthUser.ALPHABANK, eur=cur_eur_sell,
                                             usd=cur_usd_sell, rur=cur_rur_sell)
    return queryset


def belagroun():
    curr_req = requests.get('https://belapb.by/ExCardsDaily.php?')
    tree = ET.ElementTree(ET.fromstring(curr_req.text))
    root = tree.getroot()

    s_eur_sell = root[1][4].text
    s_usd_sell = root[0][4].text
    s_rur_sell = root[2][4].text

    queryset = CurrencyUnAuthUser.objects.create(company=CurrencyUnAuthUser.BELAGROPROMBANK, eur=s_eur_sell,
                                             usd=s_usd_sell, rur=s_rur_sell)
    return queryset


def belarusbankun():
    curr_req = requests.get('https://belarusbank.by/api/kursExchange?city=Минск')
    data = curr_req.json()
    cur_rur_sell = data[0]['RUB_out']
    cur_eur_sell = data[0]['EUR_out']
    cur_usd_sell = data[0]['USD_out']

    queryset = CurrencyUnAuthUser.objects.create(company=CurrencyUnAuthUser.BELARUSBANK, eur=cur_eur_sell,
                                             usd=cur_usd_sell, rur=cur_rur_sell)
    return queryset


