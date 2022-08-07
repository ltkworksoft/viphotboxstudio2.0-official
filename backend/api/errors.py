from backend.api import api
from flask import render_template
from backend.settings import settings


@api.app_errorhandler(403)
def forbidden():
    if settings.select_request_json_mimetype():
        response = settings.make_json_response(error='forbidden')
        response.status_code = 403
        return response
    return render_template('errors/http_errors.html', title='Accès non autorisé!', http_code=403), 403


@api.app_errorhandler(404)
def page_not_found(e):
    if settings.select_request_json_mimetype():
        response = settings.make_json_response(error='page not found')
        response.status_code = 404
        return response
    return render_template('errors/http_errors.html', title='Page non trouvée!', http_code=404), 404


@api.app_errorhandler(500)
def internal_server_error():
    if settings.select_request_json_mimetype():
        response = settings.make_json_response(error='internal server error')
        response.status_code = 500
        return response
    return render_template('errors/http_errors.html', title='Erreur interne du serveur!', http_code=500), 500
