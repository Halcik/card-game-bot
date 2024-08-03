from main import Card


def test_blue_card_v1():
  card = Card.get("test.png")
  assert card.n_stars==2
  assert card.powers[4]==7


def test_blue_card_v2(): #this screen has 1 star, but can 2
  card = Card.get("test_blue.png")
  assert card.n_stars==1
  assert card.powers[4]==11


def test_violet_card():
  card = Card.get("test_violet.png")
  assert card.n_stars==4
  assert card.powers[4]==11


def test_gray_card():
  card = Card.get("test_gray.png")
  assert card.n_stars==1
  assert card.powers[4]==5


def test_gold_card():
  card = Card.get("test_gold.png")
  assert card.n_stars==3
  assert card.powers[4]==9


def test_seven_card():
  card_one = Card.get("test.png")
  card_two = Card.get("test_blue.png")
  card_three = Card.get("test_gold.png")
  card_four = Card.get("test_gray.png")
  card_five = Card.get("test_violet.png")
  card_six = Card.get("test_violet.png")
  card_seven = Card.get("test_violet.png")
  assert card_seven=="Nie udało się stworzyć karty"
  assert len(Card.positions)==6


def test_delete_card():
  card_one = Card.get("test.png")
  card_two = Card.get("test_blue.png")
  card_three = Card.get("test_gold.png")
  del card_two
  assert len(Card.positions)==2


def test_simple_position_card():
  card_one = Card.get("test.png")
  card_two = Card.get("test.png")
  card_three = Card.get("test.png")
  card_four = Card.get("test_gold.png")
  cards = [card_one, card_two, card_three, card_four]
  positions = [
    str(card.position)
    for card in cards
    ]
  positions = "".join(positions)
  assert positions=="1230"


def test_card_compatibility():
  card_one = Card.get("test.png")
  card_two = Card.get("test.png")
  card_three = Card.get("test.png")
  assert Card.positions[0].__call__()==card_one #or without __call__ and with weakref.ref(card_one)
  assert Card.positions[1].__call__()==card_two
  assert Card.positions[2].__call__()==card_three

def test_use_card():
  card_one = Card.get("test.png")
  card_one.use()
  assert card_one.energy==3
  card_one.use()
  assert card_one.energy==2
  card_one.use()
  assert card_one.energy==1
  card_one.use()
  assert card_one.energy==0
  card_one.use()
  assert card_one.energy==0

def test_sum_of_powers():
  card_one = Card.get("test.png")
  card_two = Card.get("test_blue.png")
  card_three = Card.get("test_gold.png")
  card_four = Card.get("test_gray.png")
  card_five = Card.get("test_violet.png")
  card_six = Card.get("test_violet.png")
  assert Card.sum_of_powers(0)==19
  assert Card.sum_of_powers(1)==6
  assert Card.sum_of_powers(2)==15
  assert Card.sum_of_powers(3)==14
  assert Card.sum_of_powers(4)==54
  assert Card.sum_of_powers()==54

def test_delete_weak_card():
  card_one = Card.get("test.png") #2
  card_two = Card.get("test.png") #1
  card_three = Card.get("test.png") #3 this will be delete from list
  card_four = Card.get("test_gold.png") #0
  Card.delete_weak_card()
  assert len(Card.positions)==3
  assert Card.positions[-1].__call__()!=card_three