# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

__version__ = "3.1.1"


def console(*data):
    frappe.publish_realtime("toconsole", data, user=frappe.session.user)
