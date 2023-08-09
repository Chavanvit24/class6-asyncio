import asyncio
import time

class Coffee:
    pass
class Egg:
    pass
class Toast:
    pass

def PourCoffee():
    print("Pouring coffee")
    return Coffee()

async def ApplyButter():
    print("Spreading butter on toast")
    await asyncio.sleep(1)

async def FryEggsAsync(howMany):
    print("Heat pan to fry eggs")
    await asyncio.sleep(3)
    print("Frying",howMany,"eggs")
    await asyncio.sleep(3)
    print("Eggs are ready")
    return Egg()

async def ToastAsync(slices):
    for slice in range(slices):
      print("Toasting bread", slice + 1)
      await asyncio.sleep(3)
      print("Bread", slice + 1, "toasted")
      await ApplyButter()
      print("Toast", slice + 1, "ready")
    return Toast()

async def main():
    cup = PourCoffee()
    print(f"{time.ctime()} - Coffee is ready")
    await asyncio.gather(FryEggsAsync(2),ToastAsync(2))
    
if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{time.ctime()} - Breakfast cooked in",elapsed,"seconds.")

#Pouring coffee
#Wed Aug  9 15:02:13 2023 - Coffee is ready
#Heat pan to fry eggs
#Toasting bread 1
#Frying 2 eggs
#Bread 1 toasted
#Spreading butter on toast
#Toast 1 ready
#Toasting bread 2
#Eggs are ready
#Bread 2 toasted
#Spreading butter on toast
#Toast 2 ready
#Wed Aug  9 15:02:21 2023 - Breakfast cooked in 8.042351899901405 seconds.