from flask import Flask, request, json
from onec import Http1C
import const 
import log


app = Flask(__name__)
logger = log.get()

http1c_connector = Http1C()


@app.route("/", methods=['GET'])
def ping():
    if request.headers.environ.get('HTTP_X_NGINX_PROXY') == 'true':
        logger.debug(f'Get Ping from {request.environ.get("REMOTE_ADDR")} (REAL_IP: {request.environ.get("HTTP_X_REAL_IP")})')
    else:
        logger.debug(f'Get Ping from {request.environ.get("REMOTE_ADDR")}')
    
    return "Pong"

@app.route("/1c", methods=['GET'])
def ping1c():
    response = http1c_connector.ping()
    return f'code:{response.status_code}, text1C:{response.text}'

@app.route("/", methods=['POST'])
def hook():
    data = convert_hook(request.form)
    if data['token'] == const.TOKEN:
        logger.debug("Hook TOKEN accepted")
        response = http1c_connector.send(data)
        if response.status_code == 200:
            return "ok"
        else:
            return "bad", response.status_code
    else:
        logger.warn("Wrong TOKEN. Skiped")
        return "ok"

def convert_hook(hook_data):
    id_before = hook_data.get("data[FIELDS_BEFORE][ID]")
    id_after  = hook_data.get("data[FIELDS_AFTER][ID]")

    id = []
    if id_after != None:
        id.append(id_after)
    if id_before != None and id_after != id_before:
        id.append(id_before)

    data = {
        "event"     : hook_data.get("event"),
        "id_before" : id_before,
        "id_after"  : id_after,
        "id"        : id,
        "token"     : hook_data.get("auth[application_token]"),
    }
    return data


if __name__ == "__main__":

    logger.info(f'Set Flask DEBUG mode is {const.DEBUG}')
    logger.info(f'Set listen Port is {const.PORT}')

    app.run(host="0.0.0.0", port=const.PORT, debug=const.DEBUG)
