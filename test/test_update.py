from unittest import mock 
import pytest
from todos import update
from moto import mock
from todos import todoTable
import json


def test_update(mocker):
    mock_put_todo = mock.Mock(return_value = {
        "id": "624d5987-6d10-11eb-a287-7907faf8cf19",
        "text": "aprende aws",
        "checked": False,
        "createdAt": 1613120270064,
        "updatedAt": 1613120270064
    } )
    todoTable.update_todo = mock_put_todo
    espected = {
        "statusCode": 200, 
        "body": {
        "id": "624d5987-6d10-11eb-a287-7907faf8cf19",
        "text": "aprende aws",
        "checked": False,
        "createdAt": 1613120270064,
        "updatedAt": 1613120270064
        }
    }
    assert update(
        event = {
            "pathParameters" : {
                "id": "624d5987-6d10-11eb-a287-7907faf8cf19"
            },
            "body" : {
                "text": "aprende aws"
            }
        },
        context = "something"
    ) == espected
