from unittest import mock 
import pytest
from todos import delete
from moto import mock
from todos import todoTable
import json


def test_delete(mocker):
    mock_delete_todo = mock.Mock()
    todoTable.delete_todo = mock_delete_todo
    espected = {
        "statusCode": 200
    }
    assert delete(
        event = {
            "pathParameters" : {
                "id": "624d5987-6d10-11eb-a287-7907faf8cf19"
            }
        },
        context = "something"
    ) == espected
    
    assert delete(
        event = {
            "body" : {}
        },
        context = "something"
    ) != espected