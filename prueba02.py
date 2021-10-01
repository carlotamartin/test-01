from pywebio.input import *

input("This is a simple text input")
select("This is a drop down menu", ['Option1', 'Option2'])
checkbox("Multiple Choices!", options=["a",'b','c','d'])
radio("Select any one", options=['1', '2', '3'])
textarea('Text Area', rows=3, placeholder='Multiple line text input')