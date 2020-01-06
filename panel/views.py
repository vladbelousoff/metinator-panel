# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.shortcuts import render

from panel.models import Character


def index(request):
    context = {'characters': Character.objects.all()}
    return render(request, 'index.html', context)


def info(request):
    if request.method == 'GET':
        return HttpResponse('ok')
    if request.method == 'POST':
        body = json.loads(request.body)

        for character_info in body['info']:
            defaults = {
                'hostname': character_info['hostname'],
                'yang': character_info['player_elk'],
            }

            character, created = Character.objects.update_or_create(
                name=character_info['player_name'], defaults=defaults)

        return HttpResponse('ok')
