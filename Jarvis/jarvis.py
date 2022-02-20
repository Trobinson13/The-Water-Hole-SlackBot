import slack
import os
from pathlib import Path
from dotenv import load_dotenv

#loading environment variable file into system env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#Setting the webclient to read its authentication token from the systems environment variable defined in .env file.
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

#posting message in target channel
client.chat_postMessage(channel='#jarvis-playground', text="Ah. Good day, world.  How may I be of service?")