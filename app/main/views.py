from flask_login import login_required
from . import main


@main.route('/blog/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_blog(id):
    return 'Only authenticated users are allowed!'
