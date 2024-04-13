import hashlib

secret_key = 'iwrupvqb'
number = 0

while True:
    key = secret_key + str(number)
    result = hashlib.md5(key.encode()).hexdigest()
    
    if result[:6] == '000000':
        print(f'Secret Key: {key}')
        print(f'Number: {number}')
        print(f'Hash Value: {result}')
        break

    number += 1
