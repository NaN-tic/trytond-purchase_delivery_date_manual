# This file is part of the purchase_delivery_date_manual module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import purchase


def register():
    Pool.register(
        purchase.PurchaseLine,
        module='purchase_delivery_date_manual', type_='model')
