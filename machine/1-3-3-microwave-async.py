"""
การรัน Task หรือ Coroutine พร้อมกันหลายตัว
เราสามารถใช้ method ในการรัน task หรือ coroutine พร้อมกันหลายงานได้ โดยผมจะขอยกตัวอย่างมา 3 ตัว คือ
1. asyncio.gather()
2. asyncio.wait()
3. asyncio.as_completed()


ซึ่งความแตกต่างระหว่าง 2 ตัวนี้ คือ
- asyncio.gather() จะรันเรียงตามลำดับก่อนหลัง ส่วน asyncio.wait() และ asyncio.as_completed() นั้นไม่เรียง
- asyncio.gather() ไม่สามารถกำหนด timeout ได้ แต่ asyncio.wait() กำหนดได้ผ่านพารามิเตอร์ timeout
- asyncio.wait() สามารถกำหนดเงื่อนไขในการรอได้โดยใช้พารามิเตอร์ return_when
- asyncio.gather() ไม่สามารถรับค่าเป็น list ของ coroutine/task ได้โดยตรงแบบ asyncio.wait() ให้ใช้ * หน้า list เพื่อกระจายเป็น argument แทน
- asyncio.as_completed() จะใช้กับ for Loop ซึ่งไม่เหมือนตัวอื่น และเป็น for Loop ที่ทุกรอบเริ่มทำงานพร้อมกัน

จงเปรียบเทียบผลของการสร้าง Task ระหว่าง gather(), wait() และ as_completed()

"""

import asyncio
import time

async def cook(food, t):
    print(f'{time.ctime()} - Microwave ({food}): Cooking {t} seconds...')
    await asyncio.sleep(t)
    print(f'{time.ctime()} - Microwave ({food}): Finished cooking')
    return f'{food} is completed'
    

async def main():
    coros = [cook('Rice', 3), cook('Noodle', 3), cook('Curry', 3)]
    for coro in asyncio.as_completed(coros):
        result = await coro
        print(result)

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')



#Wed Aug  9 14:44:04 2023 - Microwave (Noodle): Cooking 3 seconds...
#Wed Aug  9 14:44:04 2023 - Microwave (Curry): Cooking 3 seconds...
#Wed Aug  9 14:44:04 2023 - Microwave (Rice): Cooking 3 seconds...
#Wed Aug  9 14:44:07 2023 - Microwave (Noodle): Finished cooking
#Wed Aug  9 14:44:07 2023 - Microwave (Curry): Finished cooking
#Wed Aug  9 14:44:07 2023 - Microwave (Rice): Finished cooking
#Noodle is completed
#Curry is completed
#Rice is completed
#Executed in 3.02 seconds.