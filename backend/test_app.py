import unittest
from app import health_check

class TestBackendApp(unittest.TestCase):
    def test_health_check_returns_healthy(self):
        """This test passes if our health_check function returns 'Healthy'"""
        self.assertEqual(health_check(), "Healthy")

if __name__ == '__main__':
    unittest.main()
