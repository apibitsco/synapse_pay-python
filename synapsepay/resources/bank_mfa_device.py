from ..apibits import *
from .. import Client
from . import *

class BankMfaDevice(APIResource):

    def answer(self, bank, mfa, params={}, headers={}):
        params = ParamsBuilder.merge({
            "bank" : bank,
            "mfa" : mfa,
        }, params)
        params = ParamsBuilder.merge({
            "access_token" : self.access_token,
        }, params)
        method = APIMethod("post", "/bank/mfa", params, headers, self)
        json = self.client.execute(method)
        return APIList(Bank, json['banks'], method, self.client)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(BankMfaDevice, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "bank_mfa_device")

    _api_attributes = {
        "form_extra" : {},
        "mfa" : {},
        "type" : {},
        "access_token" : {},
        "cookies" : {},
    }
