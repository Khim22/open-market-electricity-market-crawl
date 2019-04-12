import http.client
import requests
import json
import flask

conn = http.client.HTTPSConnection('compare.openelectricitymarket.sg')
page = 'https://compare.openelectricitymarket.sg/filterEstimatedSavingsAndCharges'

headersForFilter = {
    'authority': 'compare.openelectricitymarket.sg',
    'method': 'POST',
    'path': '/filterEstimatedSavingsAndCharges',
    'scheme': 'https',
    '_settings': '[object Object]',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '336',
    'Content-Type':'application/json',
    'origin': 'https://compare.openelectricitymarket.sg',
    'referer': 'https://compare.openelectricitymarket.sg/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

bodyForFilter = {
    "estimationFlag":'true',"monthlyConsumption":"100.00","housingType":"HDB 2-Room","startIndex":'1',"multiretailersearchfield":"retailerCode:BESTPE,retailerCode:DEMPL","sortBy":"estimatedChargesAsc","searchCriteriaAnd":'null',"searchCriteriaOr":"customerType:RES,customerType:BTH","searchCriteriaOfferOr":"offerType:FR"
}

r = requests.post(page, headers=headersForFilter, json=bodyForFilter)
print(bodyForFilter)
hhh = json.dumps(bodyForFilter)
# print(r.text)


# ###############################

page2 = 'https://compare.openelectricitymarket.sg/compareOffersEstimatedSavingsAndCharges'

headersForCompare = {
    'authority': 'compare.openelectricitymarket.sg',
    'method': 'POST',
    'path': '/compareOffersEstimatedSavingsAndCharges',
    'scheme': 'https',
    '_settings': '[object Object]',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '168',
    'Content-Type':'application/json',
    'origin': 'https://compare.openelectricitymarket.sg',
    'referer': 'https://compare.openelectricitymarket.sg/',
    'TE': 'Trailers',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.3'
}

bodyForCompare = {
    'estimationFlag':True,
    'monthlyConsumption':"100.00",
    'housingType':"HDB 4-Room",
    'offerIds':["ISWTPL180032","ESASIA180003","ESASIA180004","BESTPE180017","BESTPE180016"]
}

jjj = flask.jsonify(estimationFlag=True,monthlyConsumption="100.00",housingType="HDB 4-Room",offerIds=["ISWTPL180032","ESASIA180003","ESASIA180004","BESTPE180017","BESTPE180016"])

hhh = json.dumps(bodyForCompare, separators=(',', ':'))
# rd = requests.post(page, headers=headersForCompare, json=jjj)

print(jjj)
