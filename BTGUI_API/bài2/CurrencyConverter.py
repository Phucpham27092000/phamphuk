import requests

DATA = []
def Converter(oldAmount, oldCurrency, newCurrency):
    api_url = 'https://api.api-ninjas.com/v1/convertcurrency?want='
    
    get_api_url = api_url + newCurrency + "&have=" + oldCurrency + "&amount=" + str(oldAmount)
    response = requests.get(get_api_url, headers={'X-Api-Key': 'IfzWzBmhbTmFJUEokWeHiw==oyv8AU3ljJ9u45Wi'}).json()
    
    DATA.append(response['old_amount'])
    DATA.append(response['old_currency'])
    DATA.append(response['new_currency'])
    DATA.append(response['new_amount'])

