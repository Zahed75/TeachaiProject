from django.contrib import admin
from .models import Blog, SiteUtilities, Subscribers, AboutMe, ImageSlider, TypesOfTea, Black_tea, White_tea, Green_tea, Fermented_tea, Herbal_tea, Oolong_tea, Matcha_tea, HeaderAndFooter
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'published_date')
    icon_name = 'mode_edit'

@admin.register(SiteUtilities)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_us_avatar')
    icon_name = 'settings_input_composite'

@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('id','subs_mail', 'subs_first_name')
    icon_name = 'subscriptions'

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_me_avatar')
    icon_name = 'person'

@admin.register(ImageSlider)
class ImageSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'slider_img', 'active')
    icon_name = 'image'

@admin.register(TypesOfTea)
class TypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'first_section', 'second_section')
    icon_name = 'view_column'

@admin.register(Black_tea)
class BlackTeaAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'date')
    icon_name = 'local_cafe'

@admin.register(White_tea)
class WhiteTeaAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'date')
    icon_name = 'local_cafe'

@admin.register(Green_tea)
class GreenTeaAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'date')
    icon_name = 'local_cafe'

@admin.register(Matcha_tea)
class MatchaTeaAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'date')

@admin.register(Herbal_tea)
class HerbalTeaAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'date')
    icon_name = 'local_cafe'

@admin.register(Oolong_tea)
class OolongTeaAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'date')
    icon_name = 'local_cafe'

@admin.register(Fermented_tea)
class FermentedTeaAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'date')
    icon_name = 'local_cafe'

@admin.register(HeaderAndFooter)
class HeaderFooterAdmin(admin.ModelAdmin):
    list_display = ('id',)
    icon_name = 'attach_file'