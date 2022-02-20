#! /usr/bin/env python3
import os
import argparse
from flask import request
import controllers
from providers import app_provider
from config import CFG


class HTTPServer:

    def __get_ssl_context(self):
        abspath = os.path.dirname(os.path.abspath(__file__))
        crt = os.path.join(abspath, "..", "ssl", "system.crt")
        key = os.path.join(abspath, "..", "ssl", "system.key")
        return crt, key

    def __init__(self):
        self._app = app_provider

        @self._app.route("/sign-up", methods=["POST", "GET"])
        def sign_up():
            return controllers.signup_controller(request=request)

        @self._app.route("/user", methods=["GET"])
        def get_user():
            return controllers.user_controller(request=request)

        @self._app.route("/user/<uuid>", methods=["GET"])
        def get_get_user(uuid):
            return controllers.user_controller(uuid=uuid, request=request)

        @self._app.route("/sign-in", methods=["POST", "GET"])
        def sign_in():
            return controllers.login_controller(request=request)

        @self._app.route("/device", methods=["GET"])
        def get_device():
            return controllers.device_controller(request=request)

        @self._app.route("/device/<uuid>", methods=["GET"])
        def get_device_by_uuid(uuid):
            return controllers.device_controller(uuid=uuid, request=request)

    def run(self):
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument("--port", action="store",
                            dest="port", default=CFG["flask"]["port"])
        parser.add_argument("--debug", action="store_true",
                            dest="debug", default=CFG["flask"])
        args = parser.parse_args()
        try:
            PORT = int(args.port)
        except Exception:
            PORT = 9999
        IS_DEBUG_MODE = args.debug

        self._app.run(
            port=PORT,
            debug=IS_DEBUG_MODE,
            ssl_context=self.__get_ssl_context()
        )


if __name__ == "__main__":
    HTTPServer().run()
