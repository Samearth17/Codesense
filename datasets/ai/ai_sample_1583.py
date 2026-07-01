import os
import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'PATH_TO_CREDENTIALS_FILE'

DIALOGFLOW_PROJECT_ID = 'YOUR_PROJECT_ID'
DIALOGFLOW_LANGUAGE_CODE = 'en-us'
GOOGLE_APPLICATION_CREDENTIALS = 'PATH_TO_CREDENTIALS_FILE'
SESSION_ID = 'current-user-id'

def detect_intent_from_text(text, session_id, language_code=DIALOGFLOW_LANGUAGE_CODE):
 session_client = dialogflow.SessionsClient()
 session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)
 text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
 query_input = dialogflow.types.QueryInput(text=text_input)
 try:
 response = session_client.detect_intent(session=session, query_input=query_input)
 return response.query_result
 except InvalidArgument:
 raise

# Create an intent in DialogFlow    
def intent_create():
 intents_client = dialogflow.IntentsClient()
 parent = intents_client.project_agent_path(DIALOGFLOW_PROJECT_ID)
 training_phrases = [
 dialogflow.types.Intent.TrainingPhrase(parts=[
 dialogflow.types.Intent.TrainingPhrase.Part(text='What is the weather like?'),
 ]),
]

message_text = dialogflow.types.Intent.Message.Text(text=['That\'s a great question!'])

response = intents_client.create_intent(
 parent,
 intent_name='[INTENT_NAME]',
 training_phrases=training_phrases,
 message=message_text
).per_response

# Retrieve a response to a user's query
query = 'What is the weather like in London?'
response = detect_intent_from_text(query, SESSION_ID)
print('Query text: {}'.format(response.query_text))
print('Detected intent: {} (confidence: {})\n'.format(
 response.intent.display_name, response.intent_detection_confidence))
print('Fulfillment text: {}'.format(response.fulfillment_text))