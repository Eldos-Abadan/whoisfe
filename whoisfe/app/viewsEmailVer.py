from django.shortcuts import render

def EmailVerView(request):
    return render(request, "email_verification/email_verification.html")