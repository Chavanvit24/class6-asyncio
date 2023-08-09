"""
ต้องการซักผ้า 2 ตะกร้า แบบ synchronous io
กระบวนการซักผ้า 1 ตะกร้า คือ
1. หยอดเหรียญเพื่อซักผ้า
2. นำผ้าเข้าเครื่องซักผ้า
3. ซักผ้าเสร็จ (ใช้เวลา 5 วินาที)

เนื่องจากมีเครื่องซักผ้าที่สามารถพร้อมใช้งานได้ 2 เครื่องพร้อมกัน 
"""

import time

def wash(basket):
    print(f'{time.ctime()} - Washing Machine ({basket}): Put the coin')
    print(f'{time.ctime()} - Washing Machine ({basket}): Start washing...')
    time.sleep(5)
    print(f'{time.ctime()} - Washing Machine ({basket}): Finished washing')
    return f'{basket} is completed'

def main():
    for basket in ['Basket A', 'Basket B']:
        wash(basket)

if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')

#Wed Aug  9 15:07:19 2023 - Washing Machine (Basket A): Put the coin
#Wed Aug  9 15:07:19 2023 - Washing Machine (Basket A): Start washing...
#Wed Aug  9 15:07:24 2023 - Washing Machine (Basket A): Finished washing
#Wed Aug  9 15:07:24 2023 - Washing Machine (Basket B): Put the coin
#Wed Aug  9 15:07:24 2023 - Washing Machine (Basket B): Start washing...
#Wed Aug  9 15:07:29 2023 - Washing Machine (Basket B): Finished washing
#Executed in 10.00 seconds.