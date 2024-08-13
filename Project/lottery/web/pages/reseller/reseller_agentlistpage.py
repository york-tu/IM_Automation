from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class AgentListPageLocator:
    # 代理列表
    agent_account_text = (By.XPATH, '//td[@data-bind="text: login"]')
    structure_level = (By.XPATH, '//td[@data-bind="text: login"]/..//span')

    # 查找條件
    agent_account = (By.XPATH, '//input[@data-bind="value: filter.login"]')
    search_btn = (By.XPATH, '//button[@id="btnSearch"]')

class AgentListPage(BasePage):
    # 找出 display 不為 none 的元素
    def get_display_element(self, element_list):
        element_displayed = []
        for element in element_list:
            if self.is_element_displayed_by_dom(element):
                element_displayed.append(element)
        
        return element_displayed

    # 檢查代理列表的所有帳號
    def check_all_account(self, account_list, agent, general_agent):
        assert self.get_text_by_dom(account_list[0]) == agent, '代理列表 > 代理帳號顯示錯誤... ' + self.get_text_by_dom(account_list[0]) + ' 應為-> ' + agent
        assert self.get_text_by_dom(account_list[1]) == general_agent, '代理列表 > 總代帳號顯示錯誤... ' + self.get_text_by_dom(account_list[1]) + ' 應為-> ' + general_agent
    
    # 檢查代理列表的所有級別
    def check_all_level(self, level_list):
        assert self.get_text_by_dom(level_list[0]) == '代理', '代理列表 > 級別顯示錯誤... ' + self.get_text_by_dom(level_list[0]) + ' 應為-> ' + '代理'
        assert self.get_text_by_dom(level_list[1]) == '总代', '代理列表 > 級別顯示錯誤... ' + self.get_text_by_dom(level_list[1]) + ' 應為-> ' + '总代'

    def check_all_agent(self, agent, general_agent):
        '''
            檢查代理列表所有帳號、級別
        '''
        self.wait_loading_finish()
        self.click(AgentListPageLocator.search_btn)
        self.wait_loading_finish()
        Account_list = self.find_elements(AgentListPageLocator.agent_account_text)
        level_list = self.find_elements(AgentListPageLocator.structure_level)
        level_list_displayed = self.get_display_element(level_list)

        assert len(Account_list) == 2, f'代理列表應顯示代理 {agent} 及總代 {general_agent} 帳號'
        self.check_all_account(Account_list, agent, general_agent)
        self.check_all_level(level_list_displayed)
        
    def check_search_agent(self, search_account):
        '''
            檢查搜尋代理的資訊
        '''
        self.type(AgentListPageLocator.agent_account, search_account)
        self.click(AgentListPageLocator.search_btn)
        self.wait_loading_finish()
        self.wait_visibility(AgentListPageLocator.agent_account_text)
        account = self.get_text(AgentListPageLocator.agent_account_text)
        assert account == search_account, '代理列表 > 帳號顯示錯誤... ' + account + ' 應為-> ' + search_account
