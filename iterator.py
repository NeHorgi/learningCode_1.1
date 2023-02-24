'''
Реализуйте итератор колоды карт (52 штуки) CardDeck
Каждая карта представлена в виде строки типа "2 Пик". При вызове функции next()
Будет возвращаться следующая карта. "3 Пик "...
По окончании перебора всех элементов выводится сообщения "Колода закончилась"
'''


class CardDeck: # TODO вообще не правильно! чекни мэйн, почему.
    # Прочитать еще раз про итераторы!

    def __init__(self):
        self.Deck = 52
        self.card = 0
        self.colors = ['Пик', 'Черви', 'Буби', 'Крести']
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз']

    def __next__(self):

        while self.card < self.Deck:

            for color in self.colors:
                for card in self.cards:
                    self.card += 1
                    print(f'{card} {color}')

        print(f'Колода закончилась')
        StopIteration

    def __iter__(self):
        return self

if __name__ == '__main__':
    deck = CardDeck()
    for cart in deck:
        print(cart)

    # deck.__next__()
