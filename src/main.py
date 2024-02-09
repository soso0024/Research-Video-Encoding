import boto3
import csv
from datetime import datetime

# AWS authentication configuration
session = boto3.Session(profile_name='default')
client = session.client('ec2', region_name='us-east-1')

# Set start and end times
start_time = datetime(2023, 7, 9)
end_time = datetime(2023, 12, 31)

response = client.describe_spot_price_history(
    StartTime=start_time,
    EndTime=end_time,
    InstanceTypes=[
        'c5a.2xlarge',
    ],
    ProductDescriptions=[
        'Linux/UNIX (Amazon VPC)',
    ]
)

# write this response into a CSV file
csv_file_path = "../data/spot_price_history.csv"  # Path to save the CSV file

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(
        ['Timestamp', 'InstanceType', 'ProductDescription', 'SpotPrice',
         'AvailabilityZone'])

    # Iterate through the spot price history items and write each one
    for item in response['SpotPriceHistory']:
        writer.writerow([item['Timestamp'], item['InstanceType'],
                         item['ProductDescription'], item['SpotPrice'],
                         item['AvailabilityZone']])

print(f"Fin!")
