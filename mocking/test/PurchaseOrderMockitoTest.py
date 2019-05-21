
import unittest

from mockito import mock, when, verify

from PurchaseOrder import PurchaseOrder
from Store import Store


class TestMethods(unittest.TestCase):

    def test_should_buy_remove_the_product_in_the_store_if_there_are_enough_items(self):
        # Creating the mock object
        store:Store = mock()

        # Stubbing
        when(store).are_there_enough_products("Bread", 15).thenReturn(True)

        # Execute
        purchase_order:PurchaseOrder = PurchaseOrder("Bread", 15)
        purchase_order.buy(store)

        # Verify
        verify(store).remove_products("Bread", 15)
        verify(store, times=0).remove_products("Chicken", 12)

    def test_should_buy_not_remove_the_product_in_the_store_if_there_are_not_enough_items(self):
        # Creating the mock object
        store:Store = mock()

        # Stubbing
        when(store).are_there_enough_products("Bread", 15).thenReturn(False)

        # Execute
        purchase_order:PurchaseOrder = PurchaseOrder("Bread", 15)
        purchase_order.buy(store)

        # Verify
        verify(store, times=0).remove_products("Bread", 15)

    def test_shouldBuyWorkIfThereAreProductsTheFirstTimeButNotTheSeconeOne(self):
        # Creating the mock object
        store:Store = mock()

        # Stubbing
        when(store).are_there_enough_products("Bread", 15).thenReturn(True, False)

        # Execute
        purchase_order:PurchaseOrder = PurchaseOrder("Bread", 15)
        purchase_order.buy(store)
        purchase_order.buy(store)

        # Verify
        verify(store, times=2).are_there_enough_products("Bread", 15)
        verify(store, times=1).remove_products("Bread", 15)

