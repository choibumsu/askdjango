from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at']

    actions = ['make_published', 'make_draft', 'make_withdrawn']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = "글자수"

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Published상태로 변경합니다.'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft상태로 변경'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 Draft상태로 변경합니다.'

    def make_withdrawn(self, request, queryset):
        updated_count = queryset.update(status='w')
        self.message_user(request, '{}건의 포스팅을 Withdrawn상태로 변경'.format(updated_count))
    make_withdrawn.short_description = '지정 포스팅을 Withdrawn상태로 변경합니다.'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['message', 'author']
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']