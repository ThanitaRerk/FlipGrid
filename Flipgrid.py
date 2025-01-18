import curses
import random
boards = [
  ['X', 'X', 'X', 'X', 'X'],
  ['X', 'X', 'X', 'X', 'X'],
  ['X', 'X', 'X', 'X', 'X'],
  ['X', 'X', 'X', 'X', 'X'],
  ['X', 'X', 'X', 'X', 'X']
]
curX = 2 #ตำแหน่งcursorเมื่อเทียบกับ board  game
curY = 2 #ตำแหน่งcursorเมื่อเทียบกับ board  game
move = 0
def initGame() : #ฟังก์ชั่นเอาไว้กำหนดค่าเริ่มต้นของเกม
  global sc #ประกาศตัวแปร
  sc = curses.initscr() #กำหนดหน้าจอที่ใช้รันเกม
  sc.keypad(True) #เปิดการใช้งานลูกศรในkeyboard
  curses.curs_set(0) #ปิดการแสดงผล cursor
  for i in range(10):
    ranX = random.randrange(0,5)
    ranY = random.randrange(0,5)
    updateBoard(ranY,ranX)

def switch(y, x) : #เปลี่ยนxเป็นo และoเป็นx
  if boards[y][x] == 'X' :
    boards[y][x] = 'O'
  elif boards[y][x] == 'O' :
    boards[y][x] = 'X'

def updateBoard(y, x) : #อัปเดต4มุม
  switch(y,x)
  if y + 1 <= 4 :
    switch(y+1, x)
  if y - 1 >= 0 :
    switch(y-1,x)
  if x + 1 <= 4 :
    switch(y,x+1)
  if x - 1 >= 0 :
    switch(y,x-1)

def drawBoard() :
  global sc
  for i in range(5): # row
    for j in range(5): # column
      sc.addch(i*2+1, j*4+1, boards[i][j])

  sc.addch(1+(curY*2), 1+(curX*4-1), '[')
  sc.addch(1+(curY*2), 1+(curX*4+1), ']')

def drawLabel() :
  global sc, move
  sc.addstr(12, 0,'Use ' + str(move)+ ' moves.')

def moveCur(key) :
  global curX, curY, sc, move
  sc.addch(1+(curY*2), 1+(curX*4-1), ' ') #print ช่องว่างแทนตำแหน่ง cursor เก่า
  sc.addch(1+(curY*2), 1+(curX*4+1), ' ') #print ช่องว่างแทนตำแหน่ง cursor เก่า
  if key == curses.KEY_LEFT and curX > 0:
      curX -= 1
  elif key == curses.KEY_RIGHT and curX < 4:
      curX += 1
  elif key == curses.KEY_UP and curY > 0:
      curY -= 1
  elif key == curses.KEY_DOWN and curY < 4:
      curY += 1
  elif key == 10: # Enter key
    move += 1
    updateBoard(curY,curX)

def winGame() :
  isAllX = True
  for i in range(5):
    for j in range(5):
      if boards[i][j] == 'O' :
        isAllX = False
  return  isAllX

def coreGame() :
  global sc, move
  running = True
  win = False
  while running :
    sc.timeout(100) #กำหนดเวลาในกาารใช้รับค่า
    key = sc.getch() #รับค่าจากkeyboard
    if key == ord('q') : #กดqเพื่อออกจากเกม
      running = False
    if key != -1 : 
      moveCur(key)
    drawBoard()
    drawLabel()
    if winGame() : 
      running = False
      win = True
  sc.refresh()
  sc.clear()
  curses.endwin()
  if win :
    print('You win in' ,str(move),'moves')

initGame()
coreGame()