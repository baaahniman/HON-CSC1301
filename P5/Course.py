class Course:

	# constructor
	def __init__(self,cn,ct,cr):
		self._cno = cn
		self._ctitle = ct
		self._credits = cr

	# getter
	def get_cno(self):
		return self._cno
	# getter
	def	get_ctitle(self):
		return self._ctitle

	# getter
	def get_credits(self):
		return self._credits

	def set_cno(self,cn):
		self.cno = cn

	# setter
	def set_ctitle(self,ct):
		self.ctitle = ct

	# setter
	def set_credits(self,cr):
		self._credits = cr

	# return string representation of course object
	def __str__(self):
		return self._cno + ':' + self._ctitle + ':' + str(self._credits)
        
