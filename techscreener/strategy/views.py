from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StrategySerializer
from .models import Strategy

class CreateView(APIView):
    def post(self, request):
        serializer = StrategySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response({ 'message': 'Creation successful!' })
        return response

class EditView(APIView):
    def post(self, request):
        name = request.data['name']
        strategy = Strategy.objects.filter(name=name)
        strategy.update(**request.data)
        updated_strategy = Strategy.objects.filter(name=name)
        strategy_serializer = StrategySerializer(updated_strategy, many=True)
        response = Response({ 'message': 'Edit successful!' })
        return response

class FetchView(APIView):
    def get(self, request):
        users = Strategy.objects.filter()
        serializer = StrategySerializer(users, many=True)
        return Response(serializer.data)