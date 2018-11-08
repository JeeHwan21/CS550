class Card:
	
	def __init__(self, rank, suit):

		suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

		if rank == 1:
			self.rank = "Ace"
		elif rank == 11:
			self.rank = "Jack"
		elif rank == 12:
			self.rank = "Queen"
		elif rank == 13:
			self.rank = "King"
		else:
			self.rank = str(rank)

		self.suit = suit

	def __str__(self):
		return self.rank + " of " + suit[1 + self.suit]


class Deck:

	def __init__(self):
		self.cards = []
		for i in (1, 13):
			for j in (1, 4):
		self.cards.append(Card(i, j))

