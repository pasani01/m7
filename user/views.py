from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .serializers import RegisterSerializer, ChangePasswordSerializer, ResetPasswordSerializer
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
import random


code={

}

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
            # Generate a 6-digit code
            reset_code = str(random.randint(100000, 999999))
            # Store the code in the global code dict
            code[email] = reset_code
            # Send the code via email
            send_mail(
                'Reset Password Code',
                f'Sizning reset kodunuz: {reset_code}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return Response({"detail": f"{email} adresiga reset kod yuborildi."}, status=200)
        return Response(serializer.errors, status=400)
