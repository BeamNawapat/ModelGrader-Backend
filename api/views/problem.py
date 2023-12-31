# from ..utility import JSONParser, JSONParserOne, passwordEncryption
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.sandbox.grader import PythonGrader
from ..constant import GET,POST,PUT,DELETE
from ..models import Account, Problem,Testcase
from rest_framework import status
from django.forms.models import model_to_dict
from ..serializers import *

from ..controllers.problem.create_problem import *
from ..controllers.problem.update_problem import *
from ..controllers.problem.delete_problem import *
from ..controllers.problem.get_problem import *
from ..controllers.problem.get_all_problems import *
from ..controllers.problem.remove_bulk_problems import *
from ..controllers.problem.get_all_problems_by_account import *
from ..controllers.problem.validate_program import *
from ..controllers.problem.get_all_problem_with_best_submission import *
from ..controllers.problem.get_problem_in_topic_with_best_submission import *

# Create your views here.
@api_view([POST,GET])
def all_problems_creator_view(request,account_id):
    if  request.method == POST:
        return create_problem(account_id,request)
    if request.method == GET:
        return get_all_problems_by_account(account_id)

@api_view([GET,PUT,DELETE])
def one_problem_creator_view(problem_id:str,request):
    if request.method == GET:
        return get_problem(problem_id)
    elif request.method == PUT:
        return update_problem(problem_id,request)
    elif request.method == DELETE:
        return delete_problem(problem_id)

@api_view([GET,DELETE])
def all_problems_view(request):
    if request.method == GET:
        return get_all_problem_with_best_submission(request)
    elif request.method == DELETE:
        return remove_bulk_problems(request)
    
@api_view([GET,PUT,DELETE])
def one_problem_view(request,problem_id: int):
    if request.method == GET:
        return get_problem(problem_id)
    elif request.method == PUT:
        return update_problem(problem_id,request)
    elif request.method == DELETE:
        return delete_problem(problem_id)
    
@api_view([POST])
def validation_view(request):
    if request.method == POST:
        return validate_program(request)
    
@api_view([GET])
def problem_in_topic_account_view(request,account_id:str,topic_id:str,problem_id:str):
    if request.method == GET:
        return get_problem_in_topic_with_best_submission(account_id,topic_id,problem_id)