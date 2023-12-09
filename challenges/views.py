from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Run for 20 min every day",
    "march": "Learn Django for at least 20 min every day",
    "april": "Eat no meat for the entire month",
    "may": "Run for 20 min every day",
    "june": "Learn Django for at least 20 min every day",
    "july": "Eat no meat for the entire month",
    "august": "Run for 20 min every day",
    "september": "Learn Django for at least 20 min every day",
    "october": "Eat no meat for the entire month",
    "november": "Run for 20 min every day",
    "december": "Learn Django for at least 20 min every day"
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{
            capitalized_month}</a></li>"
    return HttpResponse(list_items)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,'month':month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
