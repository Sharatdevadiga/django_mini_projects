from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
# def january(request):
#     return HttpResponse("challenge for January : run 1km every day")

# def february(request):
#     return HttpResponse("challenge for February : read 1 book every week")

monthly_Challenges = {
    "january": "Run 1km every day",
    "february": "Read 1 book every week",
    "march": "Learn 1 new programming language",
    "april": "Practice 30 minutes of meditation daily",
    "may": "Write 1000 words every day",
    "june": "Exercise for 30 minutes daily",
    "july": "Cook a new recipe every week",
    "august": "Spend 1 hour on a hobby daily",
    "september": "Learn a new skill every week",
    "october": "Volunteer for a local charity",
    "november": "Save $100 every week",
    "december": "Reflect on the year and set goals for next year",
}

def index(request):
    try:
        months = list(monthly_Challenges.keys())

        # list_items = ""

        # for month in months:
        #     capitilized_month = month.capitalize()
        #     month_path = reverse("month-challenge", args=[month])
        #     list_items += f'<li><a href="{month_path}"><button>{capitilized_month}</button></a></li>'

        # response_data = f"""
        # <ul>s
        #     {list_items}
        # </ul>
        # """
        # return HttpResponse(response_data)

        return render(request, "challenges/index.html", {
            "months": months
        })
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return HttpResponseNotFound("something went wrong")


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_Challenges.keys())

        if month < 1 or month > len(months):
            return HttpResponseNotFound("This month is Invalid")

        forward_month = months[month - 1]
        path = reverse("challenges:month-challenge", args=[forward_month])
        return HttpResponseRedirect(path)
    except KeyError:
        return HttpResponseNotFound("This month is not supported yet")


def monthly_challenge(request, month):
    try:
        challengeText = monthly_Challenges[month.lower()]

        if not challengeText:
            return HttpResponseNotFound("This month is not supported yet")

        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponseNotFound(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challengeText,
            "month": month
        })


    except Exception as e:
        print(f"An error occurred: {e}")
        raise Http404("This month is not supported yet")