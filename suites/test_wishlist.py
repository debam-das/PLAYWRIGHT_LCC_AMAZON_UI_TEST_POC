from datetime import date
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from helpers import locators , constants
from pages import loginPage

@lcc.suite("Test cases for Wishlist functionality")
class test_wishlist:
    page = lcc.inject_fixture("driver")
    @lcc.test("Verify that user can not add to wishlist without logging in")
    def add_to_wishlist_without_logging_in(self):
        self.page.fill(locators.SEARCH_BOX_XPATH, constants.ITEM_TO_SEARCH)
        self.page.click(locators.SEARCH_BUTTON_XPATH)
        with self.page.expect_popup() as popup_info:
            self.page.click(locators.FIRST_SEARCH_RESULT_XPATH)
        page1 = popup_info.value
        page1.wait_for_load_state()
        lcc.log_info(page1.title())
        lcc.log_info("clicked on ADD TO WISHLIST BUTTON")
        page1.click(locators.ADD_TO_WISHLIST_BUTTON_XPATH)
        page1.wait_for_load_state()
        check_that("Title of page",page1.title(), contains_string(constants.SIGN_IN_PAGE_TITLE))
        self.page=page1
    @lcc.test("Verify that user can add to wishlist after logging in")
    def add_to_wishlist_after_logging_in(self):
        loginPage.login(self.page)

        Username=self.page.locator(locators.USERNAME_XPATH).text_content()
        check_that("username", Username, contains_string(constants.USERNAME))

        self.page.click(locators.ADD_TO_WISHLIST_BUTTON_XPATH)
        # self.page.pause()
        check_that("Success message after adding into wishlist", self.page.locator(locators.SUCCESS_MESSAGE_OF_ADDITION_INTO_WISHLIST_XPATH).text_content(), equal_to(constants.SUCCESS_MESSAGE_OF_WISHLIST_ADDITION))
        self.page.wait_for_load_state()
        elements_in_wishlist=self.page.locator(locators.TITLE_OF_ALL_ELEMENTS_XPATH)
        date_of_elements_in_wishlist=self.page.locator(locators.DATE_OF_ALL_ELEMENTS_XPATH)
        number_of_elements_in_wishlist=elements_in_wishlist.count()
        print(number_of_elements_in_wishlist)
        for i in range(number_of_elements_in_wishlist):
            element_title_in_wishlist = elements_in_wishlist.nth(i).text_content().strip()
            element_date = date_of_elements_in_wishlist.nth(i).text_content()
            lcc.log_info(element_title_in_wishlist)
            # print(element_title_in_wishlist+"-------"+element_date)
            today = date.today().strftime("%d %B %Y")
            if(elements_in_wishlist.nth(i).text_content().strip().find(constants.ITEM_NAME)):
                check_that("Title",element_title_in_wishlist.lower(),contains_string(constants.ITEM_NAME))
                check_that("Date", element_date.strip()[10:], contains_string(today) )
                check_that("index(i.e. newly wishlisted item is appearing at top)", i+1, equal_to(1))
                break
    @lcc.test("Verify that user can delete from wishlist")
    def delete_element_from_wishlist(self):
            self.page.locator("//div[@id='wl-item-view']//input[@name='submit.deleteItem']").nth(0).click()
            dict1 = {
            "deleted_item_name" : self.page.locator(locators.DELETED_ITEM_NAME_XPATH).nth(0).text_content().lower() ,
            "DeletionConfirmation" : self.page.locator(locators.DELETION_CONFIRMATION_MSG_XPATH).text_content()
                    }
            # check_that("Deleted item name", deleted_item_name.lower(), equal_to(constants.ITEM_NAME))
            check_that_in(dict1,
            "deleted_item_name", equal_to(constants.ITEM_NAME),
            "DeletionConfirmation", equal_to(constants.DELETION_CONFIRMATION_MSG)
            )
            