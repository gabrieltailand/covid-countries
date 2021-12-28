import requests
import json

dados_covid = requests.get('https://covid19-api.com/country/all?format=json" -H "accept: application/json')
dados_covid = dados_covid.json()

while True:
    pos = 0
    for c in dados_covid:
        pais = dados_covid[pos]['country']
        pos += 1
        num_pais = 0
        nome_pais = ''
    for p in pais:
        num_pais = pos
        nome_pais = pais

    escolha = int(input('Qual a opção? '))
    pais = (dados_covid[escolha])
    country = (pais['country'])
    confirmed = (pais['confirmed'])
    recovered = (pais['recovered'])
    critical = (pais['critical'])
    deaths = (pais['deaths'])
    lastChange = (pais['lastChange'])
    new_dados_covid = {'Country': country, 'Confirmed': confirmed, 'Recovered': recovered, 'Critical': critical,
                       'Deaths': deaths, 'Last Change': lastChange}

    # if escolha == num_pais:
    #     num_pais = nome_pais
    print(f'O número {escolha} corresponde ao país {pais["country"]}')
    print(new_dados_covid)

    resp = ''
    resp = str(input('Quer continuar [S/N] ? ')).strip().upper()
    if resp == 'N':
        break

print('Consulta finalizada. VOLTE SEMPRE!!!')