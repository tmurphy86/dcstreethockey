from django.contrib import admin

from reversion.admin import VersionAdmin

from leagues.models import Player, Team, Roster, Season, League, Game, Stat, Ref

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Roster)
class RosterAdmin(admin.ModelAdmin):
    pass

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    pass

@admin.register(Ref)
class RefAdmin(admin.ModelAdmin):
    pass