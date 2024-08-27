from django.contrib import admin
from text_data.models import Text, Language, Translate


class TranslatesAdmin(admin.ModelAdmin):
    list_display = ("text_key", "language", "translate")
    list_display_links = ("translate",)
    raw_id_fields = ("text_key", "language")
    search_fields = ("Translate",)
    list_filter = ("language",)



class TranslatesInline(admin.StackedInline):
    model = Translate
    fields = ["text_key", "language", "translate"]
    show_change_link = True
    extra = 0


class TextAdmin(admin.ModelAdmin):
    list_display = ("key", "key_type")
    inlines = [TranslatesInline]
    list_filter = ("key_type",)
    fieldsets = (
        (None, {
            "fields": ("key", "key_type"),
            "description": "Лимит поста в Телеграме с фото и другими медиафайлами (Тип Caption) – 1024 символа.",
        }),
    )


admin.site.register(Language)
admin.site.register(Translate, TranslatesAdmin)
admin.site.register(Text, TextAdmin)