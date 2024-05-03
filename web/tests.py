from django.test import TestCase
import web.topsisAutomation as tp
import json

# Create your tests here.

class TopsisAutomationTest(TestCase):
    def test_topsis_automation(self):
        auto = tp.TopsisAutomation("web/data/test.csv", [0.4, 0.4, 0.2], [1, 1, 1])
        auto.calculateTopsis()
        ranks = json.loads(auto.showRanks())
        expected_ranks = {
            "social_media": [
                {
                "rank": 1,
                "name": "line",
                "score": 0.9379817959542858
                },
                {
                "rank": 2,
                "name": "instagram",
                "score": 0.910704627622589
                },
                {
                "rank": 3,
                "name": "whatsapp",
                "score": 0.903709955153027
                },
                {
                "rank": 4,
                "name": "youtube",
                "score": 0.9007106408039649
                },
                {
                "rank": 5,
                "name": "twitter",
                "score": 0.7091911321570389
                },
                {
                "rank": 6,
                "name": "teams",
                "score": 0.639943943574992
                },
                {
                "rank": 7,
                "name": "linkedin",
                "score": 0.5017968419999169
                },
                {
                "rank": 8,
                "name": "discord",
                "score": 0.4929566649878376
                },
                {
                "rank": 9,
                "name": "tiktok",
                "score": 0.4445355452107081
                },
                {
                "rank": 10,
                "name": "telegram",
                "score": 0.38272360362912194
                },
                {
                "rank": 11,
                "name": "pinterest",
                "score": 0.37784389775877014
                },
                {
                "rank": 12,
                "name": "facebook",
                "score": 0.2198899069644733
                },
                {
                "rank": 13,
                "name": "messenger",
                "score": 0.11465712478167116
                },
                {
                "rank": 14,
                "name": "snapchat",
                "score": 0.10277858127690336
                },
                {
                "rank": 15,
                "name": "reddit",
                "score": 0.08626657015857178
                },
                {
                "rank": 16,
                "name": "threads",
                "score": 0.07411113888371275
                },
                {
                "rank": 17,
                "name": "slack",
                "score": 0.04721059593332495
                }
            ]
        }

        self.assertEqual(ranks, expected_ranks)




