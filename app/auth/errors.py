from flask import render_template
from . import auth

@auth.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('404.html'),404