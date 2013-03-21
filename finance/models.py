#-*-coding:utf-8-*-

from django.db import models

import datetime
today = datetime.datetime.now()
 
from utils.slugify import slugify
 
from django.contrib.humanize.templatetags.humanize import intcomma

 
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"범주")
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, verbose_name=u"메모")
 
    class Meta:
        ordering = ["pk"]
        verbose_name = u'범주'
        verbose_name_plural = u'범주'
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
 
    def __unicode__(self):
        return self.title
    
    def sum_category_budget(self):
        return intcomma(sum(Budget.objects.filter(category__title=self.title).values_list("money",flat=True)))
    
    def sum_category(self):
        temp_in = sum(Income.objects.filter(date__year=today.year, item__category__title=self.title).values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(date__year=today.year, item__category__title=self.title).values_list("money",flat=True))
        temp = temp_in  + temp_out 
        return intcomma(temp)
 
class Item(models.Model):
    item_number = models.CharField(u"항목번호", max_length=3)
    category = models.ForeignKey(Category, verbose_name=u"범주")
    title = models.CharField(max_length=50, verbose_name=u"항목명")
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, verbose_name=u'메모')
 
    class Meta:
        ordering = ["item_number"]
        verbose_name = u'항목'
        verbose_name_plural = u'항목'
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Item, self).save(*args, **kwargs)        
 
    def __unicode__(self):
        return "%s - %s" % (self.category.title, self.title)
    
    def budget(self):
        sum_list = Budget.objects.filter(item__item_number=self.item_number).values_list("money", flat=True)
        return intcomma(sum(sum_list))
    
    def january(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="1").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="1").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp)    
    
    def febrary(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="2").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="2").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp) 

    def march(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="3").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="3").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp) 

    def april(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="4").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="4").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp)  
    
    def may(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="5").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="5").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp) 
    
    def june(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="6").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="6").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp) 
    
    def july(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="7").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="7").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp)     
    
    def august(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="8").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="8").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp)     
    
    def september(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="9").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="9").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp)     
    
    def october(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="10").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="10").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp)     
    
    def november(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="11").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="11").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp)     
    
    def december(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="12").values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year, date__month="12").values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp)
    
    def year(self):
        temp_in = sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year).values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year).values_list("money",flat=True))
        temp = temp_in + temp_out
        return intcomma(temp)
    
#    def rate(self):
#        temp_in = float(sum(Income.objects.filter(item__item_number=self.item_number, date__year=today.year).values_list("money",flat=True))) / float(sum(Budget.objects.filter(item__item_number=self.item_number).values_list("money", flat=True)))
#        temp_out = float(sum(Outcome.objects.filter(item__item_number=self.item_number, date__year=today.year).values_list("money",flat=True))) / float(sum(Budget.objects.filter(item__item_number=self.item_number).values_list("money", flat=True)))
#        temp = temp_in * 100 + temp_out * 100
#        return "%10.2f %%" % temp
    
    def total(self):
        temp_in = sum(Income.objects.filter(date__year=today.year, date__month=today.month).values_list("money",flat=True))
        temp_out = sum(Outcome.objects.filter(date__year=today.year, date__month=today.month).values_list("money",flat=True))
        temp = temp_in  + temp_out 
        return sum(temp)
    
 
class Member(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"이름")
    birthday = models.DateField(verbose_name=u"생일", blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name=u"전화번호", help_text=u"'-'기호 빼고 입력", blank=True)
    email = models.EmailField(verbose_name=u"이메일", blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name=u"주소", blank=True)
    homepage = models.URLField(blank=True, verbose_name=u'홈페이지')
    family = models.ManyToManyField("self", blank=True, null=True, verbose_name=u'가족')
    comment = models.TextField(blank=True, verbose_name=u'비고')
 
    class Meta:
        ordering = ['pk']
        verbose_name = u'회원'
        verbose_name_plural = u'회원'
 
    def __unicode__(self):
        return self.name
    
    def family_list(self):
        return (",").join(self.family.all().values_list("name", flat=True))
 
class Budget(models.Model):
    fiscal_year = models.DateField(verbose_name=u"회계연도", auto_now=True)
    category = models.ForeignKey(Category, verbose_name=u"범주")
    item = models.ForeignKey(Item, verbose_name=u"항목")
    money = models.IntegerField(verbose_name=u"금액")
    delta = models.DecimalField(verbose_name=u'전년결산대비(%)', max_digits=100, decimal_places=2)
    comment = models.TextField(blank=True, verbose_name=u'비고')
 
    class Meta:
        ordering = ['fiscal_year', 'item__item_number']
        verbose_name = u"예산"
        verbose_name_plural = u"예산"
 
    def __unicode__(self):
        return self.category.title
    
    
class Income(models.Model):
    date = models.DateField(verbose_name=u"날짜")
    item = models.ForeignKey(Item, verbose_name=u"항목")
    member = models.ForeignKey(Member, verbose_name=u"이름", blank=True, null=True)
    money = models.IntegerField(verbose_name=u"금액")
    comment = models.TextField(blank=True, verbose_name=u"비고")
    week = models.IntegerField(blank=True, verbose_name=u"주차", editable=False)
 
    class Meta:
        ordering = ["-date", "item"]
        verbose_name = u"수입"
        verbose_name_plural = u"수입"
 
    def __unicode__(self):
        return u"%s" % self.item.title
 
    def save(self, *args, **kwargs):
        if not self.week:
            self.week = self.date.isocalendar()[1]
            return super(Income, self).save(*args, **kwargs)
 
 
class Outcome(models.Model):
    date = models.DateField(verbose_name=u'날짜')
    item = models.ForeignKey(Item, verbose_name=u'항목')
    executor = models.CharField(max_length=10, verbose_name=u'집행책임자', default=u"담임목사")
    money = models.IntegerField(verbose_name=u"금액")
    comment = models.TextField(blank=True, verbose_name=u"비고")
    week = models.IntegerField(blank=True, verbose_name=u"주차", editable=False)
 
    class Meta:
        ordering = ["-date", "item"]
        verbose_name = u"지출"
        verbose_name_plural = u"지출"
 
    def __unicode__(self):
        return u"%s" % (self.item.title)
 
    def save(self, *args, **kwargs):
        if not self.week:
            self.week = self.date.isocalendar()[1]
            return super(Outcome, self).save(*args, **kwargs)

        