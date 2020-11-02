import logging

import azure.functions as func
import typing


def main(req: func.HttpRequest,  technicianmsg: func.Out[typing.List[str]],  analystmsg: func.Out[typing.List[str]]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request. \nPayload: {}'.format(req.get_json()))

    to_user = req.get_json().get('to')
    from_user = req.get_json().get('from')
    msg = req.get_json().get('msg')

    if to_user == "analyst":
        analystmsg.set(msg)
        return func.HttpResponse("Messaged routed successfully.", status_code=200)
    elif to_user == "technician" : 
        technicianmsg.set(msg)
        return func.HttpResponse("Messaged routed successfully.", status_code=200)
    else:
        return func.HttpResponse("Unable to deliver message due to invalid address: {}.".format(to_user), status_code=401)
