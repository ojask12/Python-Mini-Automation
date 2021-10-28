import pyautogui as pg
import time
print("wait till it loads don't switch windows")

long_pause = 5
short_pause = 3
two_s_pause = 1
click_pause = 1

time.sleep(long_pause)
print("time up")


pg.press('tab')
time.sleep(click_pause)
pg.press('tab')
time.sleep(click_pause)
pg.press('enter')           #account selected
time.sleep(short_pause)


pg.press('tab')
time.sleep(click_pause)
pg.press('tab')
time.sleep(click_pause)
pg.press('enter')           #show advanced
time.sleep(two_s_pause)


pg.press('tab')
time.sleep(click_pause)
pg.press('tab')
time.sleep(click_pause)
pg.press('tab')
time.sleep(click_pause)
pg.press('enter')           #continue to savePCData
time.sleep(short_pause)


pg.press('tab')
time.sleep(click_pause)
pg.press('enter')           #Allowed access dialog
time.sleep(short_pause)


pg.press('tab')
time.sleep(click_pause)
pg.press('tab')
time.sleep(click_pause)
pg.press('tab')
time.sleep(click_pause)
pg.press('tab')
time.sleep(click_pause)
pg.press('tab')
time.sleep(click_pause)
pg.press('enter')           #final allow click
time.sleep(short_pause)

print ("Auth flow completed")
pg.keyDown('ctrl')
pg.press('w')               #close chrome tab
pg.keyUp('ctrl')            
time.sleep(click_pause)              

pg.keyDown('alt')
pg.press('tab')
time.sleep(click_pause)
pg.press('tab')             #cmd window in focus
pg.keyUp('alt')
