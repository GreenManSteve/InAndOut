import boto3
from botocore.exceptions import ClientError


class Email(object):
    def __init__(self, recipient, score):
        self._recipient = recipient
        self._score = score
        self.send()

    def send(self):
        # The character encoding for the email.
        CHARSET = "UTF-8"
        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name='eu-west-2')
        SUBJECT = "SUBJECT"
        BODY_TEXT = "BODY_TEXT"
        BODY_HTML = """<html>
        <head></head>
        <body>
          <h1>{subject}</h1>
          <p>{message}<br />
          </p>
        </body>
        </html>
                    """.format(subject=SUBJECT, message=BODY_TEXT)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        self._recipient,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source="arn:aws:ses:eu-west-2:849843121008:identity/stevenattwell@hotmail.com",
                # If you are not using a configuration set, comment or delete the
                # following line
                # ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])

