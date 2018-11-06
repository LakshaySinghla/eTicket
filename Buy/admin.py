from django.contrib import admin
from Buy.models import User, Stadium, Ticket, TicketType, RemainingTickets,Match
# Register your models here.
admin.site.register(User)
admin.site.register(Stadium)
admin.site.register(Ticket)
admin.site.register(TicketType)
admin.site.register(RemainingTickets)
admin.site.register(Match)
