from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .serializers import (
    RegisterSerializer,
    ChangePasswordSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer,
    UserShowSerializer,
    UserProfileUpdateSerializer,
)
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
import uuid
from drf_yasg.utils import swagger_auto_schema

RESET_CODES = {}


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
                return Response(
                    {"old_password": "Eski parol noto'g'ri."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            update_session_auth_hash(request, self.object)

            return Response({"detail": "Parol muvaffaqiyatli yangilandi."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserShowSerializer

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileUpdateSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestView(APIView):
    permission_classes = []
    serializer_class = PasswordResetRequestSerializer

    @swagger_auto_schema(request_body=PasswordResetRequestSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"detail": "Bu email kayıtlı değil."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        code = str(uuid.uuid4()).split("-")[0]
        RESET_CODES[email] = code

        send_mail(
            subject="Şifre Sıfırlama Kodu",
            message=f"Şifre sıfırlama kodunuz: {code}",
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )
        return Response({"detail": "Kod gönderildi."}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(APIView):
    permission_classes = []
    serializer_class = PasswordResetConfirmSerializer

    @swagger_auto_schema(request_body=PasswordResetConfirmSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']
        new_password = serializer.validated_data['new_password']

        real_code = RESET_CODES.get(email)
        if real_code is None or real_code != code:
            return Response(
                {"detail": "Kod geçersiz veya süresi dolmuş."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"detail": "Kullanıcı bulunamadı."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(new_password)
        user.save()

        del RESET_CODES[email]

        return Response(
            {"detail": "Şifre başarıyla güncellendi."},
            status=status.HTTP_200_OK,
        )
