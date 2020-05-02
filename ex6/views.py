from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from ex6.forms import user_id_form
from ex6.operations import recommendations


def welcome_view(request):
    # create a form instance and populate it with data from the request:
    input_form = user_id_form(request.POST or None)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
       if input_form.is_valid():
            # process the data in form.cleaned_data as required
            id = input_form.cleaned_data["user_id"]
            # redirect to a new URL:
            return redirect('/welcome/' + id)

    # if not post or not valid
    return render(request, "welcome.html", {'input_form': input_form})



def recommendation_view(request, id):
    # todo create/calc recommendations
    # If you are using DataFrames keep in mind that Django needs a dictionary as the context  variable. 
    # So use the to_dict() function to convert it.
    recommendation_dict = recommendations(id).to_dict()
    print(recommendation_dict)
    # Currently only a dataframe with UserID, MovieID and Rating is returned
    #   TODO: Enrich this data
    return render(request, "recommendations.html", recommendation_dict)
