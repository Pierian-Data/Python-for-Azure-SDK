from datetime import datetime
import json
import pytz

import azure.functions as func
import logging

# Register function app
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


# Function example #1 - HTTP Trigger
@app.function_name(name="TimeZoneHttpTrigger")
@app.route(route="timezone", auth_level=func.AuthLevel.ANONYMOUS)
def TimeZoneHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    """Function to return current time in a given timezone based on an
    HTTP request with the desired timezone

    Args:
        req (func.HttpRequest): HTTP request with JSON object containing
        relevant timezone string

    Returns:
        func.HttpResponse: HTTP response with current time information or
        error message
    """

    logging.info('Timezone HTTP trigger function received a request.')

    timezone = req.get_json()['timezone']

    return func.HttpResponse(f'{timezone}')