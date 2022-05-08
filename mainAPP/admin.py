from django.contrib import admin

# Register your models here.

from .models import Match,Team,PlayersMatchData, User_Feature_Suggestion,Player,UserTeam


admin.site.register(Match)
admin.site.register(Team)
admin.site.register(PlayersMatchData)

admin.site.register(User_Feature_Suggestion)
admin.site.register(Player)
admin.site.register(UserTeam)