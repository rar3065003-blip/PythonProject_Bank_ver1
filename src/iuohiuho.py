transactions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "RUB"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },{"id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"}]

# for transaction in transactions:
#    print(transaction.get("description"))

import random

def card_number_generator(start, stop):
     for i in range(start, stop + 1):
        dia = 0
        dia += 1
        result_2 = f'{dia:04d}'
        temp = str(f'{random.randint(000000000000, 999999999999 ):012d}')
        result_1 = " ".join(temp[i: i + 4] for i in range(0, len(temp), 4))
        result = (result_1 + ' ' + result_2)
        return result


for card_number in card_number_generator(1,99):
     print(str(card_number))

# start = 1
# stop = 3
# dia = 0
# for i in range(start, stop + 1):
#      dia += 1
#      result_2 = f'{dia:04d}'
#      temp = str(f'{random.randint(000000000000, 999999999999 ):012d}')
#      result_1 = " ".join(temp[i: i + 4] for i in range(0, len(temp), 4))
#      result = (result_1 + ' ' + result_2)
#      print(result)