# Login page
USER_NAME_XPATH = "//input[@type='email']"
CONTINUE_BUTTON_XPATH = "//input[@id='continue']"
PASSWORD_XPATH = "//input[@type='password']"
SUBMIT_BUTTON_XPATH = "//input[@id='signInSubmit']"

# Home Page
SEARCH_BOX_XPATH = "//input[@aria-label='Search']"
SEARCH_BUTTON_XPATH = "//input[@id='nav-search-submit-button']"
USERNAME_XPATH = "//span[@id='nav-link-accountList-nav-line-1']"

# Search result page
# sometimes top serach result can be search_result_2 due to ads, change FIRST_SEARCH_RESULT_XPATH locator as per requirement
FIRST_SEARCH_RESULT_XPATH = "//div[@data-cel-widget='search_result_1']"
FIRST_SEARCH_RESULT_XPATH = FIRST_SEARCH_RESULT_XPATH + "//div[@class='a-section a-spacing-none s-padding-right-small s-title-instructions-style']//child::h2//span"

# Item Page
ADD_TO_WISHLIST_BUTTON_XPATH = "//div[@id='wishlistButtonStack']"
# ADD_TO_WISHLIST_BUTTON_CSS = "span[role='radio']:has-text('Add to Wish List')"

# Wishlist page
SUCCESS_MESSAGE_OF_ADDITION_INTO_WISHLIST_XPATH = "//div[@id='addToListSuccess']//h4"
TITLE_OF_ALL_ELEMENTS_XPATH = "//div[@id='wl-item-view']//a[contains(@id,'itemName')]"
DATE_OF_ALL_ELEMENTS_XPATH = "//div[@id='wl-item-view']//span[contains(@id,'itemAddedDate')]"
DELETED_ITEM_NAME_XPATH = "//span[@class='a-list-item']//div[@class='a-row a-spacing-none']"
DELETION_CONFIRMATION_MSG_XPATH = "//span[@class='a-list-item']//div[@class='a-row a-spacing-none']//div[text()='Deleted']"