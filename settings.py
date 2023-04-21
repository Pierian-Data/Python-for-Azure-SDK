import os
from dotenv import load_dotenv

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# Load environment variables
load_dotenv(os.path.join(BASEDIR, '.env'))
AZURE_SUBSCRIPTION_ID = os.getenv('AZURE_SUBSCRIPTION_ID')
CONNECTION_STRING = os.getenv('CONNECTION_STRING')
AZURE_CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
AZURE_TENANT_ID = os.getenv('AZURE_TENANT_ID')
AZURE_CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET')

# Default variables
DEFAULT_RESOURCE_GROUP = 'default-resource-group'
DEFAULT_LOCATION = 'eastus'