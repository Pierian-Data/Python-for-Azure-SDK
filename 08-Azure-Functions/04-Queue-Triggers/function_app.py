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

    if not timezone:
        try:
            req_body = req.get_body()
        except ValueError:
            pass
        else:
            name = req_body.get('timezone')

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


# Function example #2 - Blob storage
@app.function_name(name="BlobFunction")
@app.blob_trigger(arg_name="myblob", path="dl-file-system/raw-data/{name}",
                               connection="AzureWebJobsStorage")
def blob_function(myblob: func.InputStream):
    """Process incoming blob files

    Args:
        myblob (func.InputStream): Object for incoming blob file
    """
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")


# Function example #3: Queue Trigger
@app.function_name(name="QueueFunction")
@app.queue_trigger(arg_name="msg", queue_name="my-messages",
                               connection="AzureWebJobsStorage") 
def queue_trigger(msg: func.QueueMessage):
    """Process

    Args:
        msg (func.QueueMessage): _description_
    """
    logging.info(f"Python Queue trigger processed a message: {msg.get_body().decode('utf-8')}")