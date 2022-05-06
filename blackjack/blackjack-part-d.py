from random import shuffle

def create_deck() -> list:
  deck = []
  face_values = ["A", "J", "Q", "K"]

  for i in range(4):
    for card in range(2, 11):
      deck.append(str(card))
    for card in face_values:
      deck.append(card)
  shuffle(deck)
  return deck

card_deck = create_deck()
print(card_deck)


class Player:
  def __init__(self, hand = [], money = 100) -> None:
    self.hand = hand
    self.score = self.set_score()
    self.money = money
    self.bet_money = 0
  
  def __str__(self) -> str:
    current_hand = ""
    for card in self.hand:
      current_hand += str(card) + " "
    final_status = f"{current_hand} score: {self.score}"
    return final_status

  def set_score(self):
    self.score = 0
    face_card_dict = {"A": 11, "J": 10, "Q": 10, "K": 10,
                       "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9, "10": 10 }
    ace_counter = 0
    for card in self.hand:
      self.score += face_card_dict[card]
      if card == "A":
        ace_counter += 1
      if self.score > 21 and ace_counter != 0:
        self.score -= 10
        ace_counter -= 1
    return self.score

  def hit(self, card):
    self.hand.append(card)
    self.score = self.set_score()

  def play(self, new_hand):
    self.hand = new_hand
    self.score = self.set_score()

  def bet(self, amount: int):
    self.money -= amount
    self.bet_money += amount

  def win(self, result: bool):
    if result:
      if self.score == 21 and len(self.hand) == 2:
        self.money += 2.5*self.bet_money
      else:
        self.money += (2 * self.bet_money)
      self.bet_money = 0
    else:
      self.bet_money = 0

player = Player(["3", "7", "5"])
print(player)
player.hit("A")
player.hit("A")
print(player)
player.bet(20)
print(player.money, player.bet_money)
player.win(True)
print(player.money, player.bet_money)
player.play(["A", "K"])
print(player)
player.bet(20)
player.win(True)
print(player.money, player.bet_money)