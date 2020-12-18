from all_sql_unit_test import AllSqlUnitTest
if __name__ == '__main__':
    unittest = AllSqlUnitTest()
    unittest.get_slow_query_list()
    unittest.output_to_file_json()
