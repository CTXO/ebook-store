import json

from flask import Flask, jsonify
from flask import request
from flask import redirect

app = Flask(__name__)
print("TESTING PRINT")
services = []


@app.route('/', methods=['GET'])
def entrypoint():
    account_service = next((s for s in services if s['name'] == 'account_service'), None)
    full_url = f'{account_service.get("url")}:{account_service.get("port")}'
    return redirect(full_url)


@app.route('/register', methods=['POST'])
def register_service():
    # Store the service information
    post_data = request.form
    service = next((s for s in services if s['name'] == post_data.get('service_name')), None)
    if service:
        return jsonify({'success': False, 'message': 'A service with this name is already registered'})
    services.append({'name': post_data.get('service_name'), 'url': post_data.get('service_url'),
                     'port': post_data.get('service_port')})
    return jsonify({'success': True})


@app.route('/services', methods=['GET'])
def list_services():
    return jsonify({'services': services})


@app.route('/service/<service_name>', methods=['GET'])
def get_service(service_name):
    service = next((s for s in services if s['name'] == service_name), None)
    if service is None:
        return jsonify({'error': 'Service not found'}), 404
    return jsonify({'service': service})


@app.route('/route/<service_name>/<path>', methods=['GET'])
def route_service(service_name, path):
    service = next((s for s in services if s['name'] == service_name), None)
    if service is None:
        return jsonify({'error': 'Service not found'}), 404
    userid = request.args.get('userid', '')
    redirect_url = service['url'] + ':' + service['port'] + '/' + path + '?userid=' + userid
    import logging
    logging.exception(redirect_url)
    return redirect(redirect_url, code=303)
