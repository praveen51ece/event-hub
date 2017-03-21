# for login purpose
import json
import logging
import traceback
import logging
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login,
								 logout as auth_logout, get_user_model, update_session_auth_hash)
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth.forms import AuthenticationForm
from django.template.response import TemplateResponse
from django.template import RequestContext
# from django.contrib.auth import authenticate
from django.http import *
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import check_password
from django.template import loader
from django.template import RequestContext
from models import Events,User

logger= logging.getLogger(__name__)




# @sensitive_post_parameters()
@csrf_exempt
@never_cache
def login(request,
		  redirect_field_name=REDIRECT_FIELD_NAME,
		  authentication_form=AuthenticationForm,
		  current_app=None, extra_context=None):
	"""
	Displays the login form and handles the login action.
	"""
	result = {}
	result['status'] = ''
	result['message']=""
	context = {}
	# redirect_to = request.GET.get(redirect_field_name,
	# 							   request.GET.get(redirect_field_name, ''))
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = check_authenticate(username=username, password=password)
		if user is not None:            
			if isinstance(user,User):
				result['status'] = 'success'
				# return HttpResponseRedirect('/event_insert/')
			else:
				pass
		else:
			result['status'] = 'error'
			result['message'] = "User name or password is incorrect"    
	return HttpResponse(json.dumps(result),content_type="application/json" )


def check_authenticate(username=None, password=None):
	try:
		# Try to find a user matching your username
		print 'inside authenticate'
		user = User.objects.get(use_login_id=username, use_isused=0)

		#  Check the password is the reverse of the username
		if check_password(password, user.use_pwd):
		#     # Yes? return the Django user object
			return user
		else:
		#     # No? return None - triggers default login
			print 'password does not match'
			raise User.DoesNotExist
	except Exception, e:
		print 'User not found in guest', e
        return None