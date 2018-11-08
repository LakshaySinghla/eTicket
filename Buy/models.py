from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=50)
	emailId = models.CharField(max_length=50,unique=True)
	password = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Stadium(models.Model):
	name = models.CharField(max_length=256)
	location = models.CharField(max_length=256)
	typeATotal = models.IntegerField(default=0)
	typeBTotal = models.IntegerField(default=0)
	typeCTotal = models.IntegerField(default=0)
	typeAPrice = models.IntegerField(default=0)
	typeBPrice = models.IntegerField(default=0)
	typeCPrice = models.IntegerField(default=0)
	def __str__(self):
		return self.name
	
class RemainingTickets(models.Model):
	stadiumId = models.ForeignKey(Stadium, on_delete=models.CASCADE)
	typeARemaining = models.IntegerField(default=0)
	typeBRemaining = models.IntegerField(default=0)
	typeCRemaining = models.IntegerField(default=0)
	
	def initialise(self, stadium):
		self.stadiumId = stadium
		self.typeARemaining = stadium.typeATotal 
		self.typeBRemaining = stadium.typeBTotal
		self.typeCRemaining = stadium.typeCTotal
	
	def __str__(self):
		return self.stadiumId.name

class Match(models.Model):
	name = models.CharField(max_length=256,default='match')
	teamA = models.CharField(max_length=256)
	teamB = models.CharField(max_length=256)
	stadiumId = models.ForeignKey(Stadium,on_delete=models.CASCADE)
	date = models.DateTimeField('match_date')
	def __str__(self):
		return self.teamA+' vs '+self.teamB

class Ticket(models.Model):
	ticketType = models.CharField(max_length=10)
	price = models.IntegerField(default=0)
	emailId = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
	matchId = models.ForeignKey(Match, on_delete=models.CASCADE, default=0)
	def __str__(self):
		return self.ticketType.name