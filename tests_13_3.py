import  unittest
from module_12_2 import Runner, Tournament

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)
        self.distan = 90

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_tourne1(self):
        tourne_1 = Tournament(self.distan, self.runner_1, self.runner_3)
        result = tourne_1.start()
        self.all_results['test_tourne1'] = result

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_tourne2(self):
        tourne_2 = Tournament(self.distan, self.runner_2, self.runner_3)
        result = tourne_2.start()
        self.all_results['test_tourne2'] = result

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_tourne3(self):
        tourne_3 = Tournament(self.distan, self.runner_1, self.runner_2, self.runner_3)
        result = tourne_3.start()
        self.all_results['test_tourne3'] = result

class TestClassRunner(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_walk(self):
        a = Runner('Pavel')
        for _ in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_run(self):
        b = Runner('Sasha')
        for _ in range(10):
            b.run()
        self.assertEqual(b.distance, 100)

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_challenge(self):
        a = Runner('Даша')
        b = Runner('Паша')
        for _ in range(10):
             a.walk()
             b.run()
        self.assertNotEqual(b.distance, a.distance, 'Значения равны!')

if __name__ == '__main__':
    unittest.main()
