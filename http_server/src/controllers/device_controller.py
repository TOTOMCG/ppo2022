#! /usr/bin/env python3
from flask import request


def device_controller(*, uuid=None, request):
    print("UUID:: ", uuid)
    return "device controller"
