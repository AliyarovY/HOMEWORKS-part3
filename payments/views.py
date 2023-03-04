from requests import Response
from rest_framework.views import APIView

from .serializers import PaymentSerializer
from .services import yookassa_pay


class PaymentView(APIView):
    def post(self, request, *args, **kwargs):
        if yookassa_pay(request.data['amount']):
            serializer = PaymentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save
            Response(serializer.data)
        else:
            Response({'detail': 'bad'})
