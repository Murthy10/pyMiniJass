import inspect

from pyMiniJass.rules.stich_rules import allowed_cards


class BasePlayer:
    def __init__(self, name='unknown'):
        self.name = name
        self.cards = []
        self.id = None

    def get_dict(self):
        return dict(name=self.name, type=type(self).__name__)

    def set_card(self, card):
        self.cards.append(card)

    def choose_card(self, state=None):
        raise NotImplementedError(str(inspect.stack()[1][3]))

    def stich_over(self, state=None):
        pass

    def allowed_cards(self, first_card):
        return allowed_cards(hand_cards=self.cards, first_card=first_card)

    def __str__(self):
        return '<Player:{}>'.format(self.name)
