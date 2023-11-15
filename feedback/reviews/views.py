from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
# from .models import Review

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank_you')


# def review(request):
#     if request.method == 'POST':
#        # existing_data = Review.objects.get(pk=1) # with model form method also we can update existing data like that
#         # form = ReviewForm(request.POST, instance=existing_data)
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save() # now we can just save it with modelform no need extra connect to any model because its already connected a model
#             return HttpResponseRedirect('/thank_you')
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
