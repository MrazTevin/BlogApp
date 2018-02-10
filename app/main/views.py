from flask.ext.login import login_required


@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
