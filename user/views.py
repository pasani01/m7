from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .serializers import RegisterSerializer, ChangePasswordSerializer, ResetPasswordSerializer
from rest_framework.views import APIView


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer



class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": "Eski parol noto'g'ri."}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            update_session_auth_hash(request, self.object)

            return Response({"detail": "Parol muvaffaqiyatli yangilandi."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            return Response({"detail": f"{email} adresiga reset link yuborildi (soxta)."}, status=200)
        return Response(serializer.errors, status=400)
