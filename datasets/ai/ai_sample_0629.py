import pandas as pd
from google.cloud import automl

# Create an Automl Client
client = automl.TablesClient(project='PROJECT_ID', region='us-central1')

def predict_team(player_name, position):
 """
 Generates a team recommendation using AutoML based on player's name and position.
 """
 # Create tables client
 model_display_name = 'YOUR_MODEL_DISPLAY_NAME'
 table_spec_name = f'projects/PROJECT_ID/locations/us-central1/tables/{model_display_name}'

 # Create the dataframe with player data
 data = {
 'player_name': player_name,
 'position': position
 }
 df = pd.DataFrame(data, index=[0])

 # Create a prediction object
 pred_bt = client.predict(
 model_display_name=model_display_name,
 inputs=df[['player_name', 'position']],
 table_spec_name=table_spec_name
 )

 # Format into team recommendation
 team_name = pred_bt.payload[0].tables.value.string_value
 return team_name

target_player = 'Yadiel Rivera'
target_position = 'Shortstop'
result = predict_team(target_player, target_position)
print(f'For player {target_player} playing {target_position}: {result}')