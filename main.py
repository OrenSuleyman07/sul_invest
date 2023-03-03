from collections import namedtuple

# sorting function
def sorting(start_dictionary):
    dictionary = dict.copy(start_dictionary)
    keys = list(dictionary.keys())
    for key_id in range(len(keys) - 1):
        key = keys[key_id]
        next_key = keys[key_id + 1]        
        if dictionary[key][1] > dictionary[next_key][1]:
            dictionary[key], dictionary[next_key] = dictionary[next_key], dictionary[key]
        else:
            continue
    return dictionary

# sale
class sale():
	request_list = namedtuple('Request', 'Quantity Price')

	def __init__(self):
		self.sale_list = {}
		self.last_request_id = 0

	def get(self, request_id):
		return self.sale_list.get(int(request_id), 'Заявок с таким id нет')

	def delete(self, request_id):
		del self.sale_list[int(request_id)]

	def view(self):
		checklist = sorting(self.sale_list)
		return [checklist[value] for value in checklist]

	def add(self, quantity, price):
		request_id = self.last_request_id
		self.sale_list[request_id] = self.request_list(quantity, price)
		actual = self.get(self.last_request_id)
		expected = self.request_list(quantity, price)
		self.last_request_id += 1
		return request_id, actual, expected

# buy
class buy():
	request_list = namedtuple('Request', 'Quantity Price')

	def __init__(self):
		self.buy_list = {}
		self.last_request_id = 0

	def get(self, request_id):
		return self.buy_list.get(int(request_id))

	def delete(self, request_id):
		return self.buy_list.pop(int(request_id))

	def view(self):
		checklist = sorting(self.buy_list)
		return [checklist[value] for value in checklist]

	def add(self, quantity, price):
		request_id = self.last_request_id
		self.buy_list[request_id] = self.request_list(quantity, price)
		actual = self.get(self.last_request_id)
		expected = self.request_list(quantity, price)
		self.last_request_id += 1
		return request_id, actual, expected