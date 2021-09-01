from devtest.celery import app
import requests
from bankcurrency.models import Auth
import xml.etree.ElementTree as ET


@app.task
def create_alphabank_currency():
    curr_req = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
    data = curr_req.json()
    cur_rur_sell = data['rates'][3]['buyRate']
    cur_rur_buy = data['rates'][3]['sellRate']
    cur_eur_sell = data['rates'][4]['buyRate']
    cur_eur_buy = data['rates'][4]['sellRate']
    cur_usd_sell = data['rates'][5]['buyRate']
    cur_usd_buy = data['rates'][5]['sellRate']

    Auth.objects.create(company=Auth.ALPHABANK, eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
                        usd_buy=cur_usd_buy, usd_sell=cur_usd_sell,
                        rur_buy=cur_rur_buy, rur_sell=cur_rur_sell)


@app.task
def create_belagro_currency():
    curr_req = requests.get('https://belapb.by/ExCardsDaily.php?')
    tree = ET.ElementTree(ET.fromstring(curr_req.text))
    root = tree.getroot()

    s_eur_buy = root[1][3].text
    s_eur_sell = root[1][4].text
    s_usd_buy = root[0][3].text
    s_usd_sell = root[0][4].text
    s_rur_buy = root[2][3].text
    s_rur_sell = root[2][4].text

    Auth.objects.create(company=Auth.BELAGROPROMBANK, eur_buy=s_eur_buy, eur_sell=s_eur_sell,
                        usd_buy=s_usd_buy, usd_sell=s_usd_sell,
                        rur_buy=s_rur_buy, rur_sell=s_rur_sell)


@app.task
def create_belarusbank_currency():
    curr_req = requests.get('https://belarusbank.by/api/kursExchange?city=Минск')
    data = curr_req.json()
    cur_rur_buy = data[0]['RUB_in']
    cur_rur_sell = data[0]['RUB_out']
    cur_eur_buy = data[0]['EUR_in']
    cur_eur_sell = data[0]['EUR_out']
    cur_usd_buy = data[0]['USD_in']
    cur_usd_sell = data[0]['USD_out']

    Auth.objects.create(company=Auth.BELARUSBANK, eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
                        usd_buy=cur_usd_buy, usd_sell=cur_usd_sell,
                        rur_buy=cur_rur_buy, rur_sell=cur_rur_sell)
