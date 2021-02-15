from unittest import mock 
import pytest
from todos import create
from moto import mock
from todos import todoTable
import json


def test_create(mocker):
    mock_put_todo = mock.Mock(return_value = {
        "id": "624d5987-6d10-11eb-a287-7907faf8cf19",
        "text": "Learn Serverless",
        "checked": False,
        "createdAt": 1613120270064,
        "updatedAt": 1613120270064
    } )
    todoTable.put_todo = mock_put_todo
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
    assert create(
        event = {
            "body" : {
                "text": "aprende python"
            }
        },
        context = "something"
    ) == espected
    
    assert create(
        event = {
            "body" : {}
        },
        context = "something"
    ) != espected