# Headphone example
class Headphone():
	'''Class of Headphone'''
	def __init__(self, name, style, quality, imaging, sound_profile):
		'''Initialize Values'''
		self.name = name
		self.style = style	
		self.quality = quality
		self.imaging = imaging
		self.sound_profile = sound_profile  
    
# another example
Headphone01 = Headphone('sennheiser', 'open back headphone', 'medium quality build', 'excellent', ' v shape sound')
Headphone02 = Headphone('bose', 'close back headphone', 'premium quality build', ' average', 'neutral sound')
Headphone03 = Headphone('hifiman', 'in ear monitor', 'high quality build', 'normal', 'bassy sound')
Headphone04 = Headphone('focal', 'open back headphone', 'premium quality build', 'excellent imaging', 'm shape sound')

# more example
class Student():
	'''Class of Student'''
	def __init__(self, name, course, term, status, age):
		'''Initializa Values'''
		self.name = name
		self.course = course
		self.term = term
		self.status = status
		self.age = age
    
# more example
student03 = Student('levi', 'SPN 1102', 'summer semester', 'part time', '16')
student04 = Student('julianah', 'ENC 1101', 'fall semester', 'full time', '21')
student05 = TransferStudent('angelo', 'algebra 1', 'spring semester', 'full time', '27')

# more example
