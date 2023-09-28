import pytest
import requests
import pdb
import logging as logger


## This test verifies site health by getting a 200 code back, and gets a new deck to use

@pytest.mark.tcid2
def test_shuffle_deck():
    response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    assert response.status_code is 200
    response_body = response.json()
    assert response_body['success'] is True
    deck_id = response_body['deck_id']
    assert response_body['shuffled'] is True
    assert response_body['remaining'] is 52

    logger.info(response_body)

