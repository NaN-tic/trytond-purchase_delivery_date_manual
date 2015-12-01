# This file is part of the purchase_delivery_date_manual module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class PurchaseDeliveryDateManualTestCase(ModuleTestCase):
    'Test Purchase Delivery Date Manual module'
    module = 'purchase_delivery_date_manual'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PurchaseDeliveryDateManualTestCase))
    return suite