import pytest                                                    #For testing Infopy
from tkinter import Tk                                           #For GUI
from Infopy import Process, Generate_QR, saving, Save            #Importing Infopy file to test

#Defining test_app: used for creating temprory test file
@pytest.fixture
def test_app():
    app = Tk()
    yield app
    app.destroy()

#Testing Generate_QR Function
def test_generate_qr():
    text = "Test Text"
    Generate_QR(text)
    
    assert Generate_QR(text) == True

#Testing Saving Function
def test_saving():
    file_path = "test_image.png"
    result = saving(file_path)

    assert "Image saved as" in result

#Testing Process Function
def test_process(test_app):
    text = "Test Text"
    process_result = Process(text, test_app)
    
    assert process_result == True

#Testing Save Function
def test_save(test_app):
    assert Save() == True

#Calling main Function
if __name__ == "__main__":
    pytest.main()