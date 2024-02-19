from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
from ai_tool.services.home import HomeService

class HomeController(viewsets.ModelViewSet):
 
    def __init__(self):
        self.service = HomeService()
    
    def home(self, request):
        try:
            # input_data = request.data
            data = {"data": "data"}
            data = ["abc"]
            prompt = "what is resume"
            result = self.service.home(data)
            print(result)
            print(request.body)
           
            # print(data)
            return JsonResponse({"result":result}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400) 
    
    # #method to send prompt and JD to service file
    # def job_description(self, request):
    #     try:
    #         # input_data = request.data
    #         data = {"data": "data"}
    #         data = ["abc"]
    #         prompt = "what is resume"
    #         result = self.service.invoke_gpt(data)
    #         print(result)
    #         print(request.body)
           
    #         # print(data)
    #         return JsonResponse({"result":result}, status=201)
    #     except Exception as e:
    #         return JsonResponse({"error": str(e)}, status=400)