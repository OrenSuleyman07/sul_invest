import main

sale_example = main.sale()
buy_example = main.buy()

# класс создания заявки
class create():
    # создание заявки на продажу, выдача его id, саму заявку и ожидаемую заявку
    def create_sale(self, quantity, price):
        request_id = sale_example.add(quantity, price)
        actual = sale_example.get(request_id)
        expected = sale_example.request_list(quantity, price)
        return request_id, expected, actual

    # создание заявки на покупку, выдача его id, саму заявку и ожидаемую заявку
    def create_buy(self, quantity, price):
        request_id = buy_example.add(quantity, price)
        actual = buy_example.get(request_id)
        expected = buy_example.request_list(quantity, price)
        return request_id, expected, actual

# экземпляр класса создания заявки
create_example = create()

# тест на проверку соответсвия добавленной заяки от полученной и проверка id заявок   P.S. для заявок на продажу
def test_sale():
    request_first_id, expected_first, actual_first = create_example.create_sale(4, 10)
    if expected_first != actual_first:
        return False

    request_second_id, expected_second, actual_second = create_example.create_sale(15, 30)
    if expected_second != actual_second:
        return False


    sale_example.delete(request_first_id)

    request_third_id, expected_third, actual_third = create_example.create_sale(1, 178)
    if expected_third != actual_third:
        return False

    if expected_second != actual_second:
        return False

    return True

# тест на проверку соответсвия добавленной заяки от полученной и проверка id заявок   P.S. для заявок на покупку
def test_buy():
    request_first_id, expected_first, actual_first = create_example.create_buy(4, 10)
    if expected_first != actual_first:
        return False

    request_second_id, expected_second, actual_second = create_example.create_buy(15, 30)
    if expected_second != actual_second:
        return False


    buy_example.delete(request_first_id)

    request_third_id, expected_third, actual_third = create_example.create_buy(1, 178)
    if expected_third != actual_third:
        return False

    if expected_second != actual_second:
        return False

    return True

sale_example_view = main.sale()
buy_example_view = main.buy()
# тест на проверку просмотра всех заявок
def test_view():
    sale_example_view.add(9, 56)
    sale_example_view.add(19, 936)
    buy_example_view.add(111, 47)
    expected_first = sale_example_view.request_list(9, 56)
    expected_second = sale_example_view.request_list(19, 936)
    expected_third = buy_example_view.request_list(111, 47)

    if sale_example_view.view() != [expected_first, expected_second]:
        return False
    
    if buy_example_view.view() != [expected_third]:
        return False

    return True  

# проверка всех тестов и вывод результата
def multiple_test():
    if test_sale() == True:
        print(True)
    else:
        print('Ошибка в "test_sale"')
    if test_buy() == True:
        print(True)
    else:
        print('Ошибка в "test_buy"')
    if test_view() == True:
        print(True)
    else:
        print('Ошибка в "test_view"')

    return ''

