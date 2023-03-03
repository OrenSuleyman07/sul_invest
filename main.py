from collections import namedtuple

# sorting function
def sorting(start_dictionary):
    dictionary = dict.copy(start_dictionary)
    keys = list(dictionary.keys())
    amount = 0
    for key_id in range(len(keys) - 1):
        key = keys[key_id]
        next_key = keys[key_id + 1]
        if dictionary[key][1] <= dictionary[next_key][1]:
        	amount += 1
        else:
            dictionary[key], dictionary[next_key] = dictionary[next_key], dictionary[key]
    return dictionary, len(keys) - 1, amount

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
		if len(self.sale_list) > 1:
			checklist, lenght, amount = sorting(self.sale_list)
			while lenght != amount:
				checklist, lenght, amount = sorting(checklist)
		else:
			checklist = self.sale_list
		return [checklist[value] for value in checklist]

	def add(self, quantity, price):
		if price == '':
			request_id = self.last_request_id
			self.sale_list[request_id] = self.request_list(quantity, None)
			actual = self.get(self.last_request_id)
			expected = self.request_list(quantity, None) # потом поменять обратно на quantity, price
			self.last_request_id += 1
		else:
			request_id = self.last_request_id
			self.sale_list[request_id] = self.request_list(quantity, price)
			actual = self.get(self.last_request_id)
			expected = self.request_list(quantity, price) # потом поменять обратно на quantity, price
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
		if len(self.buy_list) > 1:
			checklist, lenght, amount = sorting(self.buy_list)
			while lenght != amount:
				checklist, lenght, amount = sorting(checklist)
		else:
			checklist = self.buy_list
		return [checklist[value] for value in checklist]

	def add(self, quantity, price):
		if price == '':
			request_id = self.last_request_id
			self.buy_list[request_id] = self.request_list(quantity, None)
			actual = self.get(self.last_request_id)
			expected = self.request_list(quantity, None)
			self.last_request_id += 1
		else:
			request_id = self.last_request_id
			self.buy_list[request_id] = self.request_list(quantity, price)
			actual = self.get(self.last_request_id)
			expected = self.request_list(quantity, price)
			self.last_request_id += 1
		return request_id, actual, expected