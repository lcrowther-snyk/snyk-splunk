import boto3
import json

# Initialize a boto3 client for EventBridge
client = boto3.client('events')

# Define the event details
event_entry = {
    'Source': '',
    'DetailType': 'Snyk Finding',
    'Detail': json.dumps({
        'id': '1234',
        'project': 'test-project',
        'severity': 'high',
        'message': 'Test Snyk vulnerability detected'
    }),
    'EventBusName': ""
}

# Send the event to EventBridge
response = client.put_events(
    Entries=[event_entry]
)

# Print the response from AWS
print("Response:", response)
