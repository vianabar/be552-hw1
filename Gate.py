class Gate:
	def	__init__(name, ymax, ymin, n, k):
		gate.name = name
		gate.ymax = ymax
		gate.ymin = ymin
		gate.n = n
		gate.k = k

	def stretch(x):
		if (x > 1.5):
			raise ValueError("x can be at-most 1.5")

		self.ymax = ymax * x
		self.ymin = ymin / x

	def increase_slope(x):
		if (x > 1.05):
			raise ValueError("x can be at-most 1.05")

		self.n = n * x

	def decrease_slope(x):
		if (x > 1.05):
			raise ValueError("x can be at-most 1.05")

		self.n = n / x

	def stronger_prom(x):
		self.ymax = ymax * x
		self.ymin = ymin * x

	def weaker_prom(x):
		self.ymax = ymax / x
		self.ymin = ymin / x

	def strong_RBS(x):
		self.k = k / x

	def weaker_RBS(x):
		self.k = k * x




