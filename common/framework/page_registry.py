# -*- coding: utf-8 -*-
"""
頁面註冊配置
定義各專案的頁面註冊配置，便於統一管理
"""
from typing import Dict, Dict as DictType

# Chat 專案的頁面配置
CHAT_WEB_PAGES: DictType[str, str] = {
    'common_page': 'common.web.common.Common',
    'base_page': 'Project.chat.web.pages.webs.web_basepage.BasePage',
    'main_page': 'Project.chat.web.pages.webs.web_mainpage.MainPage',
    'login_page': 'Project.chat.web.pages.webs.web_loginpage.LoginPage',
    'integral_page': 'Project.chat.web.pages.webs.web_integralpage.IntegralPage',
    'notification_page': 'Project.chat.web.pages.webs.web_notificationpage.NotificationPage',
    'security_page': 'Project.chat.web.pages.webs.web_securitypage.SecurityPage',
    'black_page': 'Project.chat.web.pages.webs.web_blackpage.BlackPage',
    'share_page': 'Project.chat.web.pages.webs.web_sharepage.SharePage',
    'about_page': 'Project.chat.web.pages.webs.web_aboutpage.AboutPage',
    'friend_page': 'Project.chat.web.pages.webs.web_friendpage.FriendPage',
    'chatroom_page': 'Project.chat.web.pages.webs.web_chatroompage.ChatRoomPage',
    'chatlist_page': 'Project.chat.web.pages.webs.web_chatlistpage.ChatListPage',
    'brand_page': 'Project.chat.web.pages.webs.web_brandpage.BrandPage',
}

CHAT_ADMIN_PAGES: DictType[str, str] = {
    'common_page': 'common.web.common.Common',
    'base_page': 'Project.chat.web.pages.admin.admin_basepage.BasePage',
    'login_page': 'Project.chat.web.pages.admin.admin_loginpage.LoginPage',
    'main_page': 'Project.chat.web.pages.admin.admin_mainpage.MainPage',
    'groups_page': 'Project.chat.web.pages.admin.admin_groupspage.GroupsPage',
    'logging_page': 'Project.chat.web.pages.admin.admin_loggingpage.LoggingPage',
    'member_page': 'Project.chat.web.pages.admin.admin_memberpage.MemberPage',
    'recode_page': 'Project.chat.web.pages.admin.admin_recodepage.RecordPage',
    'red_envelope_page': 'Project.chat.web.pages.admin.admin_redenvelopepage.RedEnvelopePage',
    'water_recode_page': 'Project.chat.web.pages.admin.admin_water_recode_page.WaterRecodePage',
    'water_control_page': 'Project.chat.web.pages.admin.admin_water_control_page.WaterControlPage',
    'setting_page': 'Project.chat.web.pages.admin.admin_settingpage.SettingPage',
    'system_page': 'Project.chat.web.pages.admin.admin_systempage.SystemPage',
    'social_management_page': 'Project.chat.web.pages.admin.admin_social_management_page.SocialManagementPage',
    'record_page': 'Project.chat.web.pages.admin.admin_recodepage.RecordPage',
}

CHAT_WAP_PAGES: DictType[str, str] = {
    'common_page': 'common.web.common.Common',
    'base_page': 'Project.chat.web.pages.wap.wap_basepage.BasePage',
    'wap_first_page': 'Project.chat.web.pages.wap.wap_firstpage.FirstPage',
    'wap_friends_page': 'Project.chat.web.pages.wap.wap_friendspage.FriendsPage',
    'wap_message_page': 'Project.chat.web.pages.wap.wap_messagepage.MessagePage',
    'wap_main_page': 'Project.chat.web.pages.wap.wap_mainpage.MainPage',
    'wap_main_personal_page': 'Project.chat.web.pages.wap.wap_main_personal_settings.PersonalSettingPage',
    'wap_login_page': 'Project.chat.web.pages.wap.wap_loginpage.LoginPage',
    'search_page': 'Project.chat.web.pages.wap.wap_searchpage.SearchPage',
}
CHAT_WEB2_PAGES: DictType[str, str] = {
    'common_page': 'common.web.common.Common',
    'base_page': 'Project.chat.web.pages.web2.web2_basepage.BasePage',
    'web2_first_page': 'Project.chat.web.pages.web2.web2_firstpage.FirstPage',
    'web2_main_page': 'Project.chat.web.pages.web2.web2_mainpage.MainPage',
    'web2_login_page': 'Project.chat.web.pages.web2.web2_loginpage.LoginPage',
    'web2_search_page': 'Project.chat.web.pages.web2.web2_searchpage.SearchPage',
    'web2_social_page': 'Project.chat.web.pages.web2.web2_socialpage.SocialPage',
}
CHAT_APP_PAGES: DictType[str, str] = {
    'common_page': 'common.app.common.Common',
    'base_page': 'Project.chat.app.pages.base_page.Base',
    'main_page': 'Project.chat.app.pages.main_page.MainPage',
    'chatroom_page': 'Project.chat.app.pages.chatroom_page.ChatRoomPage',
    'chatlist_page': 'Project.chat.app.pages.chatlist_page.ChatListPage',
    'member_page': 'Project.chat.app.pages.member_page.MemberPage',
    'friend_page': 'Project.chat.app.pages.friend_page.FriendPage',
    'about_page': 'Project.chat.app.pages.about_page.AboutPage',
    'share_page': 'Project.chat.app.pages.share_page.SharePage',
    'blacklist_page': 'Project.chat.app.pages.blacklist_page.BlackListPage',
    'security_page': 'Project.chat.app.pages.security_page.SecurityPage',
    'privacy_page': 'Project.chat.app.pages.privacy_page.PrivacyPage',
    'chatsetup_page': 'Project.chat.app.pages.chatsetup_page.ChatSetupPage',
    'notification_page': 'Project.chat.app.pages.notification_page.NotificationPage',
    'point_page': 'Project.chat.app.pages.point_page.PointPage',
    'socialhome_page': 'Project.chat.app.pages.social_home_page.SocialHomePage',
    'socialmediapost_page': 'Project.chat.app.pages.social_media_post_page.SocialMediaPostPage',
    'socialmedialibrary_page': 'Project.chat.app.pages.social_media_library_page.SocialMediaLibraryPage',
    'socialshare_page': 'Project.chat.app.pages.social_share_page.SocialSharePage',
    'socialsearch_page': 'Project.chat.app.pages.social_search_page.SocialSearchPage',
    'discover_pages': 'Project.chat.app.pages.discover_page.DiscoverPage',
    'freeupspace_page': 'Project.chat.app.pages.free_up_space_page.FreeUpSpacePage',
}

# SBK 專案的頁面配置（已移除，不再使用）
# SBK_WEB_PAGES: DictType[str, str] = { ... }
# SBK_ADMIN_PAGES: DictType[str, str] = { ... }

# Exchange WellPay 專案的頁面配置
EXCHANGE_WELLPAY_APP_PAGES: DictType[str, str] = {
    'common_page': 'common.app.common.Common',
    'main_page': 'Project.exchange_wellpay.app.pages.app.app_main_page.MainPage',
    'register_page': 'Project.exchange_wellpay.app.pages.app.app_register_page.RegisterPage',
    'wantbuy_page': 'Project.exchange_wellpay.app.pages.app.app_want_buy_page.WantBuyPage',
    'deposit_page': 'Project.exchange_wellpay.app.pages.app.app_deposit_page.DepositPage',
    'customerservice_page': 'Project.exchange_wellpay.app.pages.app.app_customer_service_page.CustomerServicePage',
    'bindpayment_page': 'Project.exchange_wellpay.app.pages.app.app_bind_payment_page.BindPaymentPagePage',
    'my_page': 'Project.exchange_wellpay.app.pages.app.app_my_page.MyPage',
    'graporder_page': 'Project.exchange_wellpay.app.pages.app.app_grap_order_page.GrapOrderPage',
    'myorder_page': 'Project.exchange_wellpay.app.pages.app.app_my_order_page.MyOrderPage',
    'mysell_page': 'Project.exchange_wellpay.app.pages.app.app_my_sell_page.MySellPage',
    'myinfo_page': 'Project.exchange_wellpay.app.pages.app.app_my_info_page.MyInfoPage',
    'wantsell_page': 'Project.exchange_wellpay.app.pages.app.app_want_sell_page.WantSellPage',
    'payinfo_page': 'Project.exchange_wellpay.app.pages.app.app_pay_info_page.PayInfoPage',
    'depositrecord_page': 'Project.exchange_wellpay.app.pages.app.app_deposit_record_page.DepositRecordPage',
}

EXCHANGE_WELLPAY_ADMIN_PAGES: DictType[str, str] = {
    'common_page': 'common.web.common.Common',
    'login_page': 'Project.exchange_wellpay.app.pages.admin.admin_login_page.LoginPage',
    'menu_page': 'Project.exchange_wellpay.app.pages.admin.admin_menu_page.MenuPage',
    'rechargeaudit_page': 'Project.exchange_wellpay.app.pages.admin.rechargemanagement.admin_recharge_audit_page.RechargeAuditPage',
    'orderrecordbrand_page': 'Project.exchange_wellpay.app.pages.admin.buymanagement.admin_order_record_brand_page.OrderRecordBrandPage',
    'allrecordzqb_page': 'Project.exchange_wellpay.app.pages.admin.sellmanagement.admin_all_record_zqb_page.AllRecordZqbPage',
    'memberlist_page': 'Project.exchange_wellpay.app.pages.admin.membermanagement.admin_member_list_page.MemberListPage',
    'systemmanagement_page': 'Project.exchange_wellpay.app.pages.admin.systemmanagement.admin_system_management_page.SystemManagementPage',
}

# Mynah 專案的頁面配置（使用 snake_case，同時支援 camelCase 別名）
MYNAH_WEB_PAGES: DictType[str, str] = {
    # snake_case 命名（PEP 8 標準）
    'web_base_page': 'Project.mynah.pages.web.webs_basepage.WebBasePage',
    'channel_page': 'Project.mynah.pages.web.web_channelpage.WebChannelPage',
    'chat_page': 'Project.mynah.pages.web.web_chatpage.WebChatPage',
    'form_page': 'Project.mynah.pages.web.web_formpage.WebFormPage',
    'score_page': 'Project.mynah.pages.web.web_scorepage.WebScorePage',
    # camelCase 別名（向後兼容）
    'webBasePage': 'Project.mynah.pages.web.webs_basepage.WebBasePage',
    'channelPage': 'Project.mynah.pages.web.web_channelpage.WebChannelPage',
    'chatPage': 'Project.mynah.pages.web.web_chatpage.WebChatPage',
    'formPage': 'Project.mynah.pages.web.web_formpage.WebFormPage',
    'scorePage': 'Project.mynah.pages.web.web_scorepage.WebScorePage',
}

MYNAH_ADMIN_PAGES: DictType[str, str] = {
    # snake_case 命名（PEP 8 標準）
    'admin_base_page': 'Project.mynah.pages.admin.admin_basepage.AdminBasePage',
    'admin_chat_page': 'Project.mynah.pages.admin.admin_chatpage.AdminChatPage',
    'admin_form_page': 'Project.mynah.pages.admin.admin_formpage.AdminFormPage',
    'admin_ai_response_page': 'Project.mynah.pages.admin.admin_airesponsepage.AdminAIResponsePage',
    'admin_menu_page': 'Project.mynah.pages.admin.admin_menupage.AdminMenuPage',
    'admin_rules_page': 'Project.mynah.pages.admin.admin_rulespage.AdminRulesPage',
    'admin_history_page': 'Project.mynah.pages.admin.admin_historypage.AdminHistoryPage',
    'admin_promotion_ad_page': 'Project.mynah.pages.admin.admin_promotionadpage.AdminPromotionAdPage',
    'admin_score_page': 'Project.mynah.pages.admin.admin_scorepage.AdminScorePage',
    'admin_statistics_page': 'Project.mynah.pages.admin.admin_statistics.AdminStatisticsPage',
    # camelCase 別名（向後兼容）
    'adminBasePage': 'Project.mynah.pages.admin.admin_basepage.AdminBasePage',
    'adminChatPage': 'Project.mynah.pages.admin.admin_chatpage.AdminChatPage',
    'adminFormPage': 'Project.mynah.pages.admin.admin_formpage.AdminFormPage',
    'adminAIResponsePage': 'Project.mynah.pages.admin.admin_airesponsepage.AdminAIResponsePage',
    'adminMenuPage': 'Project.mynah.pages.admin.admin_menupage.AdminMenuPage',
    'adminRulesPage': 'Project.mynah.pages.admin.admin_rulespage.AdminRulesPage',
    'adminHistoryPage': 'Project.mynah.pages.admin.admin_historypage.AdminHistoryPage',
    'adminPromotionAdPage': 'Project.mynah.pages.admin.admin_promotionadpage.AdminPromotionAdPage',
    'adminScorePage': 'Project.mynah.pages.admin.admin_scorepage.AdminScorePage',
    'adminStatisticsPage': 'Project.mynah.pages.admin.admin_statistics.AdminStatisticsPage',
}

# 頁面配置映射表
PAGE_CONFIGS: DictType[str, DictType[str, str]] = {
    'chat.web': CHAT_WEB_PAGES,
    'chat.admin': CHAT_ADMIN_PAGES,
    'chat.wap': CHAT_WAP_PAGES,
    'chat.web2': CHAT_WEB2_PAGES,
    'chat.app': CHAT_APP_PAGES,
    # 'sbk.web': SBK_WEB_PAGES,  # 已移除，不再使用
    # 'sbk.admin': SBK_ADMIN_PAGES,  # 已移除，不再使用
    'exchange_wellpay.app': EXCHANGE_WELLPAY_APP_PAGES,
    'exchange_wellpay.admin': EXCHANGE_WELLPAY_ADMIN_PAGES,
    'mynah.web': MYNAH_WEB_PAGES,
    'mynah.admin': MYNAH_ADMIN_PAGES,
}


def get_page_config(project: str, page_type: str) -> DictType[str, str]:
    """
    獲取指定專案和類型的頁面配置
    
    Args:
        project: 專案名稱（如 'chat', 'sbk'）
        page_type: 頁面類型（如 'web', 'admin', 'app', 'wap'）
        
    Returns:
        Dict[str, str]: 頁面配置字典
        
    Raises:
        KeyError: 如果配置不存在
    """
    config_key = f"{project}.{page_type}"
    if config_key not in PAGE_CONFIGS:
        raise KeyError(
            f"Page config '{config_key}' not found. "
            f"Available configs: {list(PAGE_CONFIGS.keys())}"
        )
    return PAGE_CONFIGS[config_key]


def register_pages_to_factory(factory: 'PageFactory', project: str, page_type: str):
    """
    將頁面配置註冊到工廠
    
    Args:
        factory: PageFactory 實例
        project: 專案名稱
        page_type: 頁面類型
    """
    config = get_page_config(project, page_type)
    factory.register_from_dict(config)

