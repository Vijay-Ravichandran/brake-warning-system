import unittest
import logging
logging.basicConfig(filename="test_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")
loader = unittest.TestLoader()
suite = loader.discover(".", pattern = "test_*.py")
runner = unittest.TextTestRunner()
result = runner.run(suite)
logging.info("Tests Run: %d", result.testsRun)
logging.info("Failures: %d", len(result.failures))
logging.info("ERRORS: %d", len(result.errors))