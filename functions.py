def show_info(*numbers,**info):

    print(info)
    print(numbers)
    print("Information Received")
    for key,value in info.items():

        print(key,value)


show_info(3,4,3,4,2,3,name="Akash",age=25,country="USA")


#*number -> tuple
#**info -> dictionary(Key,value pairs)