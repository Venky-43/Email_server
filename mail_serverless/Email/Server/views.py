from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class Mail(APIView):
    def post(self, request):
        receiver_email = request.data.get("receiver_email")
        subject = request.data.get("subject")
        body_text = request.data.get("body_text")

        if not receiver_email or not subject or not body_text:
            return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            send_mail(subject, body_text, 'venkannababukothapalli716@gmail.com', [receiver_email])
            return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
