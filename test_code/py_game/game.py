# 导入模块
import pygame#导入pygame专门游戏的模块
from pygame.locals import *#导入pygame.locals的全部函数
import sys, random, time, math#导入sys访问模块，random随机模块，time时间模块，math数学模块


class GameWindow(object):
    '''创建游戏窗口类'''

    def __init__(self, *args, **kw):
        self.window_length = 600#窗口高度
        self.window_wide = 500#窗口宽度
        # 绘制游戏窗口，设置窗口尺寸
        self.game_window = pygame.display.set_mode((self.window_length, self.window_wide))
        # 设置游戏窗口标题
        pygame.display.set_caption("CatchBallGame")#标题CatchBallGame
        # 定义游戏窗口背景颜色参数
        self.window_color = (135, 206, 250)#RGB配色，做背景颜色

    def backgroud(self):
        # 绘制游戏窗口背景颜色
        self.game_window.fill(self.window_color)#调用上面的RGB自定义颜色


class Ball(object):
    '''创建球类'''

    def __init__(self, *args, **kw):
        # 设置球的半径、颜色、移动速度参数
        self.ball_color = (255, 215, 0)#球颜色，RGB
        self.move_x = 1#横向速度
        self.move_y = 1#纵向速度
        self.radius = 10#球半径10

    def ballready(self):
        # 设置球的初始位置、
        self.ball_x = self.mouse_x#球位置为鼠标的横坐标位置
        self.ball_y = self.window_wide - self.rect_wide - self.radius#纵坐标以球心位置为准
        # 绘制球，设置反弹触发条件
        pygame.draw.circle(self.game_window, self.ball_color, (self.ball_x, self.ball_y), self.radius)#绘制圆形的球，调用上面定义的窗口，球颜色，球的位置和半径

    def ballmove(self):
        # 绘制球，设置反弹触发条件
        pygame.draw.circle(self.game_window, self.ball_color, (self.ball_x, self.ball_y), self.radius)#同上 代码一样
        self.ball_x += self.move_x#反弹，横坐标增加
        self.ball_y -= self.move_y#纵坐标不断减小
        # 调用碰撞检测函数
        self.ball_window()#碰撞的是墙还是砖块
        self.ball_rect()#球的反应是怎样的（可以这么理解）
        # 每接5次球球速增加一倍
        if self.distance < self.radius:
            self.frequency += 1#接的次数加一
            if self.frequency == 5:#当满足频率5次的时候
                self.frequency = 0#归零
                self.move_x += self.move_x#速度加一倍 原来是1，现在就1+1=2，同理2+1=3
                self.move_y += self.move_y#同上
                self.point += self.point#分数加一
        # 设置游戏失败条件
        if self.ball_y > 520:  #窗顶到球心距离大于520，那就说明已经不在挡板上了。窗顶到球心距离等于520才是一直在挡板上。
            self.gameover = self.over_font.render("Game Over", False, (0, 0, 0))#定义一个游戏结束，False就表示失败，
            self.game_window.blit(self.gameover, (100, 130))
            self.over_sign = 1  #游戏结束标识


class Rect(object):
    '''创建球拍类'''

    def __init__(self, *args, **kw):  #初始化  def __init__()这种都代表是初始化
        # 设置球拍颜色参数
        self.rect_color = (255, 0, 0)#RGB控制挡板（球拍）颜色
        self.rect_length = 100#球拍的长度为100
        self.rect_wide = 10#球拍高度（宽度）

    def rectmove(self):
        # 获取鼠标位置参数
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()#获取鼠标横纵坐标
        # 绘制球拍，限定横向边界
        if self.mouse_x >= self.window_length - self.rect_length // 2:#如果鼠标横坐标大于了球拍最两侧中心位置
            self.mouse_x = self.window_length - self.rect_length // 2#那么就回归到球心最右侧位置 窗口宽度减去球拍一半的距离
        if self.mouse_x <= self.rect_length // 2:#如果鼠标横坐标小于了球拍最两侧中心位置
            self.mouse_x = self.rect_length // 2#那么鼠标横坐标位置就是球拍位置的一半
        pygame.draw.rect(self.game_window, self.rect_color, (
        (self.mouse_x - self.rect_length // 2), (self.window_wide - self.rect_wide), self.rect_length, self.rect_wide))#调用上面的参数


class Brick(object): #定义砖块这个类
    def __init__(self, *args, **kw):  #初始化
        # 设置砖块颜色参数
        self.brick_color = (139, 126, 102)#RGB控制砖块颜色
        self.brick_list = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1]] #定义砖块列表，砖块分为六列，五行，一个1代表一个砖块
        self.brick_length = 80#砖块长度80
        self.brick_wide = 20#砖块宽度20

    def brickarrange(self):
        for i in range(5):
            for j in range(6):  #遍历五行六列的砖块
                self.brick_x = j * (self.brick_length + 24)  #控制砖块的横向放置
                self.brick_y = i * (self.brick_wide + 20) + 40  #控制砖块的高度
                if self.brick_list[i][j] == 1:  #如果是1，那就是砖块，则执行下面的语句，把它画出来
                    # 调用前面定义好的参数，把砖块画出来到窗口固定位置
                    pygame.draw.rect(self.game_window, self.brick_color,
                                     (self.brick_x, self.brick_y, self.brick_length, self.brick_wide))
                    # 调用碰撞检测函数
                    self.ball_brick()
                    if self.distanceb < self.radius: #撞击到砖块
                        self.brick_list[i][j] = 0  #砖块就有1变为0
                        self.score += self.point#分数就加一
        # 设置游戏胜利条件：全部砖块被打掉，即所有的1变为0
        if self.brick_list == [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0]]:
            self.win = self.win_font.render("You Win", False, (0, 0, 0)) #显示出“you win”,一切就归零
            self.game_window.blit(self.win, (100, 130)) #控制“you win”位置
            self.win_sign = 1 #win的标识，赢了


class Score(object):
    '''创建分数类'''

    def __init__(self, *args, **kw):
        # 设置初始分数，开始的时候分数为0分
        self.score = 0
        # 设置分数字体为楷体，大小20
        self.score_font = pygame.font.SysFont('arial', 20)
        # 设置初始加分点数，撞击一次为1分
        self.point = 1
        # 设置初始接球次数，开始的时候撞击砖块0次
        self.frequency = 0

    def countscore(self): #定义计算分数的函数
        my_score = self.score_font.render(str(self.score), False, (255, 255, 255))
        self.game_window.blit(my_score, (555, 15))# 绘制玩家分数，分数的位置放在横坐标为555，距离窗顶位置15


class GameOver(object):
    '''创建游戏结束类'''

    def __init__(self, *args, **kw):
        # 设置Game Over字体   楷体，字体大小80
        self.over_font = pygame.font.SysFont('arial', 80)
        # 定义GameOver标识
        self.over_sign = 0


class Win(object):
    '''创建游戏胜利类'''

    def __init__(self, *args, **kw):
        # 设置You Win字体  楷体，字体大小80
        self.win_font = pygame.font.SysFont('arial', 80)
        # 定义Win标识
        self.win_sign = 0


class Collision(object):
    '''碰撞检测类'''

    # 球与窗口边框的碰撞检测
    def ball_window(self):
        if self.ball_x <= self.radius or self.ball_x >= (self.window_length - self.radius):#如果球横坐标位置小于球半径或者大于窗口宽度减去球半径，意思就是超出边界了
            self.move_x = -self.move_x#横坐标减小一个单位，意思就是反弹了
        if self.ball_y <= self.radius:#球纵坐标小于半径，意思就是只要没落地
            self.move_y = -self.move_y#继续向下移动

    # 球与球拍的碰撞检测
    def ball_rect(self):
        # 定义碰撞标识为0
        self.collision_sign_x = 0
        self.collision_sign_y = 0

#分三种情况，一种是直接碰到砖块反弹到球拍；一种是碰撞到砖块，又碰撞到墙；还有一种是碰到两个砖块，又碰到墙。这里用if-elif-else讨论。
        if self.ball_x < (self.mouse_x - self.rect_length // 2):  #如果球中心位置小于鼠标坐标减去球拍一半的长度，表示没有超出边界。即没有撞墙，撞一个砖块。
            self.closestpoint_x = self.mouse_x - self.rect_length // 2#横坐标最近点位置为鼠标位置减去球拍一半长度
            self.collision_sign_x = 1#这种情况，碰撞标识用1标识
        elif self.ball_x > (self.mouse_x + self.rect_length // 2):#超出边界范围，撞墙。碰到墙和砖块各一次。
            self.closestpoint_x = self.mouse_x + self.rect_length // 2#反弹了，横坐标最近位置为鼠标坐标加上球拍一半的长度。
            self.collision_sign_x = 2#这种情况，碰撞标识用2标识
        else: #上面两种情况都不满足的话执行下面的语句
            self.closestpoint_x = self.ball_x#横坐标最近点位置就是球位置。
            self.collision_sign_x = 3#这种情况，碰撞标识用3标识

        if self.ball_y < (self.window_wide - self.rect_wide):  #如果球的纵坐标小于窗口高度减去球心的高度。意思如果就是没有落地的话。
            self.closestpoint_y = (self.window_wide - self.rect_wide)#纵坐标最近距离为窗口高度减去球拍的高度
            self.collision_sign_y = 1#这种情况，碰撞标识用1标识
        elif self.ball_y > self.window_wide: #如果球的纵向长度大于了窗口高度，意思就是落地了
            self.closestpoint_y = self.window_wide#纵坐标最近位置就是窗口的高度（就刚好落地的时候）
            self.collision_sign_y = 2#这种情况，碰撞标识用2标识
        else:
            self.closestpoint_y = self.ball_y#球的最近纵坐标为球所在的位置
            self.collision_sign_y = 3#这种情况，碰撞标识用3标识
# 定义球拍到圆心最近点与圆心的距离   （最近点距离减去球心横坐标的距离的平方，加上纵坐标最近陆离减去球心纵坐标的平方），对这整体再开根号。意思就是求的两个位置之间的距离大小。
        self.distance = math.sqrt(
            math.pow(self.closestpoint_x - self.ball_x, 2) + math.pow(self.closestpoint_y - self.ball_y, 2))
        # 球在球拍上左、上中、上右3种情况的碰撞检测
        if self.distance < self.radius and self.collision_sign_y == 1 and (
                self.collision_sign_x == 1 or self.collision_sign_x == 2):  #如果满足：球拍到圆心最近点与圆心距离小于半径且纵坐标标识为1和横坐标标识为1或者2
            if self.collision_sign_x == 1 and self.move_x > 0:#如果横坐标标识为1并且横向速度大于0 。 向右速度大于0，向左速度小于0.！！！
                self.move_x = - self.move_x#水平速度反向
                self.move_y = - self.move_y#纵向速度也反向  就是反弹的意思
            if self.collision_sign_x == 1 and self.move_x < 0: #如果横向标识为1并且速度小于0 速度的大于小于零只是根据方向来说的，并不是速度的绝对值会小于0！！！
                self.move_y = - self.move_y#直竖直速度反向，就是弹回
            if self.collision_sign_x == 2 and self.move_x < 0:#如果横坐标标识为2并且一定速度小于0
                self.move_x = - self.move_x#水平速度反向
                self.move_y = - self.move_y#纵向速度也反向  就是反弹的意思
            if self.collision_sign_x == 2 and self.move_x > 0:#如果横坐标标识为2并且一定速度大于0
                self.move_y = - self.move_y#竖直速度反向 ，就是弹回
        if self.distance < self.radius and self.collision_sign_y == 1 and self.collision_sign_x == 3:#如果球拍到最近距离与球心距离小于球半径并且纵坐标标识为1和3
            self.move_y = - self.move_y#竖直速度反向概
        # 球在球拍左、右两侧中间的碰撞检测
        if self.distance < self.radius and self.collision_sign_y == 3:#如果球拍到最近距离与球心距离小于球半径并且纵坐标标识为3
            self.move_x = - self.move_x#水平速度反向

    # 球与砖块的碰撞检测
    def ball_brick(self):
        # 定义碰撞标识  开始标识都为0，标识没有碰撞
        self.collision_sign_bx = 0
        self.collision_sign_by = 0

        if self.ball_x < self.brick_x: #如果球横坐标小于砖块横向放置的位置大小
            self.closestpoint_bx = self.brick_x #砖块横坐标就是最近点位置
            self.collision_sign_bx = 1#标识为1
        elif self.ball_x > self.brick_x + self.brick_length:    #如果球横坐标大于砖块横向放的位置大小与砖块长度之和
            self.closestpoint_bx = self.brick_x + self.brick_length#最近点位置就是砖块横坐标放的位置大小加上砖块的长度
            self.collision_sign_bx = 2#标识为2
        else:#不是上面两种情况的话，执行下面语句
            self.closestpoint_bx = self.ball_x#球的横向最近陆离为球的中心横坐标
            self.collision_sign_bx = 3#这种情况标识为3
#y方向和x方向是同理的，就不解析描述了。
        if self.ball_y < self.brick_y:
            self.closestpoint_by = self.brick_y
            self.collision_sign_by = 1#标识为1
        elif self.ball_y > self.brick_y + self.brick_wide:
            self.closestpoint_by = self.brick_y + self.brick_wide
            self.collision_sign_by = 2#标识为2
        else:
            self.closestpoint_by = self.ball_y
            self.collision_sign_by = 3#标识为3
        # 定义砖块到圆心最近点与圆心的距离（两点距离公式，根号下横纵坐标差的平方和）
        self.distanceb = math.sqrt(
            math.pow(self.closestpoint_bx - self.ball_x, 2) + math.pow(self.closestpoint_by - self.ball_y, 2))
        # 球在砖块上左、上中、上右3种情况的碰撞检测  这个跟球在球拍的上左，上中，上右是一样的类似解析，这就不概述了
        if self.distanceb < self.radius and self.collision_sign_by == 1 and (
                self.collision_sign_bx == 1 or self.collision_sign_bx == 2):
            if self.collision_sign_bx == 1 and self.move_x > 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 1 and self.move_x < 0:
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x < 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x > 0:
                self.move_y = - self.move_y
        if self.distanceb < self.radius and self.collision_sign_by == 1 and self.collision_sign_bx == 3:
            self.move_y = - self.move_y
        # 球在砖块下左、下中、下右3种情况的碰撞检测  跟球在球拍的三个方向类似解析，不清楚可以看球在球拍的这三个方向解析
        if self.distanceb < self.radius and self.collision_sign_by == 2 and (
                self.collision_sign_bx == 1 or self.collision_sign_bx == 2):
            if self.collision_sign_bx == 1 and self.move_x > 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 1 and self.move_x < 0:
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x < 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x > 0:
                self.move_y = - self.move_y
        if self.distanceb < self.radius and self.collision_sign_by == 2 and self.collision_sign_bx == 3:
            self.move_y = - self.move_y
        # 球在砖块左、右两侧中间的碰撞检测
        if self.distanceb < self.radius and self.collision_sign_by == 3:
            self.move_x = - self.move_x


class Main(GameWindow, Rect, Ball, Brick, Collision, Score, Win, GameOver):
    '''创建主程序类'''

    def __init__(self, *args, **kw):  #初始化
        super(Main, self).__init__(*args, **kw) #调用（继承）父类的初始化，具体初始化看前面关于Main的类
        super(GameWindow, self).__init__(*args, **kw)#调用（继承）父类的初始化，调用前面GameWindow这个类
        super(Rect, self).__init__(*args, **kw)#这是对继承自父类的属性进行初始化。下面同理。
        super(Ball, self).__init__(*args, **kw)
        super(Brick, self).__init__(*args, **kw)
        super(Collision, self).__init__(*args, **kw)
        super(Score, self).__init__(*args, **kw)
        super(Win, self).__init__(*args, **kw)
        # 定义游戏开始标识
        start_sign = 0

        while True: #为真就执行
            self.backgroud() #窗口背景
            self.rectmove() #移动
            self.countscore()#计算分数

            if self.over_sign == 1 or self.win_sign == 1:  #如果着两个标识为1就结束循环了
                break
            # 获取游戏窗口状态
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #触发事件为游戏结束/离开
                    sys.exit() #退出程序
                if event.type == MOUSEBUTTONDOWN:#触发事件为鼠标移动
                    pressed_array = pygame.mouse.get_pressed() # 获取鼠标按键的情况（是否被按下
                    if pressed_array[0]:#如果为这种情况
                        start_sign = 1 #开始标识为1
            if start_sign == 0: #开始标识为0
                self.ballready()#调用球位置这个类
            else:#不然的话
                self.ballmove()#调用前面球移动这个类allmove

            self.brickarrange()#调用砖块这个类

            # 更新游戏窗口，重新开始
            pygame.display.update()
            # 控制游戏窗口刷新频率，频率越小效果越好，但是要求电脑性能越高，所以不能太低
            time.sleep(0.010)


if __name__ == '__main__':  #执行函数
    pygame.init()
    pygame.font.init()
    catchball = Main()