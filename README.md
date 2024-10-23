# Chinese notes app XML render app

This app can render XML files which was created by the package called  ```com.seewo.easinote``` on android.


## Features

- Render XML
- Save figure to image
- Rerender the figure periodically 

## How to use

1. Clone the project
2. Install the dependencies
3. In the  ```notesrender.py``` file change the ```xml_path``` variable to that path, where the ```.xml``` file(s) are stored
4. Run ```notesrender.py```

### Optional
- If you are using macOS remove the line ```root.attributes('-toolwindow', True)```
- If you want to change the rerender frequency, change the interval in this line: ```ani = FuncAnimation(fig, update, interval=1000)```
