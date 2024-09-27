from modeltranslation.translator import TranslationOptions, register

from .models import News, Category, Sud, Jurnalistik, Yangilik_sub


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content',)


@register(Sud)
class SudTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content',)


@register(Jurnalistik)
class JurnalistikTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content',)


@register(Yangilik_sub)
class Yangilik_subTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content',)