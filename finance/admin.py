#-*-coding:utf-8-*-
from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma

from finance.models import Category, Item, Member, Budget, Income, Outcome

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title","description","sum_category_budget", "sum_category"]
    list_filter = ["title",]
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ["item_number", "category", "title", "budget", 
                    "january", "febrary", "march", "april", "may", "june", "july", "august", 
                    "september", "october", "november", "december", "year", ]
    list_filter = ("category", "title")
    
class BudgetAdmin(admin.ModelAdmin):
    list_display = ["year", "category", "item","formatted_money", "percent_delta", "comment"]
    list_filter = ("fiscal_year", "category__title")
    
    def year(self, obj):
        return obj.fiscal_year.year
    year.short_description = u"회계연도"
    def formatted_money(self, obj):
        return u"\u20a9 %s" %intcomma(obj.money)
    formatted_money.short_description = u"금액"
    def percent_delta(self, obj):
        return "%.2f %%" %(obj.delta)
    percent_delta.short_description = u"전년결산대비(%)"

class MemberAdmin(admin.ModelAdmin):
    list_display = ["pk","name","phone","birthday","email","homepage","address","family_list","comment"]

    
class IncomeAdmin(admin.ModelAdmin):
    list_display = ["date","week","item", "member","_money","comment"]
    list_filter = ["date","week","item","member"]
    def _money(self, obj):
        return intcomma(obj.money)

class OutcomeAdmin(admin.ModelAdmin):
    list_display = ["date","week", "item", "_money", "executor","comment"]
    list_filter = ["date","item","week"]
    def _money(self, obj):
        return intcomma(obj.money)
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Outcome, OutcomeAdmin)