import unittest

from mastermind.infrastructure.context.context import Context


class ContextAwareTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.context = Context()
        self.clean_database()

    def tearDown(self):
        super().tearDown()
        self.context.tear_down()

    def clean_database(self):
        records = self.context.database.query(
            """show full tables where Table_Type = 'BASE TABLE'"""
        ).all()
        for record in records:
            table_name = record[0]
            self.context.database.query("""TRUNCATE TABLE `{}`""".format(table_name))
