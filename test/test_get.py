from unittest import mock 
import pytest
from todos import get
from moto import mock
from todos import todoTable
import json


def test_get(mocker):
    mock_get_todo = mock.Mock(return_value = {
        "id": "624d5987-6d10-11eb-a287-7907faf8cf19",
        "text": "Learn Serverless",
        "checked": False,
        "createdAt": 1613120270064,
        "updatedAt": 1613120270064
    } )
    todoTable.get_todo = mock_get_todo
    espected = {
        "statusCode": 200, 
        "body": {
        "id": "624d5987-6d10-11eb-a287-7907faf8cf19",
        "text": "Learn Serverless",
        "checked": False,
        "createdAt": 1613120270064,
        "updatedAt": 1613120270064
        }
    }
    assert get(
        event = {
            "pathParameters" : {
                "id": "624d5987-6d10-11eb-a287-7907faf8cf19"
            }
        },
        context = "something"
    ) == espected
    
    assert get(
        event = {
            "body" : {}
        },
        context = "something"
    ) != espected