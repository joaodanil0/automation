from src.appium.Appium import ExampleAppium

def test_02():
    
    test = ExampleAppium()
    test.setUp()
    test.test_find_battery()
    test.tearDown()

