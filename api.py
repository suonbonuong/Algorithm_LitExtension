import csv
import requests

def get_data():
    url = 'https://001a625b56445c9005594031ec9f724d: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@shadowbqt.myshopify.com/admin/api/2020-07/customers.json'
    r = requests.get(url)
    return r.json()


data = get_data()['customers']
keys = data[0].keys()
with open("data.csv", 'wt') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow([key for key in keys])
    for info in data:
        writer.writerow([i for i in info.values()])
