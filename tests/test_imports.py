from unittest import TestCase

class TestImports(TestCase):

    def setUp(self):
        pass

    def testImportFunction(self):
        from examplepackage import example_function
        
    def testImportClass(self):
        from examplepackage import ExampleClass

    def testImportMain(self):
        from examplepackage import main_function
        
