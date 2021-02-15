from unittest import mock 
import pytest
from todos import getlang
from moto import mock
from todos import todoTable
import json


def test_getlang(mocker):
    mock_get_todo = mock.Mock(
        return_value = {
            "TranslatedText": "Apprendre Serverless",
            "SourceLanguageCode": "en",
            "TargetLanguageCode": "fr",
            "ResponseMetadata": {
                "RequestId": "0b4a91d7-badb-45c3-b7f5-ee7775bdf80a",
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "x-amzn-requestid":
                    "0b4a91d7-badb-45c3-b7f5-ee7775bdf80a",
                    "cache-control":"no-cache",
                    "content-type": "application/x-amz-json-1.1",
                    "content-length": "93",
                    "date": "Thu, 04 Feb 2021 18:22:51 GMT"
                },
                "RetryAttempts": 0
            }
        }
    )
    todoTable.get_todo = mock_get_todo
    espected = {
        "TranslatedText": "Apprendre Serverless",
        "SourceLanguageCode": "en",
        "TargetLanguageCode": "fr",
        "ResponseMetadata": {
            "RequestId": "0b4a91d7-badb-45c3-b7f5-ee7775bdf80a",
            "HTTPStatusCode": 200,
            "HTTPHeaders": {
                "x-amzn-requestid":
                "0b4a91d7-badb-45c3-b7f5-ee7775bdf80a",
                "cache-control":"no-cache",
                "content-type": "application/x-amz-json-1.1",
                "content-length": "93",
                "date": "Thu, 04 Feb 2021 18:22:51 GMT"
            },
            "RetryAttempts": 0
        }
    }
    assert getlang(
        event = {
            "pathParameters" : {
                "id": "624d5987-6d10-11eb-a287-7907faf8cf19",
                "lang": "fr"
            }
        },
        context = "something"
    ) == espected
    
    assert getlang(
        event = {
            "body" : {}
        },
        context = "something"
    ) != espected