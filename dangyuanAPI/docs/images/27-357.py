class Stones():
    '''石子类'''

    def __init__(self):
        self.stones = {'A': 3, 'B': 5, 'C': 7}

    def remove(self, which, num):
        if which not in ['A', 'B', 'C']:
            print('只能在 A B C 中做选择!')
            return False
        if not self.can_remove(which, num):
            print(f'不能从{which}中拿{num}个石子')
            return False
        self.stones[which] -= num
        self.show_stones()
        return True

    def can_remove(self, which, num):
        if num > self.stones[which]:
            print(f'{which}中还剩下{self.stones[which]}个石子')
            return False
        return True

    def show_stones(self):
        print('A:','*'*self.stones['A'])
        print('B:','*'*self.stones['B'])
        print('C:','*'*self.stones['C'])

    def is_onlyone(self):
        if self.stones['A']+self.stones['B']+self.stones['C'] == 1:
            return True
        return False

class Player():
    '''玩家类'''
    
    def __init__(self, stones, name):
        self.stones = stones
        self.name = name

    def remove(self):
        result = False
        print(f'{self.name}开始拿了...')
        while not result:
            which = input(f'{self.name}，请输入你要在哪堆上拿(A B C): ')
            num = int(input(f'{self.name}，请输入你要拿多少个: '))
            result = self.stones.remove(which, num)

    
class Judge():
    '''裁判类'''

    def __init__(self, stones, player1, player2):
        self.stones = stones
        self.player1 = player1
        self.player2 = player2
        self.who_is_next = player1

    def let_player_play(self):
        self.who_is_next.remove()
        self.update_next_player()

    def update_next_player(self):
        if self.who_is_next == self.player1:
            self.who_is_next = self.player2
        else:
            self.who_is_next = self.player1

    def is_game_over(self):
        if self.stones.is_onlyone():
            return True
        return False

    def show_result(self):
        print('--- GAME OVER ---')
        print(f'{self.who_is_next.name}，很抱歉，你输了!')

    def tell_rules(self):
        '''告知游戏规则'''

    def start_game(self):
        '''开始游戏，打印游戏初始状态'''
        self.stones.show_stones()
        

def main():
    stones = Stones()
    name1 = input('请输入玩家1的名字：')
    player1 = Player(stones, name1)
    name2 = input('请输入玩家2的名字：')
    player2 = Player(stones, name2)
    judge = Judge(stones, player1, player2)

    judge.tell_rules()
    judge.start_game()
    while True:
        judge.let_player_play()
        if judge.is_game_over():
            judge.show_result()
            break


if __name__ == '__main__':
    main()


