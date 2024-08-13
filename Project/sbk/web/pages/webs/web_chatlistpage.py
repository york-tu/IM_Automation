from xml.sax.xmlreader import Locator
from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
import os,random, re

class ChatListPageLocator:
	menu_icon = (By.XPATH, "//div[@class='menu-icon']/div")
	system_message = (By.XPATH, "(//p[@class='wcr-system-message__text'])[last()]")

	chat_list = (By.XPATH, "//p[@class='chat-list__name__text']")
	chat_list_frist = (By.XPATH, "(//p[@class='chat-list__name__text'])[1]")
	chat_list_msg = (By.XPATH, "//p[@class='chat-list__msg__text']")
	chat_list_msg_frist = (By.XPATH, "(//p[@class='chat-list__msg__text'])[1]")

	chat_room_title = (By.XPATH, "//p[@class='chat-detail__name__text']")
	chat_room_last_msg = (By.XPATH, "(//div[@class='wcr-list__msg']//span[1])[last()]")

	def chat_room_locator(self, text):
		locator = (By.XPATH, f"//div[@class='chat-list']//p[text()='{text}']")
		return locator

class ChatListPage(BasePage):
	def into_chat_room(self, name):
		self.wait_login_finish()
		for _ in range(0, 3):
			if self.is_element_finded(ChatListPageLocator.chat_room_locator(self, name)) == True:
				self.click(ChatListPageLocator.chat_room_locator(self, name))
			else:
				self.sleep(0.5)
				self.scroll_to_element(ChatListPageLocator.chat_room_locator(self, name))

			assert self.get_text(ChatListPageLocator.chat_room_title) == name , f"進入聊天室有誤"

	def check_last_message(self):
		self.sleep(0.5)
		room_last_msg = self.get_text(ChatListPageLocator.chat_room_last_msg)
		list_last_msg = self.get_text(ChatListPageLocator.chat_list_msg_frist)

		assert room_last_msg == list_last_msg , f"列表最後一筆訊息有誤 應為: {room_last_msg} 顯示為: {list_last_msg}"
	
	def check_group_build(self, user_id, name):
		self.wait_loading_finish()

		system_message = self.get_text(ChatListPageLocator.system_message)
		message = user_id + '已建立「' + name + '」群组' 
		assert system_message == message , f"列表最後一筆訊息有誤 應為: {system_message} 顯示為: {message}"
