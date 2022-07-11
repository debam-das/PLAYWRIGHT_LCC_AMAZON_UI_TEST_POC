import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
from playwright.sync_api import sync_playwright
import helpers.base as base


url = base.config_reader('AMAZON_URL', 'base_url')
headless = base.config_reader('test_mode', 'headless')
screen_Recording = base.config_reader('test_mode', 'screen_record')
tracing = base.config_reader('test_mode', 'tracing')

@lcc.fixture(names=("driver", "driver_obj"), scope="session")
def setup():
    with sync_playwright() as p:
        # p5=p.devices['Pixel 5']
        if(headless.lower() == "yes"):
            browser = p.chromium.launch(channel="chrome")
            # use (.firefox.launch()) to launch firefox
            # browser = p.firefox.launch()
            # webkit to launch Safari
            # browser = p.webkit.launch()
            # Channel='msedge' to launch Edge Browser
            # browser = p.chromium.launch(channel="msedge")
        else:
            browser = p.chromium.launch(channel="chrome", headless=False)
            # use (.firefox.launch()) to launch firefox
            # browser = p.firefox.launch(headless=False)
            # webkit to launch Safari
            # browser = p.webkit.launch(headless=False)
            # Channel='msedge' to launch Edge Browser
            # browser = p.chromium.launch(channel="msedge", headless=False)
        if(screen_Recording.lower() == "yes"):
            # context = browser.new_context(**p5,record_video_dir="../videos/")
            context = browser.new_context(record_video_dir="../videos/")
        else:
            context = browser.new_context()
        if(tracing.lower() == "yes"):
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
        else:
            pass
        # Open new page
        page = context.new_page()
        page.goto(url)
        # loginPage.login(page)
        yield page
        if(tracing.lower() == "yes"):
            context.tracing.stop(path = "trace.zip")
        else:
            pass
        context.close()
        browser.close()