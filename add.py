import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    num1 = req.params.get('n1')
    num2 = req.params.get('n2')


    if num1:
        result = int(num1) + int(num2)
        
        return func.HttpResponse(f" {result}.  ")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )