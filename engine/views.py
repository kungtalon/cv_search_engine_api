from django.shortcuts import render
from rest_framework.views import APIView
from engine.apps import ApiConfig
from rest_framework.response import Response

class Ranking(APIView):
    def post(self, request):
        #data = request.data
        query = request.GET.get('query')
        notitle = request.GET.get('notitle')
        noabstract = request.GET.get('noabstract')
        nosubsections = request.GET.get('nosubsections')
        conference = request.GET.get('conference')
        start_year = request.GET.get('start_year')
        end_year = request.GET.get('end_year')
        lgbm = ApiConfig.model
        #predict using independent variables
        custom_args = {
            'search_title': False if notitle else True,
            'search_abstract': False if noabstract else True,
            'search_subsections': False if nosubsections else True,
            'conference': conference if conference else None,
            'start_year': int(start_year) if start_year else 0,
            'end_year': int(end_year) if end_year else 9999,
        }
        retrieved = lgbm.search(query, custom_args)
        return Response(data=retrieved, status=200)