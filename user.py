import main
# import tests

sale_example = main.sale()
buy_example = main.buy()

while True:
    command = input('\nВведите команду - add, get, del, view, exit: ')

    # add, get, del
    if command == 'add' or command == 'get' or command == 'del':
        request_type = input('Введите тип завяки - "sale", "buy": ')

        # sale
        if request_type == 'sale':
            if command == 'add':
                quantity = input('Введите кол-во: ')
                price = input('Введите цену: ')
                request_id, actual, expected = sale_example.add(quantity, price) 
                print(f'id вашей заявки: {request_id}')

            elif command == 'get':
                request_id = input('Введите id заявки: ')
                print(sale_example.get(request_id))

            elif command == 'del':
                request_id = input('Введите id заявки: ')
                sale_example.delete(request_id)

        # buy
        elif request_type == 'buy':
            if command == 'add':
                quantity = input('Введите кол-во: ')
                price = input('Введите цену: ')
                request_id, actual, expected = buy_example.add(quantity, price)
                print(f'id вашей заявки: {request_id}')
            
            elif command == 'get':
                request_id = input('Введите id заявки: ')
                print(buy_example.get(request_id))

            elif command == 'del':
                request_id = input('Введите id заявки: ')
                buy_example.delete(request_id)
        
        # неизвестный тип
        else:
            print(f'Неизвестный тип - {request_type}')

    # view
    elif command == 'view':
        print(sale_example.view())
        print(buy_example.view())
    
    # exit
    elif command == 'exit':
        break
    
    # неизвестная команда
    else:
        print(f'Неизвестная команда - {command}')