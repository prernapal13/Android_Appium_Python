from appium.webdriver.common.mobileby import MobileBy

class HomePage:
    xpath_home_page_header = '//*[contains(@resource-id,"text1")]'
    home_page_header_text = "What movies do you like to watch more?"
    xpath_hindi = '//*[contains(@resource-id,"tv_one")]'


class VideoPage:
    xpath_signup_popup = '//*[contains(@resource-id, "tv_button_text")]'
    xpath_title = '//*[contains(@resource-id, "tv_spotlight_title")]'
    xpath_play_button = '//*[contains(@resource-id,"v_detail_play")]/android.widget.ImageView'
    xpath_video_frame = '//*[contains(@resource-id,"viusdk_video_frame")]'
    xpath_play_next_video = '//*[contains(@resource-id,"title_text_next_recommonded")]'
    xpath_video_loading = '//*[contains(@resource-id,"video_player_loading_text")]'

