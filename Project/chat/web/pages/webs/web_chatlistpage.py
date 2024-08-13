from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
from Project.chat.web.pages.webs.web_loginpage import LoginPageLocator


class ChatListPageLocator:
    menu_icon = (By.XPATH, "//div[@class='menu-icon']/div")
    system_message = (By.XPATH, "(//p[@class='wcr-system-message__text'])[last()]")
    menu_arrow = (By.XPATH, "//div[@class='chat-list__item -active']//div[@class='menu-arrow']")
    delete_text = (By.XPATH, "//div[@class='menu-list']//div[@class='menu-icon -icon-trash']")
    confirm_submit = (By.XPATH, "//button[@class='btn btn-danger btn-md']")

    chat_list = (By.XPATH, "//p[@class='chat-list__name__text']")
    chat_list_first = (By.XPATH, "(//p[@class='chat-list__name__text'])[1]")
    chat_list_msg = (By.XPATH, "//p[@class='chat-list__msg__text']")
    chat_list_msg_first = (By.XPATH, "(//p[@class='chat-list__msg__text'])[1]")

    chat_room_title = (By.XPATH, "//p[@class='chat-detail__name__text']")
    chat_room_last_msg = (By.XPATH, "(//div[@class='wcr-list__msg']//span[1])[last()]")

    @staticmethod
    def chat_room_locator(text):
        locator = (By.XPATH, f"//div[@class='chat-list']//p[text()='{text}']")
        return locator


class ChatListPage(BasePage):
    def into_chat_room(self, name):
        self.refresh_browser()
        self.wait_login_finish()
        self.click(LoginPageLocator.model_btn)
        self.wait_login_finish()
        for _ in range(0, 3):
            if self.is_element_finded(ChatListPageLocator.chat_room_locator(name)) is True:
                self.click(ChatListPageLocator.chat_room_locator(name))
                break
            else:
                self.sleep(0.5)
                self.scroll_to_element(ChatListPageLocator.chat_room_locator(name))

        assert self.get_text(ChatListPageLocator.chat_room_title) == name, f"進入聊天室有誤"

    def check_last_message(self):
        self.sleep(0.5)
        room_last_msg = self.get_text(ChatListPageLocator.chat_room_last_msg)
        list_last_msg = self.get_text(ChatListPageLocator.chat_list_msg_first)

        assert room_last_msg == list_last_msg, f"列表最後一筆訊息有誤 應為: {room_last_msg} 顯示為: {list_last_msg}"

    def get_chat_list_msg_text(self):
        return self.get_text(ChatListPageLocator.chat_list_msg_first)

    def check_group_build(self, user_id, name):
        self.wait_loading_finish()

        system_message = self.get_text(ChatListPageLocator.system_message)
        message = user_id + '已建立「' + name + '」群组'
        assert system_message == message, f"列表最後一筆訊息有誤 應為: {system_message} 顯示為: {message}"

    def delete_chatroom_record(self):
        self.click(ChatListPageLocator.menu_arrow)
        self.click(ChatListPageLocator.delete_text)
        self.click(ChatListPageLocator.confirm_submit)
        self.wait_loading_finish()