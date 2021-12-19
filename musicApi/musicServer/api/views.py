from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


@api_view()
@permission_classes([AllowAny])
def first(request):
    print(request.query_params)
    print(request.query_params['num'])
    number = request.query_params['num']
    new_number = int(number) * 2

    return Response({'message': 'we recieved your request', 'result' : new_number})