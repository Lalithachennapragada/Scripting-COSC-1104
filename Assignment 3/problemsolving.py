import boto3
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# AWS Configuration
REGION = 'us-east-1a'  # AWS region details
S3_BUCKET = 'lalithachennapragada-backup-bucket'  #  S3 bucket name
EMAIL_FROM = 'lalithalabcat@gmail.com'  # sender email
EMAIL_TO = 'lalithachennapragada88@gmail.com'  # recipient email
EMAIL_PASSWORD = 'lab@Password'  # sender email password
SMTP_SERVER = 'smtp.gmail.com'  # Use your email provider's SMTP server
SMTP_PORT = 587

# Initialize AWS clients
ec2 = boto3.client('ec2', region_name=REGION)
s3 = boto3.client('s3', region_name=REGION)

def create_snapshot(volume_id):
    """Creates a snapshot for a specified volume."""
    try:
        response = ec2.create_snapshot(VolumeId=volume_id, Description=f"Automated backup {datetime.now()}")
        snapshot_id = response['SnapshotId']
        print(f"Snapshot {snapshot_id} created for volume {volume_id}.")
        return snapshot_id
    except Exception as e:
        print(f"Error creating snapshot for volume {volume_id}: {e}")
        return None

def upload_snapshot_to_s3(snapshot_id):
    """Uploads snapshot metadata to S3."""
    try:
        metadata = {
            'SnapshotId': snapshot_id,
            'Timestamp': str(datetime.now())
        }
        s3.put_object(Bucket=S3_BUCKET, Key=f"backups/{snapshot_id}.json", Body=json.dumps(metadata))
        print(f"Snapshot metadata for {snapshot_id} uploaded to S3 bucket {S3_BUCKET}.")
    except Exception as e:
        print(f"Error uploading snapshot {snapshot_id} metadata to S3: {e}")

def send_email_notification(subject, body):
    """Sends an email notification."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email notification sent.")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    """Main function to automate the backup process."""
    try:
        volumes = ec2.describe_volumes()
        for volume in volumes['Volumes']:
            volume_id = volume['VolumeId']
            print(f"Processing volume {volume_id}...")
            snapshot_id = create_snapshot(volume_id)
            if snapshot_id:
                upload_snapshot_to_s3(snapshot_id)
                send_email_notification(
                    subject=f"Backup Successful for Volume {volume_id}",
                    body=f"Snapshot {snapshot_id} created and uploaded to S3."
                )
            else:
                send_email_notification(
                    subject=f"Backup Failed for Volume {volume_id}",
                    body=f"Snapshot creation failed for volume {volume_id}."
                )
    except Exception as e:
        print(f"Error in the backup process: {e}")
        send_email_notification(
            subject="Backup Process Failed",
            body=f"An error occurred: {e}"
        )

if __name__ == '__main__':
    main()
