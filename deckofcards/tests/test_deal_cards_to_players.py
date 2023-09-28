import pytest
import requests
import pdb
import logging as logger


## This test draws cards from the deck, then places them into two piles (player hands)

@pytest.mark.tcid3
def test_draw_cards_from_deck():
    response_shuffle = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    assert response_shuffle.status_code is 200
    shuffle_response_body = response_shuffle.json()
    assert shuffle_response_body['success'] is True
    deck_id = shuffle_response_body['deck_id']
    assert shuffle_response_body['shuffled'] is True
    assert shuffle_response_body['remaining'] is 52

    draw_response = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id + '/draw/?count=3')
    draw_response_body = draw_response.json()
    cards = draw_response_body['cards']
    logger.info(cards)
    pile_one = 'pile_one'

    for card in cards:
        assert len(card['code']) is 2
        cards_response_one = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id +
                                          '/pile/' + pile_one + '/add/?cards=' + card['code'])
        assert cards_response_one.status_code is 200

    player_one_hand = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id +
                                   '/pile/' + pile_one + '/list/')
    response_body = player_one_hand.json()
    logger.info(response_body)

    draw_response = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id + '/draw/?count=3')
    draw_response_body = draw_response.json()
    cards = draw_response_body['cards']
    logger.info(cards)
    pile_two = 'pile_two'

    for card in cards:
        assert len(card['code']) is 2
        cards_response_two = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id +
                                          '/pile/' + pile_two + '/add/?cards=' + card['code'])
        assert cards_response_two.status_code is 200
    player_two_hand = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id +
                                   '/pile/' + pile_two + '/list/')
    response_body = player_two_hand.json()

    logger.info(response_body)
