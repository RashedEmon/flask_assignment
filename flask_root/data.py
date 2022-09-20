#Related third party imports.
from werkzeug.security import generate_password_hash
#Local application specific imports.
from flask_root.models import User

users = [
    User('rashedul',generate_password_hash('rashedul@islam')),
    User('johndoe',generate_password_hash('john@doe')),
    User('khalidbinwalid',generate_password_hash('khalid@walid'))
]


todos = [
        {
        'id': '1',
        'title': 'Learn python',
        'status': 'Ongoing' 
        },
        {
        'id': '2',
        'title': 'Learn Nodejs',
        'status': 'Completed'
        },
        {
        'id': '3',
        'title': 'Learn Flask',
        'status': 'Ongoing' 
        },
    ]

