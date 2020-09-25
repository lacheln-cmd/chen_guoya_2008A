import pytest
@pytest.fixture(scope="class") # 作用域
def aa():
    print("fixture函数被运行了")
    return 11

@pytest.fixture(autouse=True) # 作用域
def bb():
    print("fixture函数被git运行了")
    return 11

test_fixture_1.py

class Test111():
    def test_aa(self):
        print(111)
    def test_bb(self):
        print(111)

class Test222():
    def test_aa(self):
        print(11)
    def test_bb(self):
        print(111)

test_fixture_2.py

class Test111():
    def test_aa(self):
        print(111)
    def test_bb(self):
        print(111)

class Test222():
    def test_aa(self):
        print(11)
    def test_bb(self):
        print(111)