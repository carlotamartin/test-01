from pywebio.output import *
from pywebio import session
put_text("Hello friend!")
put_table([
 ['Object', 'Unit'],
 ['A', '55'],
 ['B', '73'],
])
put_markdown('~~PyWebIO~~')
put_file('output_file.txt', b'You can put anything here')
put_image(open('python_logo.png', 'rb').read())
popup('popup title', 'popup text content')
session.hold()