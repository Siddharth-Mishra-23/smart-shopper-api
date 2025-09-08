# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .scraper import scrape_product_info
from asgiref.sync import async_to_sync

class ProductSearchAPIView(APIView):
    def get(self, request):
        product_name = request.query_params.get('name')
        
        if not product_name:
            return Response({'error': 'Product name parameter "name" is required.'}, status=400)
        
        try:
            # Use async_to_sync to call the asynchronous scraper from a synchronous context
            products_data = async_to_sync(scrape_product_info)(product_name)
            return Response(products_data, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=500)