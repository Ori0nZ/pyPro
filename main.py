import os
def menu_display():
    print('------------------------------\n'
            '     Lab3 - Thuc Anh         \n'
            '-----------------------------\n'
            ' Funtion Program:           \n'
            '0. Exit program\n'
            '1. File View\n'
            '2. Product View by name\n'
            '3. Product View by number\n'
            '4. Add product\n')
    user_choice = input("Type your choice:")
    if(user_choice=='1'):
        file_count()
    elif(user_choice=='0'):
        print("End")
        exit(0)
    elif(user_choice=='2'):
        product_count()
    elif(user_choice=='3'):
        product_number()
    elif(user_choice=='4'):
        add_product()
    else:
        menu_display()
def type_choice():
    user_choice = input("no/N/0 to exit, yes/Y/1 to menu:")
    if(user_choice=='0' or user_choice.upper()=='N' or user_choice.upper()=='NO'):
        print("Program end!!")
        exit(0)
    elif(user_choice=='1'or user_choice.upper()=='Y' or user_choice.upper()=='YES'):
        menu_display()
    else:
        print("Type don't valid, again!")
        type_choice()
def file_count():
    onlyfiles = next(os.walk('.'))[2] 
    print('Folder have', len(onlyfiles),"files\n")
    for file in onlyfiles:
        print(file)
    print('\n')
    type_choice()
def product_count():
    f = open('products.txt', 'r')
    products = f.readlines()
    list_products= list()
    for product in products:
        if(len(list(product.split(";")))<4):
            continue
        list_products.append(list(product.split(";")))
    list_products=  sorted(list_products, key = lambda i: i[1])
    for product in list_products:
        print('Product: %12s' % product[1])
        f.close()
    type_choice()
def product_number():
    f = open('products.txt', 'r')
    products = f.readlines()
    list_products= list()
    for product in products:
        stringproduct = list(product.split(";"))
        if(len(stringproduct)==4): 
            stringproduct[3] = int(stringproduct[3].replace(' ', '').replace('\n',''))
            list_products.append(stringproduct)
    list_products=  sorted(list_products, key = lambda i: i[3])
    print(list_products)
    for product in list_products:
        print('Product: %12s   ------ %6s ' % (product[1],  product[3]))
    f.close()
    type_choice()
def add_product():
    print('Product infomation: ')
    boolID = True
    while(boolID):
        boolID= False
        id = input("Type the producer ID(primary key): ")
        f = open('products.txt', 'r')
        products = f.readlines()
        list_products= list()
        for product in products:
            stringproduct = list(product.split(";"))
            if(stringproduct[0]== id):
                boolID = True
                print("ID used: type difference")
                break
    name = input("Add product name: ").upper()
    year = input("Add product years: ")
    number = input("Add product number: ")
    stringAdd = id + ";" + name + ";"+ year + ";"+ number+'\n'
    f = open('products.txt', 'a+')
    f.write(stringAdd)
    f.close()
    print("add success!")
    type_choice()
menu_display()