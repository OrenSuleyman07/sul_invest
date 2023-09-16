import main
# import tests

sale_example = main.sale()
buy_example = main.buy()

while True:
    command = input('\nВведите команду - add, get, del, view, exit: ').strip()

    # add, get, del
    if command in ('add', 'get', 'del'):
        request_type = input('Введите тип завяки - "sale", "buy": ').strip()

        # sale
        if request_type == 'sale':
            if command == 'add':
                quantity = input('Введите кол-во: ').strip()
                price = input('Введите цену: ').strip()
                request_id = sale_example.add(quantity, price) 
                print(f'id вашей заявки: {request_id}')

            elif command == 'get':
                request_id = input('Введите id заявки: ').strip()
                print(sale_example.get(request_id))

            elif command == 'del':
                request_id = input('Введите id заявки: ').strip()
                sale_example.delete(request_id)

        # buy
        elif request_type == 'buy':
            if command == 'add':
                quantity = input('Введите кол-во: ').strip()
                price = input('Введите цену: ').strip()
                request_id= buy_example.add(quantity, price)
                print(f'id вашей заявки: {request_id}')
            
            elif command == 'get':
                request_id = input('Введите id заявки: ').strip()
                print(buy_example.get(request_id))

            elif command == 'del':
                request_id = input('Введите id заявки: ').strip()
                buy_example.delete(request_id)
        
        # неизвестный тип
        else:
            print(f'Неизвестный тип - {request_type}')

    # view
    elif command == 'view':
        print(sale_example.view(), buy_example.view(), sep='\n')
    
    # exit
    elif command == 'exit':
        break
    
    # неизвестная команда
    else:
        print(f'Неизвестная команда - {command}')