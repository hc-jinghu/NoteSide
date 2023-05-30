# unit testing for noteside

import unittest

from task_list import task_list
from task import task

data = ["laundry", "leetcode", "bank application", "buy the book", "grocery"]
result_dict = {}

class test_list(unittest.TestCase):
    def testData(self):
        # mannually construct a task dict
        task_counter = 0
        for d in data:
            new_task = task(task_counter, d)
            # new_task.print_task()
            result_dict.update({task_counter:new_task})
            task_counter += 1
        return result_dict
    
    def test_addTask(self):
        # Test if the list is adding task correctly
        new_list = task_list()
        for d in data:
            new_list.addTsk(d)
        result_keys = result_dict.keys()
        new_keys = new_list.collection.keys()
        self.assertEqual(result_keys, new_keys, 'Keys are not identical')

        for k in new_keys:
            element = new_list.collection.get(k).desc
            self.assertEqual(result_dict.get(k).desc, element, 'Values are not identical')


if __name__ == '__main__':
    unittest.main()
    