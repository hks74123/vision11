from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from rest_framework.views import APIView
from .repository import UserValidation, admin_user_roles


class CheckForUsername(APIView):
    '''
        View Function inherites APIView from
        rest_framework accepts post request
        and returns the status of availability
        of username with message.
    '''

    def post(self, request, *args):
        return UserValidation().validate_username(request.data)


class CheckForEmail(APIView):
    '''
        View Function inherites APIView from
        rest_framework accepts post request
        and returns the status of availability
        of email with message.
    '''

    def post(self, request, *args):
        return UserValidation().validate_email(request.data)



def AgeVerificationUploadDocument(request):
    '''
        View for handle of uploading the
        age verification document needs a
        files containing information related
        to age, user should be authorised.
    '''
    if request.user.is_authenticated:
        return UserValidation().upload_age_verification_document(request.FILES,request.user)
    return HttpResponseBadRequest()



def accept_age_verification_request(request,pid):
    try:
        if request.user.is_authenticated and request.user.is_staff:
            return admin_user_roles().accept_age_verification_request(pid)
        return redirect('/')
    except:
        return redirect('/')


def deny_age_verification_request(request,pid):
    try:
        if request.user.is_authenticated and request.user.is_staff:
            return admin_user_roles().deny_age_verification_request(pid)
        return redirect('/')
    except:
        return redirect('/')