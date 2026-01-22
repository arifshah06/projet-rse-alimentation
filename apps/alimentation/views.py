from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models

from .models import FoodEntry, FoodEmissionFactor
from .forms import FoodEntryForm


@login_required
def foodentry_create(request):
    factors = {f.code: f.kg_co2_per_meal for f in FoodEmissionFactor.objects.all()}
    if request.method == "POST":
        form = FoodEntryForm(request.POST, user=request.user)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect("alimentation:list")
    else:
        form = FoodEntryForm(user=request.user)

    return render(
        request,
        "alimentation/foodentry_form.html",
        {"form": form, "factors": factors},
    )

@login_required
def foodentry_list(request):
    entries = FoodEntry.objects.filter(user=request.user).order_by("-year", "-created_at")

    total_co2 = sum(e.total_co2_kg or 0 for e in entries)
    count = entries.count()

    context = {
        "entries": entries,
        "total_co2": total_co2,
        "count": count,
    }
    return render(request, "alimentation/list.html", context)
