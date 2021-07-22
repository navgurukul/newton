```ngMeta
analyzing-the-screenshot_key1
```

analyzing-the-screenshot_key2
analyzing-the-screenshot_key3


analyzing-the-screenshot_key4


```python
   >>> import pyautogui
   >>> im = pyautogui.screenshot()
❶ >>> im.getpixel((50, 200))
```
analyzing-the-screenshot_key5
```python
❷ >>> pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
```
analyzing-the-screenshot_key6
```python
❸ >>> pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))
```
analyzing-the-screenshot_key7
