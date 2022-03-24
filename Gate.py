class Gate:
	def	__init__(self, name, ymax, ymin, n, k):
		self.name = name
		self.ymax = ymax
		self.ymin = ymin
		self.n = n
		self.k = k

	def stretch(self, x):
		if (x > 1.5):
			raise ValueError("x can be at-most 1.5")

		self.ymax = self.ymax * x
		self.ymin = self.ymin / x

	def increase_slope(self, x):
		if (x > 1.05):
			raise ValueError("x can be at-most 1.05")

		self.n = self.n * x

	def decrease_slope(self, x):
		if (x > 1.05):
			raise ValueError("x can be at-most 1.05")

		self.n = self.n / x

	def stronger_prom(self, x):
		self.ymax = self.ymax * x
		self.ymin = self.ymin * x

	def weaker_prom(self, x):
		self.ymax = self.ymax / x
		self.ymin = self.ymin / x

	def strong_RBS(self, x):
		self.k = self.k / x

	def weaker_RBS(self, x):
		self.k = self.k * x




