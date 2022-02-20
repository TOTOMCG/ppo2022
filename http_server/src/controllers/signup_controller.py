from flask import make_response


def signup_controller(*, request):
    if request.headers.get("X-ACCESS-TOKEN") is None:
        return make_response({"error": {"message": "Unauthorized"}}, 401)

    if request.headers.get("Content-Type") == "application/json":
        return
    elif request.headers.get("Content-Type") == "multipart/form-data":
        return
    else:
        return make_response("TEST", 400)
    return "sign up"
