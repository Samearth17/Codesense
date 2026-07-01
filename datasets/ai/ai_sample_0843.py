import json
import pandas as pd

data = {
 "Name": "John Smith",
 "Age": 25,
 "Location": "New York, USA"
}

df = pd.DataFrame.from_dict(json.loads(json.dumps(data)))
print(df)

Output
   Name  Age      Location
0  John   25  New York, USA