# verify models are created correctly
from django.test import TestCase
from django.db import models

from gpus.models import GPU


class GPUTestCase(TestCase):
    def test_set_up(self):
        # Set up non-modified objects used by all test methods
        GPU.objects.create(url="url", alias="alias")

    def testURLMaxLength(self):
        gpu = GPU.objects.create(url="url", alias="alias")
        max_length = gpu._meta.get_field('url').max_length
        self.assertEqual(max_length, 512)

    def testAliasMaxLength(self):
        gpu = GPU.objects.create(url="url", alias="alias")
        max_length = gpu._meta.get_field('alias').max_length
        self.assertEqual(max_length, 512)

    # def testManufacturerMaxLength(self):
    #     gpu = GPU.objects.create(url="url", alias="alias")
    #     max_length = gpu._meta.get_field('manufacturer').max_length
    #     self.assertEqual(max_length, 256)
    #
    # def testBrandMaxLength(self):
    #     gpu = GPU.objects.create(url="url", alias="alias")
    #     max_length = gpu._meta.get_field('brand').max_length
    #     self.assertEqual(max_length, 256)
    #
    # def testUniqueness(self):
    #     g1 = GPU.objects.create(unique=True)
    #     g2 = GPU.objects.create(unique=True)
    #     self.assertNotEquals(g1, g2)
