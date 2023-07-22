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

    timezone = req.params.get('timezone')

    if not timezone:
        try:
            req_json = req.get_json()
        except ValueError:
            pass
        else:
            name = req_json.get('timezone')

    if timezone:
        current_time = datetime.now(pytz.timezone(timezone)).strftime('%H:%M %A %d %B %Y')
        return func.HttpResponse(
            json.dumps({'timezone': timezone, 'current_time': current_time}),
            mimetype='application/json'
        )
    else:
        return func.HttpResponse(
             "Please send an appropriate request to the API.",
             status_code=200
        )