import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_all_params(link):
    print(link)
    headers = {
        'authority': 'www.mobile.de',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,en;q=0.9,en-US;q=0.8',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    }

    session = requests.Session()

    try:
        response = session.get(link, headers=headers)
        response.raise_for_status()

        html_code = response.text
        soup = BeautifulSoup(html_code, 'lxml')

        title_element = soup.find('h1', {'class': 'h2'})
        try:
            car_title = title_element.text.strip()
        except AttributeError as e:
            print (f"Error Car Name: {e}")
            return "-0", -0, "-0", -0
        
        car_title = car_title.replace("*", " ").strip()
        car_title = car_title.replace("+", " ").strip()
        car_title = car_title.replace('"', " ").strip()
        car_title = car_title.replace('.', " ").strip()
        car_title = car_title.replace(',', " ").strip()
        car_title = car_title.replace('/', " ").strip()
        
        price_netto_span = soup.find('span', {'class': 'netto-price'})
        price_brutto_span = soup.find('span', {'class': 'brutto-price'})
        
        price_netto_p = soup.find('p', {'class': 'netto-price'})
        price_brutto_p = soup.find('p', {'class': 'brutto-price'})
        
        price_netto_ = soup.find( {'class': 'netto-price'})
        price_brutto_ = soup.find( {'class': 'brutto-price'})

        price_elements = [price_netto_span, price_brutto_span, price_netto_p, price_brutto_p, price_netto_, price_brutto_]
        
        filtered_price = [int(ele.text.strip().split(' ')[0].replace("\xa0", "").replace("€", "").strip()) for ele in price_elements if ele]

        price_as_integer = min(filtered_price)
        # Получаем "первую регистрацию"
        registration_date_element = soup.find('span', string='Первая регистрация')
        try:
            registration_date_value = registration_date_element.find_next_sibling('span').text.strip()
        except AttributeError as e:
            print (f"Error Car Date: {e}")
            return "-0", -0, "-0", -0

        # Получаем "объем двигателя"
        engine_volume_element = soup.find('span', string='Объем двигателя')
        try:
            engine_volume_value = engine_volume_element.find_next_sibling('span').text.strip()
        except AttributeError as e:
            print (f"Error Car Value: {e}")
            return "-0", -0, "-0", -0

        print(car_title, price_as_integer, registration_date_value, int(engine_volume_value.replace("\xa0", "").replace("ссм", "").strip()))

        return car_title, price_as_integer, registration_date_value, int(engine_volume_value.replace("\xa0", "").replace("ссм", "").strip())
    
    except requests.exceptions.RequestException as e:
        print (f"Error Pars: {e}")
        return "0", 0, "09/2020", 0

def price_calculate(name, price, date, eng_volume):
    if name != "0":
        if date == "-0":
            return 0,0,0
        input_datetime = datetime.strptime(date, "%m/%Y")

        # Получение текущей даты
        current_datetime = datetime.now()
    
        # Разница в годах между входной датой и текущей датой
        years_difference = (current_datetime - input_datetime).days // 365
    
        if 3 <= years_difference <= 5:
            full_price = ((200+price)*0.06) + price +2000+600+720
    
            if 1000 <= eng_volume <= 1499:
                rate = 1.74
            elif 1500 <= eng_volume <= 1999:
                rate = 2.74
            elif 2000 <= eng_volume <= 2999:
                rate = 3.04
            elif 3000 <= eng_volume <= 3499:
                rate = 3.64
            else:
                print("Значение не соответствует ни одному диапазону.")
                return name, "Для расчёта объема свыше 3500 литров - свяжитесь с менеджером", -1 
    
            rt = (eng_volume * rate)*1.015
            full_price = (full_price+rt)*1.13
    
            return round(full_price,2), name, 0
    
        elif years_difference < 3:
            full_price = ((200+price)*0.06) + price +2000+600+720
            rt = price *0.495
            full_price = (full_price+rt)*1.13
            text = "Цена велика, однако, можно попробовать снизить итоговую стоимость автомобиля!"
            
            return round(full_price,2), name, text
        else:
            result = "Машины старше 5 лет высокая таможенная пошлина и их ввозить не выгодно."
            return name, result, -1
    else:
        return 0,0,0
