from email.message import Message
import boto3

client = boto3.client('sns')

topic_arn = "arn:aws:sns:us-west-2:534283426081:fancy-count-words-topic"


def send_words_notification(number_of_words, filename):
    client.publish(
        TopicArn=topic_arn,
        Subject="Number of words",
        Message="The word count in the file " +
        filename + " is " + str(number_of_words)+". "
    )
