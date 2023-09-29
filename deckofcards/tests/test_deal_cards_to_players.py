from operator import index

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

    ## Create player one's hand
    draw_response = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id + '/draw/?count=3')
    draw_response_body = draw_response.json()
    cards = draw_response_body['cards']
    pile_one = 'pile_one'

    player_one_cards = []
    for card in cards:
        assert len(card['code']) is 2
        cards_response_one = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id +
                                          '/pile/' + pile_one + '/add/?cards=' + card['code'])
        assert cards_response_one.status_code is 200
        player_one_cards.append(card['value'])
    logger.debug(player_one_cards)

    i = 0
    while i < len(player_one_cards):
        if player_one_cards[i] == 'KING':
            player_one_cards[i] = '10'
        if player_one_cards[i] == 'QUEEN':
            player_one_cards[i] = '10'
        if player_one_cards[i] == 'JACK':
            player_one_cards[i] = '10'
        if player_one_cards[i] == 'ACE':
            player_one_cards[i] = '10'
        i += 1

    player_one_cards = [eval(i) for i in player_one_cards]
    logger.debug(player_one_cards)
    player_one_hand_value = sum(player_one_cards)
    if player_one_hand_value == 21:
        print("Blackjack")
    logger.debug(player_one_hand_value)

    ## Create player two's hand
    draw_response = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id + '/draw/?count=3')
    draw_response_body = draw_response.json()
    cards = draw_response_body['cards']
    logger.info(cards)
    pile_two = 'pile_two'

    player_two_cards = []
    for card in cards:
        assert len(card['code']) is 2
        cards_response_two = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id +
                                          '/pile/' + pile_two + '/add/?cards=' + card['code'])
        assert cards_response_two.status_code is 200
        player_two_cards.append(card['value'])
    logger.debug(player_two_cards)

    i = 0
    while i < len(player_two_cards):
        if player_two_cards[i] == 'KING':
            player_two_cards[i] = '10'
        if player_two_cards[i] == 'QUEEN':
            player_two_cards[i] = '10'
        if player_two_cards[i] == 'JACK':
            player_two_cards[i] = '10'
        if player_two_cards[i] == 'ACE':
            player_two_cards[i] = '10'
        i += 1

    player_two_cards = [eval(i) for i in player_two_cards]
    logger.debug(player_two_cards)
    player_two_hand_value = sum(player_two_cards)
    if player_two_hand_value == 21:
        print("Blackjack")
    logger.debug(player_two_hand_value)
