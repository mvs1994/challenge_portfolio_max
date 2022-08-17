from pages.base_page import BasePage


class LoginPage(BasePage):
    sign_out_button_xpath = "//*[@id='sign out']"
    players_button_xpath = "//*[@id='players']"
    scouts_panel_field_xpath = "//*['Scouts Panel']"
    // *[text() = "Events count"]
    // *[text() = "Reports count"]
    // *[text() = "Matches count"]
    // *[text() = "Players count"]
    // *[text() = "Shortcuts"]
    // *[text() = "Activity"]
 // *[text() = "Tester Tester"]