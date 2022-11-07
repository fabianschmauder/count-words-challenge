
from count_words import countWords
from s3_utils import load_s3_object_content
from sns_utils import send_words_notification


def handle_record(record):
    s3_data = record["s3"]
    bucket_name = s3_data["bucket"]["name"]
    object_key = s3_data["object"]["key"]
    print("load data for "+ bucket_name + " " + object_key)
    content = load_s3_object_content(bucket_name, object_key)
    print("count words")
    number_of_words = countWords(content)
    send_words_notification(number_of_words, object_key)


def lambda_handler(event, context):
    for record in event["Records"]:
        handle_record(record)

