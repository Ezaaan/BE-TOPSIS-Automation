from django.test import TestCase
import topsisAutomation as tp

# Create your tests here.

auto = tp.TopsisAutomation("web/data/test.csv", [0.4, 0.4, 0.2], [1, 1, 1])
auto.calculateTopsis()
auto.showRanks()
