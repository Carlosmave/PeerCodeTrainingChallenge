from libraries.common import log_message, browser
from libraries.google.google import Google
from libraries.itunes.itunes import Itunes
from config import OUTPUT_FOLDER, tabs_dict


class Process:
    def __init__(self):
        log_message("Initialization")
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_settings.popups": 0,
            "directory_upgrade": True,
            "download.default_directory": OUTPUT_FOLDER,
            "plugins.always_open_pdf_externally": True,
            "download.prompt_for_download": False
        }
        browser.open_available_browser(preferences = prefs)
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()
        google = Google(browser, {"url": "https://www.google.com/ncr"})
        google.access_google()
        self.google = google

    def start(self):
        matched_link = self.google.search_movie()
        itunes = Itunes(browser, {"url": matched_link})
        self.itunes = itunes
        self.itunes.access_itunes()
        tabs_dict["Itunes"] = len(tabs_dict)
        self.itunes.extract_artists_information()
        self.itunes.create_report()

    def finish(self):
        log_message("DW Process Finished")
        browser.close_browser()
