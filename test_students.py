import unittest
from student import Student

class TestStudent(unittest.TestCase):

    @classmethod 
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownlass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_email(self):

        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_alert_santa(self):
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

if __name__ == '__main__':
    unittest.main()