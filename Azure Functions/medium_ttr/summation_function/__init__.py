import logging
import azure.functions as func
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    num1 = req.params.get('first_number')
    if not num1:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            num1 = req_body.get('first_number')

    num2 = req.params.get('second_number')
    if not num2:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            num2 = req_body.get('second_number')

    sum = int(num1) + int(num2)

    if sum:
        return func.HttpResponse(str(sum))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
