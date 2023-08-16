# Payment system
from fastapi import FastAPI

app = FastAPI(docs_url='/')

# import all components
from api.convert import convert_api
from api.profile import profile_api
from api.transfers import transfer_api


