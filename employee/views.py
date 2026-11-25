from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token

from employee.models import EmployeeDb
from employee.serializers import EmployeeSerializer, RegistrationSerializer

# Create your views here.
class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer_instance = RegistrationSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response({
                'message': 'Registration successful'
            })

        return Response(serializer_instance.errors)


class EmployeeListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        qs = EmployeeDb.objects.all()
        serializer_ins = EmployeeSerializer(qs, many=True)
        return Response(serializer_ins.data)


    def post(self, request):
        serializer_ins = EmployeeSerializer(data=request.data)
        if serializer_ins.is_valid():
            serializer_ins.save()
            return Response(serializer_ins.data)
             
        else:
            return Response(serializer_ins.errors)

    
class EmployeeRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        emp_obj = EmployeeDb.objects.get(id=id)
        serializer_ins = EmployeeSerializer(emp_obj)
        return Response(serializer_ins.data)


    def put(self, request, id):      
        emp_obj =get_object_or_404(EmployeeDb,id=id)
        serializer_ins = EmployeeSerializer(emp_obj, data=request.data)

        if serializer_ins.is_valid():
            serializer_ins.save()
            return Response(serializer_ins.data)
        return Response(serializer_ins.errors)


    def delete(self, request, id):       
        employee_obj = get_object_or_404(EmployeeDb,id=id)
        employee_obj.delete()

        return Response({
            'message': 'Employee deleted successfully'
        })