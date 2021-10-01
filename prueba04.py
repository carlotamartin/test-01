from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
def app():
    put_markdown('# Professional Info')
#group all the inputs to make a form
data = input_group("Basic info",[
    input('Input your name', name='name', required=True),
    checkbox("Languages of choice", ['JAVA', 'Python', 'C', 'C++'], name='loc'),
    select("Experience", ['0 - 1', '1 - 2', '2+'], name='yoe', required=True),
    radio("Gender", options=['Male', 'Female', 'Other'],name='gndr', required=True),
    textarea('Tell something about yourself', rows=3, name='abt', required=True),
    file_upload('Profile Image',placeholder='Choose file',accept='image/*',name='dp',
    required=True)
    ])
    # main function
if __name__ == '__main__':
    start_server(app, port=32420, debug=True)