# kunder
	# en adresse, et navn, et telefonnummer

# konti, har en saldo, et kontonummer, har en kunde
	# transaktion, et beloeb (+/-), en konto
	
# bank, har antal konti
	# overfoersel, to transaktioner


class Bank(object):
	"""docstring for Bank"""
	def __init__(self):
		pass

class Konto(object):
	"""docstring for Konto"""
	def __init__(self, nummer, kunde):
		self.saldo = 0
		self.nummer = nummer
		self.kunde = kunde
	
	def debit(self, amount):
		assert amount >= 0
		self.saldo -= amount

	def credit(self, amount):
		assert amount >= 0
		self.saldo += amount

class Kunde(object):
	"""docstring for Kunde"""
	def __init__(self, adresse, navn, telefonnummer):
		self.adresse = adresse
		self.navn = navn
		self.telefonnummer = telefonnummer
		self.fordel_niveau = 0

poul = Kunde('ligustervej', 'poul', '1234')
konto = Konto(101, poul)
print poul.navn
print konto.kunde.navn
print konto.saldo

konto.credit(100)
print konto.saldo


		
	


