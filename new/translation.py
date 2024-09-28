from modeltranslation.translator import TranslationOptions, register
from .models import Category, News, Sud, Jurnalistik, Yangilik_sub


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content', 'time',)

@register(Sud)
class SudTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content', 'time',)

@register(Jurnalistik)
class JurnalistikTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content', 'time',)

@register(Yangilik_sub)
class Yangilik_subTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content', 'time',)
