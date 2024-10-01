import asyncio
import requests


async def function1():
    print("func 1")
    URL = "https://uniquehimachal.com/wp-content/uploads/2021/06/leh-5.jpg"
    response = requests.get(URL)
    open("Random1.jpg", "wb").write(response.content)

    return "Harry"


async def function2():
    print("func 2")
    URL = "https://unsplash.com/photos/y97sM41-g9k/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8Mnx8amFpcHVyfGVufDB8fHx8MTY4MzQ0NzUxMg&force=true.jpg"
    response = requests.get(URL)
    open("Random2.jpg", "wb").write(response.content)


async def function3():
    print("func 3")
    URL = "https://www.wallpapers13.com/wp-content/uploads/2019/07/Stockholm-Capital-of-Sweden-sunset-Landscape-Photography-4K-Ultra-HD-TV-Wallpaper-for-Desktop-Laptop-Tablet-And-Mobile-Phones-1920x1200-1920x1080.jpg"
    response = requests.get(URL)
    open("Random3.jpg", "wb").write(response.content)


async def main():
    # await function1()
    # await function2()
    # await function3()
    # return 3
    
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)

    # task = asyncio.create_task(function1())   # To get better organisation of things we use the above gather syntax
    # # await function1()
    # await function2()
    # await function3()

asyncio.run(main())
