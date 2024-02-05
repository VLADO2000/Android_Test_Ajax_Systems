import pytest



def test_hub_add_exists(homehub_fixture):
    add_hub_btn = homehub_fixture.get_add_new_hub_btn()
    assert (homehub_fixture.is_element_displayed(element=add_hub_btn))

def test_sidebar_elements_correctness(homehub_fixture):
    side_menu_bar = homehub_fixture.get_side_menu_bar()
    homehub_fixture.click_element(element=side_menu_bar)
    list_sidebar = homehub_fixture.get_sidebar_list()
    
    assert len(list_sidebar) == 3
    

