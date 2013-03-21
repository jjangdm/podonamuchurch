from django.shortcuts import render_to_response
from finance.models import Member, Income, Outcome, Budget, Category, Item
import datetime
today = datetime.datetime.now()

def index(self):
    return render_to_response("./index.html", dict(
                                                   today=today,
                                                   )
                              )



def report_member(self):
    member_list = Member.objects.all()
    return render_to_response("./report/member.html", dict(
                                                           today=today,
                                                           member_list=member_list, 
                                                                   )
                                  )
    

def report_income(self):
    income = Income.objects.filter(date__year=today.year).all()
    income_list = income.filter(date=today.date)
    tithe = income_list.filter(item__item_number="001")
    thanks = income_list.filter(item__item_number="002")
    thanks_special = income_list.filter(item__item_number="003")
    mission = income_list.filter(item__item_number="004")
    mission_special = income_list.filter(item__item_number="005")
    lordday = income_list.filter(item__item_number="006")
    etc = income_list.filter(item__item_number="007")
    sum_tithe_month = sum(income.filter(date__month=today.month, item__item_number="001").values_list("money",flat=True))
    sum_thanks_month = sum(income.filter(date__month=today.month, item__item_number="002").values_list("money",flat=True))
    sum_thanks_special_month = sum(income.filter(date__month=today.month, item__item_number="003").values_list("money",flat=True))
    sum_mission_month = sum(income.filter(date__month=today.month, item__item_number="004").values_list("money",flat=True))
    sum_mission_special_month = sum(income.filter(date__month=today.month, item__item_number="005").values_list("money",flat=True))
    sum_lordday_month = sum(income.filter(item__item_number="006").values_list("money",flat=True))
    sum_etc_month = sum(income.filter(item__item_number="007").values_list("money",flat=True))
    sum_tithe_year = sum(income.filter(item__item_number="001").values_list("money",flat=True))
    sum_thanks_year = sum(income.filter(item__item_number="002").values_list("money",flat=True))
    sum_thanks_special_year = sum(income.filter(item__item_number="003").values_list("money",flat=True))
    sum_mission_year = sum(income.filter(item__item_number="004").values_list("money",flat=True))
    sum_mission_special_year = sum(income.filter(item__item_number="005").values_list("money",flat=True))
    sum_lordday_year = sum(income.filter(item__item_number="006").values_list("money",flat=True))
    sum_etc_year = sum(income.filter(item__item_number="007").values_list("money",flat=True))
    sum_today = sum(income_list.values_list("money",flat=True))
    sum_tithe = sum(tithe.values_list("money", flat=True))
    sum_thanks = sum(thanks.values_list("money", flat=True))
    sum_thanks_special = sum(thanks_special.values_list("money", flat=True))
    sum_mission = sum(mission.values_list("money", flat=True))
    sum_mission_special = sum(mission_special.values_list("money", flat=True))
    sum_lordday = sum(lordday.values_list("money", flat=True))
    sum_etc = sum(etc.values_list("money", flat=True))
    budget_list = Budget.objects.filter(fiscal_year__year=today.year).values_list("money",flat=True)
    budget_tithe = sum(budget_list.filter(item__item_number="001"))
    budget_thanks = sum(budget_list.filter(item__item_number="002"))
    budget_thanks_special = sum(budget_list.filter(item__item_number="003"))
    budget_mission = sum(budget_list.filter(item__item_number="004"))
    budget_mission_special = sum(budget_list.filter(item__item_number="005"))
    budget_lordday = sum(budget_list.filter(item__item_number="006"))
    budget_etc = sum(budget_list.filter(item__item_number="007"))
    rate_tithe = sum_tithe_year / float(budget_tithe) *100
    rate_thanks = sum_thanks_year / float(budget_thanks) *100
    rate_thanks_special = sum_thanks_special_year / float(budget_thanks_special) *100
    rate_mission = sum_mission_year / float(budget_mission) *100
    rate_mission_special = sum_mission_special_year / float(budget_mission_special) *100
    rate_lordday = sum_lordday_year / float(budget_lordday) *100
    rate_etc = sum_etc_year / float(budget_etc) *100
    total_income_month = sum(Income.objects.filter(date__year=today.year, date__month=today.month).values_list("money",flat=True))
    total_income = sum(Income.objects.filter(date__year=today.year).values_list("money",flat=True))
    rate_total = float(total_income) / float(sum(Budget.objects.filter(fiscal_year__year=today.year, \
                                                                       item__item_number__startswith="0").values_list("money", flat=True))) * 100
    return render_to_response("./report/income.html", dict(
                                                           today=today,
                                                           tithe=tithe,
                                                           thanks=thanks,
                                                           thanks_special=thanks_special,
                                                           mission=mission,
                                                           mission_special=mission_special,
                                                           lordday=lordday,
                                                           etc=etc,
                                                           sum_tithe_month=sum_tithe_month,
                                                           sum_thanks_month=sum_thanks_month,
                                                           sum_thanks_special_month=sum_thanks_special_month,
                                                           sum_mission_month=sum_mission_month,
                                                           sum_mission_special_month=sum_mission_special_month,
                                                           sum_lordday_month=sum_lordday_month,
                                                           sum_etc_month=sum_etc_month,
                                                           sum_tithe_year=sum_tithe_year,
                                                           sum_thanks_year=sum_thanks_year,
                                                           sum_thanks_special_year=sum_thanks_special_year,
                                                           sum_mission_year=sum_mission_year,
                                                           sum_mission_special_year=sum_mission_special_year,
                                                           sum_lordday_year=sum_lordday_year,
                                                           sum_etc_year=sum_etc_year,
                                                           sum_today=sum_today,
                                                           sum_tithe=sum_tithe,
                                                           sum_thanks=sum_thanks,
                                                           sum_thanks_special=sum_thanks_special,
                                                           sum_mission=sum_mission,
                                                           sum_mission_special=sum_mission_special,
                                                           sum_lordday=sum_lordday,
                                                           sum_etc=sum_etc,
                                                           rate_tithe=rate_tithe,
                                                           rate_thanks=rate_thanks,
                                                           rate_thanks_special=rate_thanks_special,
                                                           rate_mission=rate_mission,
                                                           rate_mission_special=rate_mission_special,
                                                           rate_lordday=rate_lordday,
                                                           rate_etc=rate_etc,
                                                           total_income_month=total_income_month,
                                                           total_income=total_income,
                                                           rate_total=rate_total,
                                                    
                                                           )
                                 )
    
    
    
def report_budget(self):
    budget_list = Budget.objects.filter(fiscal_year__year=today.year).all()
    total_budget = sum(budget_list.values_list("money", flat=True))
    category_list = Category.sum_category
    return render_to_response("./report/budget.html", dict(
                                                           today=today,
                                                           budget_list=budget_list,
                                                           category_list=category_list,
                                                           total_budget=total_budget,
                                                           )
                              )

def report_total(self):
    item_list = Item.objects.all()
    #income
    income_list = item_list.filter(item_number__startswith="0")
    monthly_sum_income = []
    for month in range(1,13):
        temp = sum(Income.objects.filter(date__year=today.year, date__month="%s" %month).values_list("money",flat=True))
        monthly_sum_income.append(temp)
    total_income = sum(monthly_sum_income)
    total_budget_income = sum(Budget.objects.filter(fiscal_year__year=today.year, item__item_number__startswith="0").values_list("money",flat=True))
    rate_income = float(total_income)/float(total_budget_income) * 100
    #management
    management_list = item_list.filter(item_number__startswith="11")
    monthly_sum_management = []
    for month in range(1,13):
        temp = sum(Outcome.objects.filter(date__year=today.year, date__month="%s" %month, item__item_number__startswith="11").values_list("money",flat=True))
        monthly_sum_management.append(temp)
    total_management = sum(monthly_sum_management)
    total_budget_management = sum(Budget.objects.filter(fiscal_year__year=today.year, item__item_number__startswith="11").values_list("money",flat=True))
    rate_management = float(total_management)/float(total_budget_management) * 100
    #education
    education_list = item_list.filter(item_number__startswith="12")
    monthly_sum_education = []
    for month in range(1,13):
        temp = sum(Outcome.objects.filter(date__year=today.year, date__month="%s" %month, item__item_number__startswith="12").values_list("money",flat=True))
        monthly_sum_education.append(temp)
    total_education = sum(monthly_sum_education)
    total_budget_education = sum(Budget.objects.filter(fiscal_year__year=today.year, item__item_number__startswith="12").values_list("money",flat=True))
    rate_education = float(total_education)/float(total_budget_education) * 100
    #feed
    feed_list = item_list.filter(item_number__startswith="13")
    monthly_sum_feed = []
    for month in range(1,13):
        temp = sum(Outcome.objects.filter(date__year=today.year, date__month="%s" %month, item__item_number__startswith="13").values_list("money",flat=True))
        monthly_sum_feed.append(temp)
    total_feed = sum(monthly_sum_feed)
    total_budget_feed = sum(Budget.objects.filter(fiscal_year__year=today.year, item__item_number__startswith="13").values_list("money",flat=True))
    rate_feed = float(total_feed)/float(total_budget_feed) * 100
    #reward
    reward_list = item_list.filter(item_number__startswith="14")
    monthly_sum_reward = []
    for month in range(1,13):
        temp = sum(Outcome.objects.filter(date__year=today.year, date__month="%s" %month, item__item_number__startswith="14").values_list("money",flat=True))
        monthly_sum_reward.append(temp)
    total_reward = sum(monthly_sum_reward)
    total_budget_reward = sum(Budget.objects.filter(fiscal_year__year=today.year, item__item_number__startswith="14").values_list("money",flat=True))
    rate_reward = float(total_reward)/float(total_budget_reward) * 100
    #mission
    mission_list = item_list.filter(item_number__startswith="15")
    monthly_sum_mission = []
    for month in range(1,13):
        temp = sum(Outcome.objects.filter(date__year=today.year, date__month="%s" %month, item__item_number__startswith="15").values_list("money",flat=True))
        monthly_sum_mission.append(temp)
    total_mission = sum(monthly_sum_mission)
    total_budget_mission = sum(Budget.objects.filter(fiscal_year__year=today.year, item__item_number__startswith="15").values_list("money",flat=True))
    rate_mission = float(total_mission)/float(total_budget_mission) * 100
    #operation
    operation_list = item_list.filter(item_number__startswith="16")
    monthly_sum_operation = []
    for month in range(1,13):
        temp = sum(Outcome.objects.filter(date__year=today.year, date__month="%s" %month, item__item_number__startswith="16").values_list("money",flat=True))
        monthly_sum_operation.append(temp)
    total_operation = sum(monthly_sum_operation)
    total_budget_operation = sum(Budget.objects.filter(fiscal_year__year=today.year, item__item_number__startswith="16").values_list("money",flat=True))
    rate_operation = float(total_operation)/float(total_budget_operation) * 100
    #etc
    etc_list = item_list.filter(item_number__startswith="19")
    monthly_sum_etc = []
    for month in range(1,13):
        temp = sum(Outcome.objects.filter(date__year=today.year, date__month="%s" %month, item__item_number__startswith="19").values_list("money",flat=True))
        monthly_sum_etc.append(temp)
    total_etc = sum(monthly_sum_etc)
    total_budget_etc = sum(Budget.objects.filter(fiscal_year__year=today.year, item__item_number__startswith="19").values_list("money",flat=True))
#    rate_etc = float(total_etc)/float(total_budget_etc) * 100
    #outcome
    monthly_sum_outcome = []
    for month in range(1,13):
        temp = sum(Outcome.objects.filter(date__year=today.year, date__month="%s" %month, item__item_number__startswith="1").values_list("money",flat=True))
        monthly_sum_outcome.append(temp)
    total_outcome = sum(monthly_sum_outcome)
    total_budget_outcome = sum(Budget.objects.filter(fiscal_year__year=today.year, item__item_number__startswith="1").values_list("money",flat=True))
    total = total_income - total_outcome
    rate_outcome = float(total_outcome)/float(total_budget_outcome) * 100
    return render_to_response("./report/total.html", dict(
                                                          today=today,
                                                          #income
                                                          income_list=income_list,
                                                          monthly_sum_income=monthly_sum_income,
                                                          total_income=total_income,
                                                          total_budget_income=total_budget_income,
                                                          rate_income=rate_income,
                                                          #management
                                                          management_list=management_list,
                                                          monthly_sum_management=monthly_sum_management,
                                                          total_management=total_management,
                                                          total_budget_management=total_budget_management,
                                                          rate_management=rate_management,
                                                          #education
                                                          education_list=education_list,
                                                          monthly_sum_education=monthly_sum_education,
                                                          total_education=total_education,
                                                          total_budget_education=total_budget_education,
                                                          rate_education=rate_education,
                                                          #feed
                                                          feed_list=feed_list,
                                                          monthly_sum_feed=monthly_sum_feed,
                                                          total_feed=total_feed,
                                                          total_budget_feed=total_budget_feed,
                                                          rate_feed=rate_feed,
                                                          #reward
                                                          reward_list=reward_list,
                                                          monthly_sum_reward=monthly_sum_reward,
                                                          total_reward=total_reward,
                                                          total_budget_reward=total_budget_reward,
                                                          rate_reward=rate_reward,
                                                          #mission
                                                          mission_list=mission_list,
                                                          monthly_sum_mission=monthly_sum_mission,
                                                          total_mission=total_mission,
                                                          total_budget_mission=total_budget_mission,
                                                          rate_mission=rate_mission,
                                                          #operation
                                                          operation_list=operation_list,
                                                          monthly_sum_operation=monthly_sum_operation,
                                                          total_operation=total_operation,
                                                          total_budget_operation=total_budget_operation,
                                                          rate_operation=rate_operation,
                                                          #etc
                                                          etc_list=etc_list,
                                                          monthly_sum_etc=monthly_sum_etc,
                                                          total_etc=total_etc,
                                                          total_budget_etc=total_budget_etc,
#                                                          rate_etc=rate_etc,
                                                          #total
                                                          total_icome=total_income,
                                                          total_outcome=total_outcome,
                                                          total = total,
                                                          #totaly_month_outcome
                                                          monthly_sum_outcome=monthly_sum_outcome,
                                                          total_budget_outcome=total_budget_outcome,
                                                          rate_outcome=rate_outcome,
                                                          ))    
    
    
#pdf generating view
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def some_view(request):
    s = """The view layer Django has the concept of "view" to encapsulate the logic responsible bla bla..."""
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    p = canvas.Canvas(response)
    p.drawString(80,750,s)
    p.showPage()
    p.save()
    return response