from typing import Any

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.test import Client


class demo_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        path = ["NoteApp", "demo"]
        for _ in path:
            if request.path == f"/{_}/" and "email1" not in request.session:
                return redirect("/login/")

        return response
