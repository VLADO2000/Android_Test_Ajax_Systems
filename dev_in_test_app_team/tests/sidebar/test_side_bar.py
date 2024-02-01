import pytest

sidebar_locator_pathes = [
    '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App Settings"]',
    '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Help"]',
]

def test_hubAdd_exists(homehub_fixture):
    assert (homehub_fixture.assert_add_hub_button())

def test_sidebar_elements_correctness(homehub_fixture):
    homehub_fixture.click_side_menu_bar()
    list_sidebar = homehub_fixture.find_elements_list(locator='//android.view.View[@resource-id="com.ajaxsystems:id/atomImage"]', 
                                                      locator_type='xpath')
    
    assert len(list_sidebar) == 3

def test_accessibility_of_menu_options(homehub_fixture):
    homehub_fixture.click_side_menu_bar()
    for loc in sidebar_locator_pathes:
        homehub_fixture.click_menu_bar_elem_sequentialy(loc)

    

