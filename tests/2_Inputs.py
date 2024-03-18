from streamlit.testing.v1 import AppTest

at = AppTest.from_file("pages/2_Inputs.py")
at.run()


def test_welcoming_text():
    at.radio("build_state").set_value("Beta").run()
    at.text_input("name").input("Test").run()
    at.button[0].click().run()
    assert at.success[0].value == "Welcome aboard **Test** on Beta version!"


test_welcoming_text()
