# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="dfsfsadfaffa", header="dsfdgsdagsa", footer="ggdasgasgs"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

