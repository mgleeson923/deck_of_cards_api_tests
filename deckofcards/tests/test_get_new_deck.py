import pytest
import requests
import pdb
import logging as logger


## This test verifies site health by getting a 200 code back, and gets a new deck to use

@pytest.mark.tcid1
def test_get_new_deck():
    response = requests.get('https://deckofcardsapi.com/api/deck/new/')
    assert response.status_code is 200
    response_body = response.json()
    assert response_body['success'] is True

    logger.info(response_body)