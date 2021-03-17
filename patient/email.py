import boto3
from botocore.exceptions import ClientError


class Email(object):
    def __init__(self, recipient, score):
        self._recipient = recipient
        self._score = score
        self.send()

    def send(self):
        # Replace sender@example.com with your "From" address.
        # This address must be verified with Amazon SES.
        sender = "Sender Name <sender@example.com>"

        # Replace recipient@example.com with a "To" address. If your account
        # is still in the sandbox, this address must be verified.
        recipient = "recipient@example.com"

        # Specify a configuration set. If you do not want to use a configuration
        # set, comment the following variable, and the
        # ConfigurationSetName=CONFIGURATION_SET argument below.
        configuration_set = "ConfigSet"

        # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        aws_region = "eu-west-2"

        # The subject line for the email.
        subject = "Your Framingham Score"

        # The email body for recipients with non-HTML email clients.
        body_text = ("Framingham results"
                     )

        # The HTML body of the email.
        body_html = """<html>
        <head></head>
        <body>
          <h1>Framingham Score</h1>
          <p>Your framingham score for cardiovascular health is {}</p>
        </body>
        </html>
                    """.format(self._score)

        # The character encoding for the email.
        charset = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=aws_region)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        recipient,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': charset,
                            'Data': body_html,
                        },
                        'Text': {
                            'Charset': charset,
                            'Data': body_text,
                        },
                    },
                    'Subject': {
                        'Charset': charset,
                        'Data': subject,
                    },
                },
                Source=sender,
                # If you are not using a configuration set, comment or delete the
                # following line
                ConfigurationSetName=configuration_set,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
