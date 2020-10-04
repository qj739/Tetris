# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time

import random

brick_array = [[0 for i in range(20)] for i in range(10)]

#brick 0---方块 1---长条 2---T字 3---L 4---倒L 5---Z字 6---倒Z
current_brick_id=1
next_brick_id = 1
game_over = False

current_brick_direct = 0
next_brick_direct = 0
current_y_pos = 19
current_x_pos = 5

speed = 0.1

#方块MASK
Square_mask = [[
    [1,1,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ],
    
    [[1,1,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ],

    [[1,1,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ],

    [[1,1,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]
    ]

Line_mask= [[
    [1,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ],
    
    [[1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0]
    ],

    [[1,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ],

    [[1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0]
    ]
    ]

T_mask = [[
    [1,1,1,0],
    [0,1,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ],
    
    [[0,1,0,0],
    [0,1,1,0],
    [0,1,0,0],
    [0,0,0,0]
    ],

    [[0,0,0,0],
    [0,1,0,0],
    [1,1,1,0],
    [0,0,0,0]
    ],

    [[0,1,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,0,0,0]
    ]
    ]

L1_mask = [[
    [1,0,0,0],
    [1,0,0,0],
    [1,1,0,0],
    [0,0,0,0]
    ],
    
    [[0,0,0,0],
    [0,0,1,0],
    [1,1,1,0],
    [0,0,0,0]
    ],

    [[0,1,1,0],
    [0,0,1,0],
    [0,0,1,0],
    [0,0,0,0]
    ],

    [[1,1,1,0],
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]
    ]

L2_mask = [[
    [0,1,0,0],
    [0,1,0,0],
    [1,1,0,0],
    [0,0,0,0]
    ],
    
    [[1,1,1,0],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,0,0]
    ],

    [[1,1,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [0,0,0,0]
    ],

    [[1,0,0,0],
    [1,1,1,0],
    [0,0,0,0],
    [0,0,0,0]
    ]
    ]

Z1_mask = [[
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,0,0,0]
    ],
    
    [[0,1,1,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ],

    [[1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,0,0,0]
    ],

    [[0,1,1,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]
    ]


Z2_mask = [[
    [0,1,0,0],
    [1,1,0,0],
    [1,0,0,0],
    [0,0,0,0]
    ],
    
    [[1,1,0,0],
    [0,1,1,0],
    [0,0,0,0],
    [0,0,0,0]
    ],

    [[0,1,0,0],
    [1,1,0,0],
    [1,0,0,0],
    [0,0,0,0]
    ],

    [[1,1,0,0],
    [0,1,1,0],
    [0,0,0,0],
    [0,0,0,0]
    ]
    ]

all_brick_list=[Square_mask , Line_mask , T_mask , L1_mask , L2_mask , Z1_mask ,Z2_mask]

def print_text(s, font, x, y, text, fcolor=(255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    s.blit(imgText, (x, y))

def draw_game_rect(s):
    pygame.draw.rect(s, (0,0,0), ((0, 0), (240, 480)), 0)


def draw_brick_array(s):
    for x in range(10):
        for y in range(20):
            if brick_array[x][y] != 0:
                pygame.draw.rect(s, (128,128,128), ((x*24, 480-(y+1)*24), (23, 23)), 0)

def is_game_over():
    pass
        

#碰撞检测与处理 判断有没重合区域
def collid_process():
    current_brick_mask=all_brick_list[current_brick_id][current_brick_direct]
    for x in range(4):
        for y in range(4):
            #mask对应整个大图中的位置
            ab_x = current_x_pos + x
            ab_y = current_y_pos - y
            if ab_y < 0 and current_brick_mask[x][y] == 1:
                return True

            if current_brick_mask[x][y] == 1 and brick_array[ab_x][ab_y] == 1:
                return True
    return False

def draw_current_brick(s):
    current_brick_mask = all_brick_list[current_brick_id][current_brick_direct]
    for x in range(4):
        for y in range(4):
            if current_brick_mask[x][y] == 1:
                pygame.draw.rect(s, (128,128,128), (( (current_x_pos+x)*24, 480-(current_y_pos - y+1)*24), (23, 23)), 0)

def add_current_brick_to_map():
    current_brick_mask = all_brick_list[current_brick_id][current_brick_direct]

    for x in range(4):
        for y in range(4):
            ab_x = current_x_pos + x
            ab_y = current_y_pos - y
            if current_brick_mask[x][y] == 1:
                brick_array[ab_x][ab_y]=1


def x_collid():
    for x in range(4):
        for y in range(4):
            current_brick_mask=all_brick_list[current_brick_id][current_brick_direct]
            ab_x = current_x_pos + x
            if current_brick_mask[x][y] == 1:
                if ab_x >= 9:
                    return True
    return False 

def remove_line():
    global brick_array
    for y in range(20):
        is_full_line = True
        for x in range(10):
            if brick_array[x][y] != 1:
                is_full_line = False
                break

        if is_full_line:
            for ny in range(y ,19):
                for nx in range(10):
                    brick_array[nx][ny] = brick_array[nx][ny+1]

            for nx in range(10):
                brick_array[nx][19] = 0
            
            return True
    return False

def is_brick_outof_screen():
    for x in range(4):
        for y in range(4):
            current_brick_mask=all_brick_list[current_brick_id][current_brick_direct]
            ab_x = current_x_pos + x
            ab_y = current_y_pos - y
            if current_brick_mask[x][y] == 1 and ab_x>9:
                return True
    return False   

def move_x_pos_when_rotate():
    global current_x_pos
    if current_x_pos <= 6:
        return

    while is_brick_outof_screen():
        current_x_pos = current_x_pos - 1
    
            

def main():
    print("main")
    global current_y_pos
    global current_x_pos
    global next_brick_id
    global next_brick_direct
    global game_over
    global current_brick_direct
    global current_brick_id
    
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    f2 = pygame.font.Font(None, 72)  # GAME OVER 的字体

    pygame.display.set_caption("Teris")
    last_move_time = time.time() 
    while True:
        screen.fill((40, 40, 60))
        draw_game_rect(screen)
        draw_brick_array(screen)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key==K_UP:
                    current_brick_direct = (current_brick_direct + 1) % 4
                    move_x_pos_when_rotate()
                elif event.key ==K_DOWN:
                    print("k down")
                elif event.key ==K_RIGHT:
                    print("k right")
                    #判断X方向是否有碰撞
                    if not x_collid():
                        current_x_pos = current_x_pos + 1

                    if current_x_pos > 19:
                        current_x_pos = 19
                    
                elif event.key ==K_LEFT:
                    current_x_pos = current_x_pos - 1
                    if current_x_pos < 0:
                        current_x_pos = 0
                    
                
        draw_current_brick(screen)
        if time.time() - last_move_time > speed:
            last_move_time = time.time()
            current_y_pos = current_y_pos -1

            if collid_process():
                if current_y_pos == 18 and current_x_pos == 5:
                    game_over = True
                    
                current_y_pos = current_y_pos + 1
                add_current_brick_to_map()
                current_brick_id = next_brick_id
                current_brick_direct = next_brick_direct
                current_x_pos = 5
                current_y_pos = 19
                next_brick_id = random.randint(0,6)
                next_brick_direct = random.randint(0,3)
            
            if current_y_pos <= 0:
                current_y_pos = 0

        if game_over:
            print_text(screen , f2 , 300,200, 'GAME OVER', (200, 30, 30))

        remove_line_cnt = 0
        while remove_line():
            remove_line_cnt = remove_line_cnt +1
        
        if remove_line_cnt>0:
            print("remove "+ str(remove_line_cnt) + " line" )
        pygame.display.update()

if __name__ == "__main__":
    main()