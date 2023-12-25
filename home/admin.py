from django.contrib import admin

from home.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated_at')
    search_fields = ('slug', 'body')
    list_filter = ('updated_at',)
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user',)


admin.site.register(Post, PostAdmin)
