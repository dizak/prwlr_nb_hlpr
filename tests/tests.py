"""
This module tests the functionalities of the other modules included in this
package.
"""


from unittest import TestCase


class ObjectsTests(TestCase):
    """
    Tests of the custom objects functionalities from the <objects> submodule
    """
    def setUp(self):
        """
        Set up the environment for the <objects> submodule tests
        """
        from prwlr_nb_hlpr import objects
        self.objects = objects

        self.ref_list_without = list('fooba')
        self.tes_list = list('foobar')
        self.tes_char = 'r'

    def test_without(self):
        """
        Test if listx.without method returns correct value
        """

        self.assertListEqual(
            self.objects.listx().without(self.tes_char),
            self.ref_list_without,
        )
