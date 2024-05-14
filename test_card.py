from main import Card


def test_blue_card_v1():
  card = Card.get("test.png")
  assert card.n_stars==2

def test_blue_card_v2(): #this screen has 1 star, but can 2
  card = Card.get("test_blue.png")
  assert card.n_stars==1

def test_violet_card():
  card = Card.get("test_violet.png")
  assert card.n_stars==4

def test_gray_card():
  card = Card.get("test_gray.png")
  assert card.n_stars==1

def test_gold_card():
  card = Card.get("test_gold.png")
  assert card.n_stars==3

def test_seven_card():
  card_one = Card.get("test.png")
  card_two = Card.get("test_blue.png")
  card_three = Card.get("test_gold.png")
  card_four = Card.get("test_gray.png")
  card_five = Card.get("test_violet.png")
  card_six = Card.get("test_violet.png")
  card_seven = Card.get("test_violet.png")
  assert Card.n_cards==6

def test_delete_card():
  card_one = Card.get("test.png")
  card_two = Card.get("test_blue.png")
  card_three = Card.get("test_gold.png")
  del card_two
  assert Card.n_cards==2
