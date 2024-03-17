from main import Card

#test to write

card_one = Card.get("test.png")
print(card_one)
print(Card.n_cards)

card_two = Card.get("test_blue.png")
print(card_two)
print(Card.n_cards)

card_three = Card.get("test_gold.png")
print(card_three)
print(Card.n_cards)

card_four = Card.get("test_gray.png")
print(card_four)
print(Card.n_cards)

card_five = Card.get("test_violet.png")
print(card_five)
print(Card.n_cards)

card_six = Card.get("test_violet.png")
print(card_six)
print(Card.n_cards)

card_seven = Card.get("test_violet.png")
print(card_seven)
print(Card.n_cards)

del card_six
print(Card.n_cards)