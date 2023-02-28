from collections import namedtuple

# sale
class sale():
	request_list = namedtuple('list', 'Quantity Price')

	def __init__(self):
		self.sale_list = {}
		self.last_request_id = 0

	def get(self, request_id):
		return self.sale_list.get(int(request_id), 'Заявок с таким id нет')

	def delete(self, request_id):
		del self.sale_list[int(request_id)]

	def view(self):
		view_list = [self.sale_list[i] for i in self.sale_list]
		return view_list

	def add(self, quantity, price):
		request_id = self.last_request_id
		self.sale_list[request_id] = self.request_list(quantity, price)
		actual = self.get(self.last_request_id)
		expected = self.request_list(quantity, price)
		self.last_request_id += 1
		return request_id, actual, expected

# buy
class buy():
	request_list = namedtuple('list', 'Quantity Price')

	def __init__(self):
		self.buy_list = {}
		self.last_request_id = 0

	def get(self, request_id):
		return self.buy_list.get(int(request_id))

	def delete(self, request_id):
		return self.buy_list.pop(int(request_id))

	def view(self):
		view_list = [self.buy_list[i] for i in self.buy_list]
		return view_list

	def add(self, quantity, price):
		request_id = self.last_request_id
		self.buy_list[request_id] = self.request_list(quantity, price)
		actual = self.get(self.last_request_id)
		expected = self.request_list(quantity, price)
		self.last_request_id += 1
		return request_id, actual, expected