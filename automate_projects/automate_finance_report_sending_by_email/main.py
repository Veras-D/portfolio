import pyautogui
from time import sleep
import pyperclip
import fundamentus

df = fundamentus.get_resultado()
filtro = df[(df.pl > 5) & (df.dy > 0.07) & (df.mrgebit > 0.4)]
filtro.sort_values('dy', ascending = False, inplace = True)

pyautogui.PAUSE = 0.1
pyautogui.press('winleft')
pyperclip.copy('Google Chrome')

pyperclip.paste()
# pyautogui.write('Google Chrome')
pyautogui.press('enter')
sleep(2)
pyperclip.copy('https://docs.google.com/spreadsheets/u/0/')
pyperclip.paste()
# pyautogui.write("https://docs.google.com/spreadsheets/u/0/", interval=0.1)
pyautogui.press('enter')
pyautogui.moveTo(432,383)
pyautogui.click()
sleep(1)
pyautogui.write('papel', interval=0.1)
pyautogui.press('tab')

for column in filtro.columns:
    pyautogui.write(column)
    pyautogui.press('tab')

pyautogui.press('enter')
pyautogui.press('enter')

for index, row in filtro.iterrows():
    pyautogui.write(index)
    pyautogui.press('tab')
    
    pyautogui.write(str(row['cotacao']))
    pyautogui.press('tab')
    
    pyautogui.write(str(row['pl']))
    pyautogui.press('tab')
    
    pyautogui.write(str(row['pvp']))
    pyautogui.press('tab')
    
    pyautogui.write(str(row['psr']))
    pyautogui.press('tab')
    
    pyautogui.write(str(row['dy']))
    pyautogui.press('tab')
    
    pyautogui.write(str(row['pa']))
    pyautogui.press('tab')

    pyautogui.write(str(row['pcg']))
    pyautogui.press('tab')
    
    pyautogui.write(str(row['pebit']))
    pyautogui.press('tab')
    
    pyautogui.write(str(row['pacl']))
    pyautogui.press('tab')
    
    pyautogui.write(str(row['evebit']))
    pyautogui.press('tab')

    pyautogui.write(str(row['evebitda']))
    pyautogui.press('tab')

    pyautogui.write(str(row['mrgebit']))
    pyautogui.press('tab')

    pyautogui.write(str(row['mrgliq']))
    pyautogui.press('tab')

    pyautogui.write(str(row['roic']))
    pyautogui.press('tab')
    
    pyautogui.write(str(row['roe']))
    pyautogui.press('tab')
    
    pyautogui.write(str(row['liqc']))
    pyautogui.press('tab')

    pyautogui.write(str(row['liq2m']))
    pyautogui.press('tab')

    pyautogui.write(str(row['patrliq']))
    pyautogui.press('tab')

    pyautogui.write(str(row['divbpatr']))
    pyautogui.press('tab')

    pyautogui.write(str(row['c5y']))
    pyautogui.press('tab')
    
    pyautogui.press('enter')
    pyautogui.press('enter')


pyautogui.moveTo(64,197)
pyautogui.click()

pyautogui.moveTo(144,433)
pyautogui.moveTo(422,447)
pyautogui.click()

pyautogui.moveTo(768,520)
pyautogui.click()

pyperclip.copy('dveras2310@gmail.com')
pyperclip.paste()
pyautogui.press('enter')

pyautogui.moveTo(910,661)
pyautogui.click()

pyperclip.copy('Monthly Financial Report')
pyperclip.paste()

pyautogui.moveTo(804,755)
pyautogui.click()

pyautogui.moveTo(820,834)
pyautogui.click()

pyautogui.moveTo(1154,822)
pyautogui.click()

pyautogui.moveTo(38,134)
pyautogui.click()

pyautogui.moveTo(387,325)
pyautogui.click()