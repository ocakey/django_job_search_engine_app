from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import job_data, user_history
from .forms import JobForm
from .algorithm import job_search
from .history import recent_search, existing_search
from .time_interval import time_changed
from .geojson_create import data2geojson
from .database_connection import mapbox
import datetime

job_title_clean = ''
special_clean = ''
location_clean = ''
date_posted_clean = ''
submit_start = False
submit_active = False


# Create your views here.

class JobListView(ListView):
    template_name = 'search/data_list.html'
    queryset = job_data.objects.all()


def JobSearchView(request):
    # global job_title_clean
    # global special_clean
    # global location_clean
    # global date_posted_clean
    # global submit_start
    # global submit_active
    page = ''
    total_page_num = ''
    p = ''
    per_page_results = ''
    total_page_num = ''

    # submitbutton = request.POST.get("submit")
    # if submitbutton == 'Submit':
    #     submit_active = True
    #     submit_start = True
    #
    # # form = JobForm(request.POST or None)
    # form = JobForm(request.POST or None)
    #
    # if form.is_valid():
    #     job_title_clean = form.cleaned_data.get("job_title")
    #     special_clean = form.cleaned_data.get("job_special")
    #     location_clean = form.cleaned_data.get("location")
    #     date_posted_clean = form.cleaned_data.get("date_posted")
    #
    #     if job_title_clean == "" and special_clean == "" and location_clean == "":
    #         end_asd = ''
    #     else:
    #         recent_search(job_title_clean, special_clean, location_clean, request.META.get('REMOTE_ADDR'),
    #                       request.META['HTTP_USER_AGENT'])
    #
    # history_results = existing_search(request.META.get('REMOTE_ADDR'), request.META['HTTP_USER_AGENT'])
    # search_history = user_history.objects.filter(pk__in=history_results).order_by('-exp_date')[:3]
    #
    # form = JobForm(initial={'job_title': job_title_clean, 'job_special': special_clean, 'location': location_clean})
    #
    # results = job_search(job_title_clean, special_clean, location_clean, date_posted_clean)
    # data2geojson(results)
    #
    # time = time_changed(results)
    #
    # # job_keyword = job_data.objects.filter(job_title__icontains=job_title_clean)
    # if results != "loc_not_ph" and results != "":
    #     job_recommend = job_data.objects.filter(pk__in=results)
    #     p = Paginator(job_recommend, 30)
    #
    #     # print(job_recommend)
    #
    #     # print('NUMBER OF PAGES')
    #     # print(p.num_pages)
    #     total_page_num = p.num_pages
    #
    #     page_num = request.GET.get('page', 1)
    #     # print(page_num)
    #
    #     submit_request = form.has_changed()
    #
    #     if submit_start is True:
    #         try:
    #             page = p.page(page_num)
    #             submitbutton = "Submit"
    #             # submit_start = False
    #         except EmptyPage:
    #             page = p.page(1)
    #     else:
    #         page = p.page(1)
    #
    #     if submit_active is True:
    #         page = p.page(1)
    #         submit_active = False
    #     per_page_results = len(page.object_list)
    #
    #
    # elif results == "loc_not_ph":
    #     job_recommend = "loc_not_ph"
    # else:
    #     job_recommend = ""
    #
    # mapbox_access_token = mapbox
    #
    # context = {'form': form, 'job_title': job_title_clean, 'location': location_clean, 'job_special': special_clean,
    #            'submitbutton': submitbutton, 'job_recommend': job_recommend, 'page': page, 'p': p,
    #            'per_page_results': per_page_results, 'total_page_num': total_page_num, 'search_history': search_history, 'submit_start': submit_start,
    #            'time_results': time, 'mapbox_access_token': mapbox_access_token}
    # # print(special_clean)
    #
    # # print(results)
    # return render(request, 'search/data_search.html', context)


def MainPageSearch(request):
    global job_title_clean
    global special_clean
    global location_clean
    global date_posted_clean
    global submit_start
    global submit_active
    page = ''
    total_page_num = ''
    p = ''
    per_page_results = ''
    total_page_num = ''

    submitbutton = request.POST.get("submit")
    if submitbutton == 'Submit':
        submit_active = True
        submit_start = True

    # form = JobForm(request.POST or None)
    form = JobForm(request.POST or None)

    if form.is_valid():
        job_title_clean = form.cleaned_data.get("job_title")
        special_clean = form.cleaned_data.get("job_special")
        location_clean = form.cleaned_data.get("location")
        date_posted_clean = form.cleaned_data.get("date_posted")

        if job_title_clean == "" and special_clean == "" and location_clean == "":
            end_asd = ''
        else:
            recent_search(job_title_clean, special_clean, location_clean, request.META.get('REMOTE_ADDR'),
                          request.META['HTTP_USER_AGENT'])

    history_results = existing_search(request.META.get('REMOTE_ADDR'), request.META['HTTP_USER_AGENT'])
    search_history = user_history.objects.filter(pk__in=history_results).order_by('-exp_date')[:3]

    form = JobForm(initial={'job_title': job_title_clean, 'job_special': special_clean, 'location': location_clean})

    results = job_search(job_title_clean, special_clean, location_clean, date_posted_clean)
    data2geojson(results)

    time = time_changed(results)

    # job_keyword = job_data.objects.filter(job_title__icontains=job_title_clean)
    if results != "loc_not_ph" and results != "":
        job_recommend = job_data.objects.filter(pk__in=results)
        p = Paginator(job_recommend, 30)

        # print(job_recommend)

        # print('NUMBER OF PAGES')
        # print(p.num_pages)
        total_page_num = p.num_pages

        page_num = request.GET.get('page', 1)
        # print(page_num)

        submit_request = form.has_changed()

        if submit_start is True:
            try:
                page = p.page(page_num)
                submitbutton = "Submit"
                # submit_start = False
            except EmptyPage:
                page = p.page(1)
        else:
            page = p.page(1)

        if submit_active is True:
            page = p.page(1)
            submit_active = False
        per_page_results = len(page.object_list)


    elif results == "loc_not_ph":
        job_recommend = "loc_not_ph"
    else:
        job_recommend = ""

    mapbox_access_token = mapbox
    print(date_posted_clean)

    context = {'form': form, 'job_title': job_title_clean, 'location': location_clean, 'job_special': special_clean, 'date_posted': date_posted_clean,
               'submitbutton': submitbutton, 'job_recommend': job_recommend, 'page': page, 'p': p,
               'per_page_results': per_page_results, 'total_page_num': total_page_num, 'search_history': search_history,
               'submit_start': submit_start,
               'time_results': time, 'mapbox_access_token': mapbox_access_token}
    # print(special_clean)

    # print(results)
    return render(request, 'search/index.html', context)


def PrivacyPolicyView(request):
    context = {}
    return render(request, 'search/privacy.html', context)


def TermsOfService(request):
    context = {}
    return render(request, 'search/terms.html', context)

def read_file(request):
    f = open('data.geojson', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="application/json")
