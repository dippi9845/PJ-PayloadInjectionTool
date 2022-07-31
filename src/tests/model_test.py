import unittest
from ..PJ.model.variable import Variable, FixedVariable, InjectableVariable


class TestUrl(unittest.TestCase):
    def test1(self):
        pass

    def test2(self):
        pass


class VaraibleTest(unittest.TestCase):
    
    VAR_NAME = "var name test"
    PROTOCOL = "PROTOCOL"
    CONTENT = "caio"

    def test_get_varaible(self):
        var = Variable(self.VAR_NAME)
        self.assertEqual(var.get_variable_name(), self.VAR_NAME, "name should be " + self.VAR_NAME)

        var = Variable(self.VAR_NAME, protocol=self.PROTOCOL)
        self.assertEqual(var.get_protocol(), self.PROTOCOL,  "protocol should be " + self.PROTOCOL)

        var = Variable(self.VAR_NAME, protocol=self.PROTOCOL, content=self.CONTENT)
        self.assertEqual(var.get_content(), self.CONTENT,  "content should be " + self.CONTENT)

    def test_from_dict_single(self):
        var_dict = {self.VAR_NAME : self.CONTENT}
        var = Variable.from_dict(var_dict)

        self.assertEqual(var.get_variable_name(), self.VAR_NAME, "name should be " + self.VAR_NAME)
        self.assertEqual(var.get_content(), self.CONTENT,  "content should be " + self.CONTENT)
    
    def test_from_dict_multiple(self):
        second_name = "second name"
        second_content = "second content"

        var_dict = {self.VAR_NAME : self.CONTENT, second_name : second_content}
        var = Variable.from_dict(var_dict)

        self.assertEqual(type(var), list, "Should be a list")

        self.assertEqual(var[0].get_variable_name(), self.VAR_NAME, "name should be " + self.VAR_NAME)
        self.assertEqual(var[0].get_content(), self.CONTENT,  "content should be " + self.CONTENT)

        self.assertEqual(var[1].get_variable_name(), second_name, "name should be " + second_name)
        self.assertEqual(var[1].get_content(), second_content,  "content should be " + second_content)

    def test_fixed(self):
        var = FixedVariable.from_variable(Variable(self.VAR_NAME, content=self.CONTENT))
        var.inject("bla bla")
        self.assertEqual(var.get_content(), self.CONTENT)


    def test_injectable(self):
        pass

if __name__ == "__main__":
    unittest.main()
    input()