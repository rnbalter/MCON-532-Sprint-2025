import os #allows us to maniuplate/find/load files
from openai import OpenAI #open openai package
from dotenv import load_dotenv #containes env variables used in execution of spec program hence .env. env = env vars

# Load the .env file only once
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
#path basically allows you to join two paths: getting the current file ie in the src directory ie os then just add a "/.env" joining names and dir locations
load_dotenv(dotenv_path=dotenv_path)
#then loads the combined path .env file and makes the env vars defeined in .env available to the current python process
#therefore in current python process the envvars are avail

# Initialize the client only once
_client_instance = None

#creates a single global instance avail to whole process space kinda like static - dont want to create client mult times
#only call this method once and then reuse this one client on subseq pulls
def get_openai_client():
    global _client_instance
    if _client_instance is None: #if doesnt exist then create the client:
        api_key = os.getenv("OPENAI_API_KEY")
        org_id = os.getenv("OPENAI_ORG_ID").strip()
        _client_instance = OpenAI(api_key=api_key, organization=org_id) #passes key and id and calls openai method to fetch our one instance of client
    return _client_instance