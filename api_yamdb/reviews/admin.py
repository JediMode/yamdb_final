from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_genres',
        'category',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'

    def get_genres(self, obj_genre):
        all_genres = obj_genre.genre.values_list('name', flat=True)
        return [genre for genre in all_genres]


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'score',
        'pub_date',
        'author',
        'title'
    )
    search_fields = ('text', 'pub_date', 'author', 'score')
    list_filter = ('pub_date', 'score')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'review',
        'author',
        'text',
        'pub_date'
    )
    list_display_links = ('text',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
