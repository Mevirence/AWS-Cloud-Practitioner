import json
import boto3

translate = boto3.client('translate')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        text = body.get('text')
        target = body.get('target')

        if not text or not target:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Both "text" and "target" fields are required.'})
            }

        result = translate.translate_text(
            Text=text,
            SourceLanguageCode='auto',  # Auto-detect source language
            TargetLanguageCode=target
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'translated_text': result['TranslatedText']})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
