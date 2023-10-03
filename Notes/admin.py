from django.contrib import admin
from Notes.models import signup
from Notes.models import notes
# Register your models here.

class userSignUp(admin.ModelAdmin):
    list_display = ('id','username','email','password','status')

admin.site.register(signup,userSignUp)


class userNotes(admin.ModelAdmin):
    list_display=('id','user_id','title','description')

admin.site.register(notes,userNotes)