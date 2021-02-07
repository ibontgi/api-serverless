import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
translate = boto3.client('translate')

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    sourceLanguage = 'en'
    targetLanguage = event['pathParameters']['lang']
    textString  = result['Item']['text']

    translated = translate.translate_text(Text=textString, SourceLanguageCode=sourceLanguage, TargetLanguageCode=targetLanguage)

    #translated = translate.translate_text(Text : result['Item']['text'], SourceLanguageCode : "auto", TargetLanguageCode : event['pathParameters']['lang'])

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(translated, cls=decimalencoder.DecimalEncoder),
        
    }

    return response
