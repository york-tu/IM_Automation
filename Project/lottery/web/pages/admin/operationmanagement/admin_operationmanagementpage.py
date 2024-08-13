from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class OperationManagementPageLocator:
    # ------------運維管理分類------------
    menu_operation_management = (By.XPATH, "//span[text()='运维管理']")
    # *注單中心
    menu_order_center = (By.XPATH, "//span[text()='注单中心']/..")
    ok_point_order_center = (By.XPATH, "//span[@class='el-breadcrumb__inner']//a[contains(text(), '注单中心')]")
    # *即時注單
    menu_instant_order_center = (By.XPATH, "//span[text()='即时注单']/..")
    ok_point_instant_order_center = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '即时注单')]")

    # *外接平台
    menu_external_planform_operation = (By.XPATH, "//span[text()='运维管理']/../..//span[text()='外接平台']/..")
    menu_gamelist = (By.XPATH, "//span[text()='游戏列表']")
    ok_gamelist = (By.XPATH, "//ul[@class='page-breadcrumb']//*[contains(text(), '游戏列表')]")
    menu_channel_setting = (By.XPATH, "//span[text()='频道设置']")
    ok_channel_setting = (By.XPATH, "//ul[@class='page-breadcrumb']//*[contains(text(), '频道设置')]")
    menu_replenishment_management = (By.XPATH, "//span[text()='补单管理']")
    ok_replenishment_management = (By.XPATH, "//ul[@class='page-breadcrumb']//*[contains(text(), '补单管理')]")

    # menu_external_planform_ag = (By.XPATH, "//li[@permission-id='ops.cm.ag']")                                                                           # AG
    # menu_external_planform_ag_channel_setting = (By.XPATH, "//span[text()='AG']/../..//span[text()='频道设置']/../..")                             # AG -> 頻道設定
    # ok_point_external_planform_ag_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='AG']/../..//*[text()='频道设置']")
    # menu_external_planform_ag_video = (By.XPATH, "//span[text()='AG-视讯']/..")                                                                # AG -> AG-視訊
    # menu_external_planform_ag_video_game_list = (By.XPATH, "//span[text()='AG-视讯']/../..//span[text()='游戏列表']/..")                        # AG -> AG-視訊 -> 遊戲列表
    # menu_external_planform_ag_video_replenishment_management = (By.XPATH, "//span[text()='AG-视讯']/../..//span[text()='补单管理']/..")         # AG -> AG-視訊 -> 補單管理
    # ok_point_external_planform_ag_video_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='AG-视讯']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_ag_video_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='AG-视讯']/../..//*[text()='补单管理']")
    # menu_external_planform_ag_electronics = (By.XPATH, "//span[text()='AG-电子']/..")                                                          # AG -> AG-電子
    # menu_external_planform_ag_electronics_game_list = (By.XPATH, "//span[text()='AG-电子']/../..//span[text()='游戏列表']/..")                  # AG -> AG-電子 -> 遊戲列表
    # menu_external_planform_ag_electronics_replenishment_management = (By.XPATH, "//span[text()='AG-电子']/../..//span[text()='补单管理']/..")   # AG -> AG-電子 -> 補單管理
    # ok_point_external_planform_ag_electronics_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='AG-电子']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_ag_electronics_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='AG-电子']/../..//*[text()='补单管理']")
    # menu_external_planform_ag_fishing = (By.XPATH, "//span[text()='AG-捕鱼']/..")                                                              # AG -> AG-捕魚
    # menu_external_planform_ag_fishing_game_list = (By.XPATH, "//span[text()='AG-捕鱼']/../..//span[text()='游戏列表']/..")                      # AG -> AG-捕魚 -> 遊戲列表
    # menu_external_planform_ag_fishing_replenishment_management = (By.XPATH, "//span[text()='AG-捕鱼']/../..//span[text()='补单管理']/..")       # AG -> AG-捕魚 -> 補單管理
    # ok_point_external_planform_ag_fishing_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='AG-捕鱼']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_ag_fishing_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='AG-捕鱼']/../..//*[text()='补单管理']")

        
    # menu_external_planform_bbin = (By.XPATH, "//li[@permission-id='ops.cm.bbin']")                                                                         # BBIN
    # menu_external_planform_bbin_channel_setting = (By.XPATH, "//span[text()='BBIN']/../..//span[text()='频道设置']/../..")                          # BBIN -> 頻道設定
    # ok_point_external_planform_bbin_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='BBIN']/../..//*[text()='频道设置']")
    # menu_external_planform_bbin_fishing = (By.XPATH, "//span[text()='BBIN-捕鱼']/..")                                                            # BBIN -> BBIN-捕鱼
    # menu_external_planform_bbin_fishing_game_list = (By.XPATH, "//span[text()='BBIN-捕鱼']/../..//span[text()='游戏列表']/..")                    # BBIN -> BBIN-捕鱼 -> 遊戲列表
    # menu_external_planform_bbin_fishing_replenishment_management = (By.XPATH, "//span[text()='BBIN-捕鱼']/../..//span[text()='补单管理']/..")     # BBIN -> BBIN-捕鱼 -> 補單管理
    # ok_point_external_planform_bbin_fishing_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='BBIN-捕鱼']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_bbin_fishing_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='BBIN-捕鱼']/../..//*[text()='补单管理']")
    # menu_external_planform_bbin_electronics = (By.XPATH, "//span[text()='BBIN-电子']/..")                                                        # BBIN -> BBIN-电子
    # menu_external_planform_bbin_electronics_game_list = (By.XPATH, "//span[text()='BBIN-电子']/../..//span[text()='游戏列表']/..")                # BBIN -> BBIN-电子 -> 遊戲列表
    # menu_external_planform_bbin_electronics_replenishment_management = (By.XPATH, "//span[text()='BBIN-电子']/../..//span[text()='补单管理']/..") # BBIN -> BBIN-电子 -> 補單管理
    # ok_point_external_planform_bbin_electronics_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='BBIN-电子']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_bbin_electronics_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='BBIN-电子']/../..//*[text()='补单管理']")
    # menu_external_planform_bbin_video = (By.XPATH, "//span[text()='BBIN-视讯']/..")                                                              # BBIN -> BBIN-视讯
    # menu_external_planform_bbin_video_game_list = (By.XPATH, "//span[text()='BBIN-视讯']/../..//span[text()='游戏列表']/..")                      # BBIN -> BBIN-视讯 -> 遊戲列表
    # menu_external_planform_bbin_video_replenishment_management = (By.XPATH, "//span[text()='BBIN-视讯']/../..//span[text()='补单管理']/..")       # BBIN -> BBIN-视讯 -> 補單管理
    # ok_point_external_planform_bbin_video_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='BBIN-视讯']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_bbin_video_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='BBIN-视讯']/../..//*[text()='补单管理']")
    # menu_external_planform_bbin_sport = (By.XPATH, "//span[text()='BBIN-体育']/..")                                                              # BBIN -> BBIN-体育
    # menu_external_planform_bbin_sport_game_list = (By.XPATH, "//span[text()='BBIN-体育']/../..//span[text()='游戏列表']/..")                      # BBIN -> BBIN-体育 -> 遊戲列表
    # menu_external_planform_bbin_sport_replenishment_management = (By.XPATH, "//span[text()='BBIN-体育']/../..//span[text()='补单管理']/..")       # BBIN -> BBIN-体育 -> 補單管理
    # ok_point_external_planform_bbin_sport_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='BBIN-体育']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_bbin_sport_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='BBIN-体育']/../..//*[text()='补单管理']")
        

    # menu_external_planform_cq = (By.XPATH, "//li[@permission-id='ops.cm.cq']")                                                                            # CQ
    # menu_external_planform_cq_channel_setting = (By.XPATH, "//span[text()='CQ']/../..//span[text()='频道设置']/../..")                              # CQ -> 頻道設定
    # ok_point_external_planform_cq_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='CQ']/../..//*[text()='频道设置']")
    # menu_external_planform_cq_electronics = (By.XPATH, "//span[text()='CQ9-电子']/..")                                                           # CQ -> CQ9-电子
    # menu_external_planform_cq_electronics_game_list = (By.XPATH, "//span[text()='CQ9-电子']/../..//span[text()='游戏列表']/..")                  # CQ -> CQ9-电子 -> 遊戲列表
    # menu_external_planform_cq_electronics_replenishment_management = (By.XPATH, "//span[text()='CQ9-电子']/../..//span[text()='补单管理']/..")   # CQ -> CQ9-电子 -> 補單管理
    # ok_point_external_planform_cq_electronics_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='CQ9-电子']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_cq_electronics_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='CQ9-电子']/../..//*[text()='补单管理']")
    # menu_external_planform_cq_fishing = (By.XPATH, "//span[text()='CQ9-捕鱼']/..")                                                               # CQ -> CQ9-捕鱼
    # menu_external_planform_cq_fishing_game_list = (By.XPATH, "//span[text()='CQ9-捕鱼']/../..//span[text()='游戏列表']/..")                       # CQ -> CQ9-捕鱼 -> 遊戲列表
    # menu_external_planform_cq_fishing_replenishment_management = (By.XPATH, "//span[text()='CQ9-捕鱼']/../..//span[text()='补单管理']/..")        # CQ -> CQ9-捕鱼 -> 補單管理
    # ok_point_external_planform_cq_fishing_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='CQ9-捕鱼']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_cq_fishing_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='CQ9-捕鱼']/../..//*[text()='补单管理']")


    # menu_external_planform_dt = (By.XPATH, "//li[@permission-id='ops.cm.dt']")                                                                             # DT
    # menu_external_planform_dt_channel_setting = (By.XPATH, "//span[text()='DT']/../..//span[text()='频道设置']/../..")                               # DT -> 頻道設定
    # ok_point_external_planform_dt_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='DT']/../..//*[text()='频道设置']")
    # menu_external_planform_dt_electronics = (By.XPATH, "//span[text()='DT-电子']/..")                                                            # DT -> DT-电子
    # menu_external_planform_dt_electronics_game_list = (By.XPATH, "//span[text()='DT-电子']/../..//span[text()='游戏列表']/..")                    # DT -> DT-电子 -> 遊戲列表
    # menu_external_planform_dt_electronics_replenishment_management = (By.XPATH, "//span[text()='DT-电子']/../..//span[text()='补单管理']/..")     # DT -> DT-电子 -> 補單管理
    # ok_point_external_planform_dt_electronics_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='DT-电子']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_dt_electronics_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='DT-电子']/../..//*[text()='补单管理']")

        
    # menu_external_planform_fg = (By.XPATH, "//li[@permission-id='ops.cm.fg']")                                                                            # FG
    # menu_external_planform_fg_channel_setting = (By.XPATH, "//span[text()='FG']/../..//span[text()='频道设置']/../..")                              # FG -> 頻道設定
    # ok_point_external_planform_fg_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='FG']/../..//*[text()='频道设置']")
    # menu_external_planform_fg_chess = (By.XPATH, "//span[text()='FG-棋牌']/..")                                                                 # FG -> FG-棋牌
    # menu_external_planform_fg_chess_game_list = (By.XPATH, "//span[text()='FG-棋牌']/../..//span[text()='游戏列表']/..")                         # FG -> FG-棋牌 -> 遊戲列表
    # menu_external_planform_fg_chess_replenishment_management = (By.XPATH, "//span[text()='FG-棋牌']/../..//span[text()='补单管理']/..")          # FG -> FG-棋牌 -> 補單管理
    # ok_point_external_planform_fg_chess_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='FG-棋牌']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_fg_chess_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='FG-棋牌']/../..//*[text()='补单管理']")
    # menu_external_planform_fg_electronics = (By.XPATH, "//span[text()='FG-电子']/..")                                                           # FG -> FG-电子
    # menu_external_planform_fg_electronics_game_list = (By.XPATH, "//span[text()='FG-电子']/../..//span[text()='游戏列表']/..")                   # FG -> FG-电子 -> 遊戲列表
    # menu_external_planform_fg_electronics_replenishment_management = (By.XPATH, "//span[text()='FG-电子']/../..//span[text()='补单管理']/..")    # FG -> FG-电子 -> 補單管理
    # ok_point_external_planform_fg_electronics_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='FG-电子']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_fg_electronics_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='FG-电子']/../..//*[text()='补单管理']")

        
    # menu_external_planform_gc = (By.XPATH, "//li[@permission-id='ops.cm.gc']")                                                                       # GC
    # menu_external_planform_gc_channel_setting = (By.XPATH, "//span[text()='GC']/../..//span[text()='频道设置']/../..")                         # GC -> 頻道設定
    # ok_point_external_planform_gc_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='GC']/../..//*[text()='频道设置']")
    # menu_external_planform_gc_video = (By.XPATH, "//span[text()='GC-视讯']/..")                                                             # GC -> GC-视讯
    # menu_external_planform_gc_video_game_list = (By.XPATH, "//span[text()='GC-视讯']/../..//span[text()='游戏列表']/..")                    # GC -> GC-视讯 -> 遊戲列表
    # menu_external_planform_gc_video_replenishment_management = (By.XPATH, "//span[text()='GC-视讯']/../..//span[text()='补单管理']/..")     # GC -> GC-视讯 -> 補單管理
    # ok_point_external_planform_gc_video_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='GC-视讯']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_gc_video_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='GC-视讯']/../..//*[text()='补单管理']")

        
    # menu_external_planform_gm = (By.XPATH, "//li[@permission-id='ops.cm.gm']")                                                                       # GM
    # menu_external_planform_gm_channel_setting = (By.XPATH, "//span[text()='GM']/../..//span[text()='频道设置']/../..")                         # GM -> 頻道設定
    # ok_point_external_planform_gm_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='GM']/../..//*[text()='频道设置']")
    # menu_external_planform_gm_chess = (By.XPATH, "//span[text()='GM-棋牌']/..")                                                             # GM -> GM-棋牌
    # menu_external_planform_gm_chess_game_list = (By.XPATH, "//span[text()='GM-棋牌']/../..//span[text()='游戏列表']/..")                    # GM -> GM-棋牌 -> 遊戲列表
    # menu_external_planform_gm_chess_replenishment_management = (By.XPATH, "//span[text()='GM-棋牌']/../..//span[text()='补单管理']/..")     # GM -> GM-棋牌 -> 補單管理
    # ok_point_external_planform_gm_chess_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='GM-棋牌']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_gm_chess_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='GM-棋牌']/../..//*[text()='补单管理']")

        
    # menu_external_planform_ky = (By.XPATH, "//li[@permission-id='ops.cm.ky']")                                                                       # KY
    # menu_external_planform_ky_channel_setting = (By.XPATH, "//span[text()='KY']/../..//span[text()='频道设置']/..")                         # KY -> 頻道設定
    # ok_point_external_planform_ky_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='KY']/../..//*[text()='频道设置']")
    # menu_external_planform_ky_chess = (By.XPATH, "//span[text()='开元棋牌']/..")                                                            # KY -> 开元棋牌
    # menu_external_planform_ky_chess_game_list = (By.XPATH, "//span[text()='开元棋牌']/../..//span[text()='游戏列表']/..")                    # KY -> 开元棋牌 -> 遊戲列表
    # menu_external_planform_ky_chess_replenishment_management = (By.XPATH, "//span[text()='开元棋牌']/../..//span[text()='补单管理']/..")     # KY -> 开元棋牌 -> 補單管理
    # ok_point_external_planform_ky_chess_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='开元棋牌']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_ky_chess_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='开元棋牌']/../..//*[text()='补单管理']")

        
    # menu_external_planform_lc = (By.XPATH, "//li[@permission-id='ops.cm.lc']")                                                                       # LC
    # menu_external_planform_lc_channel_setting = (By.XPATH, "//span[text()='LC']/../..//span[text()='频道设置']/../..")                         # LC -> 頻道設定
    # ok_point_external_planform_lc_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='LC']/../..//*[text()='频道设置']")
    # menu_external_planform_lc_chess = (By.XPATH, "//span[text()='龙城棋牌']/..")                                                            # LC -> 龙城棋牌
    # menu_external_planform_lc_chess_game_list = (By.XPATH, "//span[text()='龙城棋牌']/../..//span[text()='游戏列表']/..")                    # LC -> 龙城棋牌 -> 遊戲列表
    # menu_external_planform_lc_chess_replenishment_management = (By.XPATH, "//span[text()='龙城棋牌']/../..//span[text()='补单管理']/..")     # LC -> 龙城棋牌 -> 補單管理
    # ok_point_external_planform_lc_chess_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='龙城棋牌']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_lc_chess_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='龙城棋牌']/../..//*[text()='补单管理']")

        
    # menu_external_planform_mg = (By.XPATH, "//li[@permission-id='ops.cm.mg']")                                                                          # MG
    # menu_external_planform_mg_channel_setting = (By.XPATH, "//span[text()='MG']/../..//span[text()='频道设置']/../..")                            # MG -> 頻道設定
    # ok_point_external_planform_mg_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='MG']/../..//*[text()='频道设置']")
    # menu_external_planform_mg_video = (By.XPATH, "//span[text()='MG-视讯']/..")                                                                # MG -> MG-视讯
    # menu_external_planform_mg_video_game_list = (By.XPATH, "//span[text()='MG-视讯']/../..//span[text()='游戏列表']/..")                        # MG -> MG-视讯 -> 遊戲列表
    # menu_external_planform_mg_video_replenishment_management = (By.XPATH, "//span[text()='MG-视讯']/../..//span[text()='补单管理']/..")         # MG -> MG-视讯 -> 補單管理
    # ok_point_external_planform_mg_video_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='MG-视讯']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_mg_video_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='MG-视讯']/../..//*[text()='补单管理']")
    # menu_external_planform_mg_electronics = (By.XPATH, "//span[text()='MG-电子']/..")                                                          # MG -> MG-电子
    # menu_external_planform_mg_electronics_game_list = (By.XPATH, "//span[text()='MG-电子']/../..//span[text()='游戏列表']/..")                  # MG -> MG-电子 -> 遊戲列表
    # menu_external_planform_mg_electronics_replenishment_management = (By.XPATH, "//span[text()='MG-电子']/../..//span[text()='补单管理']/..")   # MG -> MG-电子 -> 補單管理
    # ok_point_external_planform_mg_electronics_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='MG-电子']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_mg_electronics_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='MG-电子']/../..//*[text()='补单管理']")

        
    # menu_external_planform_pt = (By.XPATH, "//li[@permission-id='ops.cm.pt']")                                                                           # PT
    # menu_external_planform_pt_channel_setting = (By.XPATH, "//span[text()='PT']/../..//span[text()='频道设置']/../..")                            # PT -> 頻道設定
    # ok_point_external_planform_pt_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='PT']/../..//*[text()='频道设置']")
    # menu_external_planform_pt_electronics = (By.XPATH, "//span[text()='PT-电子']/..")                                                          # PT -> PT-电子
    # menu_external_planform_pt_electronics_game_list = (By.XPATH, "//span[text()='PT-电子']/../..//span[text()='游戏列表']/..")                  # PT -> PT-电子 -> 遊戲列表
    # menu_external_planform_pt_electronics_replenishment_management = (By.XPATH, "//span[text()='PT-电子']/../..//span[text()='补单管理']/..")   # PT -> PT-电子 -> 補單管理
    # ok_point_external_planform_pt_electronics_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='PT-电子']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_pt_electronics_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='PT-电子']/../..//*[text()='补单管理']")
    # menu_external_planform_pt_fishing = (By.XPATH, "//span[text()='PT-捕鱼']/..")                                                              # PT -> PT-捕鱼
    # menu_external_planform_pt_fishing_game_list = (By.XPATH, "//span[text()='PT-捕鱼']/../..//span[text()='游戏列表']/..")                      # PT -> PT-捕鱼 -> 遊戲列表
    # menu_external_planform_pt_fishing_replenishment_management = (By.XPATH, "//span[text()='PT-捕鱼']/../..//span[text()='补单管理']/..")       # PT -> PT-捕鱼 -> 補單管理
    # ok_point_external_planform_pt_fishing_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='PT-捕鱼']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_pt_fishing_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='PT-捕鱼']/../..//*[text()='补单管理']")

        
    # menu_external_planform_sb = (By.XPATH, "//li[@permission-id='ops.cm.sb']")                                                                                     # SB
    # menu_external_planform_sb_channel_setting = (By.XPATH, "//span[text()='SB']/../..//span[text()='频道设置']/../..")                                      # SB -> 頻道設定
    # ok_point_external_planform_sb_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='SB']/../..//*[text()='频道设置']")
    # menu_external_planform_sb_virtual_sport_two = (By.XPATH, "//span[text()='SB-虚拟体育2']/..")                                                         # SB -> SB-虚拟体育2
    # menu_external_planform_sb_virtual_sport_two_game_list = (By.XPATH, "//span[text()='SB-虚拟体育2']/../..//span[text()='游戏列表']/..")                 # SB -> SB-虚拟体育2 -> 遊戲列表
    # menu_external_planform_sb_virtual_sport_two_replenishment_management = (By.XPATH, "//span[text()='SB-虚拟体育2']/../..//span[text()='补单管理']/..")  # SB -> SB-虚拟体育2 -> 補單管理
    # ok_point_external_planform_sb_virtual_sport_two_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-虚拟体育2']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_sb_virtual_sport_two_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-虚拟体育2']/../..//*[text()='补单管理']")
    # menu_external_planform_sb_virtual_sport = (By.XPATH, "//span[text()='SB-虚拟体育']/..")                                                               # SB -> SB-虚拟体育
    # menu_external_planform_sb_virtual_sport_game_list = (By.XPATH, "//span[text()='SB-虚拟体育']/../..//span[text()='游戏列表']/..")                      # SB -> SB-虚拟体育 -> 遊戲列表
    # menu_external_planform_sb_virtual_sport_replenishment_management = (By.XPATH, "//span[text()='SB-虚拟体育']/../..//span[text()='补单管理']/..")        # SB -> SB-虚拟体育 -> 補單管理
    # ok_point_external_planform_sb_virtual_sport_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-虚拟体育']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_sb_virtual_sport_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-虚拟体育']/../..//*[text()='补单管理']")
    # menu_external_planform_sb_sport = (By.XPATH, "//span[text()='SB-体育']/..")                                                                          # SB -> SB-体育
    # menu_external_planform_sb_sport_game_list = (By.XPATH, "//span[text()='SB-体育']/../..//span[text()='游戏列表']/..")                                  # SB -> SB-体育 -> 遊戲列表
    # menu_external_planform_sb_sport_replenishment_management = (By.XPATH, "//span[text()='SB-体育']/../..//span[text()='补单管理']/..")                   # SB -> SB-体育 -> 補單管理
    # ok_point_external_planform_sb_sport_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-体育']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_sb_sport_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-体育']/../..//*[text()='补单管理']")
    # menu_external_planform_sb_practice = (By.XPATH, "//span[text()='SB-百练赛']/..")                                                                     # SB -> SB-百练赛
    # menu_external_planform_sb_practice_game_list = (By.XPATH, "//span[text()='SB-百练赛']/../..//span[text()='游戏列表']/..")                            # SB -> SB-百练赛 -> 遊戲列表
    # menu_external_planform_sb_practice_replenishment_management = (By.XPATH, "//span[text()='SB-百练赛']/../..//span[text()='补单管理']/..")              # SB -> SB-百练赛 -> 補單管理
    # ok_point_external_planform_sb_practice_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-百练赛']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_sb_practice_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-百练赛']/../..//*[text()='补单管理']")
    # menu_external_planform_sb_fishing = (By.XPATH, "//span[text()='SB-捕鱼']/..")                                                                        # SB -> SB-捕鱼
    # menu_external_planform_sb_fishing_game_list = (By.XPATH, "//span[text()='SB-捕鱼']/../..//span[text()='游戏列表']/..")                               # SB -> SB-捕鱼 -> 遊戲列表
    # menu_external_planform_sb_fishing_replenishment_management = (By.XPATH, "//span[text()='SB-捕鱼']/../..//span[text()='补单管理']/..")                # SB -> SB-捕鱼 -> 補單管理
    # ok_point_external_planform_sb_fishing_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-捕鱼']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_sb_fishing_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-捕鱼']/../..//*[text()='补单管理']")
    # menu_external_planform_sb_electronics = (By.XPATH, "//span[text()='SB-电子']/..")                                                                   # SB -> SB-电子
    # menu_external_planform_sb_electronics_game_list = (By.XPATH, "//span[text()='SB-电子']/../..//span[text()='游戏列表']/..")                           # SB -> SB-电子 -> 遊戲列表
    # menu_external_planform_sb_electronics_replenishment_management = (By.XPATH, "//span[text()='SB-电子']/../..//span[text()='补单管理']/..")            # SB -> SB-电子 -> 補單管理
    # ok_point_external_planform_sb_electronics_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-电子']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_sb_electronics_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SB-电子']/../..//*[text()='补单管理']")

        
    # menu_external_planform_3s = (By.XPATH, "//li[@permission-id='ops.cm.ss']")                                                                      # 3S
    # menu_external_planform_3s_channel_setting = (By.XPATH, "//span[text()='3S']/../..//span[text()='频道设置']/../..")                        # 3S -> 頻道設定
    # ok_point_external_planform_3s_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='3S']/../..//*[text()='频道设置']")
    # menu_external_planform_3s_sport = (By.XPATH, "//span[text()='3S-体育']/..")                                                            # 3S -> 3S-体育
    # menu_external_planform_3s_sport_game_list = (By.XPATH, "//span[text()='3S-体育']/../..//span[text()='游戏列表']/..")                    # 3S -> 3S-体育 -> 遊戲列表
    # menu_external_planform_3s_sport_replenishment_management = (By.XPATH, "//span[text()='3S-体育']/../..//span[text()='补单管理']/..")     # 3S -> 3S-体育 -> 補單管理
    # ok_point_external_planform_3s_sport_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='3S-体育']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_3s_sport_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='3S-体育']/../..//*[text()='补单管理']")

        
    # menu_external_planform_sw = (By.XPATH, "//li[@permission-id='ops.cm.sw']")                                                                           # SW
    # menu_external_planform_sw_channel_setting = (By.XPATH, "//span[text()='SW']/../..//span[text()='频道设置']/../..")                            # SW -> 頻道設定
    # ok_point_external_planform_sw_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='SW']/../..//*[text()='频道设置']")
    # menu_external_planform_sw_electronics = (By.XPATH, "//span[text()='SW-电子']/..")                                                          # SW -> SW-电子
    # menu_external_planform_sw_electronics_game_list = (By.XPATH, "//span[text()='SW-电子']/../..//span[text()='游戏列表']/..")                  # SW -> SW-电子 -> 遊戲列表
    # menu_external_planform_sw_electronics_replenishment_management = (By.XPATH, "//span[text()='SW-电子']/../..//span[text()='补单管理']/..")   # SW -> SW-电子 -> 補單管理
    # ok_point_external_planform_sw_electronics_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SW-电子']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_sw_electronics_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='SW-电子']/../..//*[text()='补单管理']")

        
    # menu_external_planform_vg = (By.XPATH, "(//li[@permission-id='ops.cm.bbin']/following::a)[1]")                                                                       # VG
    # menu_external_planform_vg_channel_setting = (By.XPATH, "//span[text()='VG']/../..//span[text()='频道设置']/../..")                        # VG -> 頻道設定
    # ok_point_external_planform_vg_channel_setting = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='VG']/../..//*[text()='频道设置']")
    # menu_external_planform_vg_chess = (By.XPATH, "//span[text()='VG-棋牌']/..")                                                            # VG -> VG-棋牌
    # menu_external_planform_vg_chess_game_list = (By.XPATH, "//span[text()='VG-棋牌']/../..//span[text()='游戏列表']/..")                    # VG -> VG-棋牌 -> 遊戲列表
    # menu_external_planform_vg_chess_replenishment_management = (By.XPATH, "//span[text()='VG-棋牌']/../..//span[text()='补单管理']/..")     # VG -> VG-棋牌 -> 補單管理
    # ok_point_external_planform_vg_chess_game_list = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='VG-棋牌']/../..//*[text()='游戏列表']")
    # ok_point_external_planform_vg_chess_replenishment_management = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='VG-棋牌']/../..//*[text()='补单管理']")

    # *五分彩种
    menu_five_min_ticket = (By.XPATH, "//span[text()='五分彩种']/..")                                                           # 五分彩种

    menu_five_min_js6_ticket = (By.XPATH, "//span[text()='极速六合彩']/..")                                                     # 五分彩种 -> 極速六合彩
    menu_five_min_js6_ticket_period_management = (By.XPATH, "//span[text()='极速六合彩']/../..//span[text()='期数管理']/..")     # 五分彩种 -> 極速六合彩 -> 期數管理
    menu_five_min_js6_ticket_handicap_management = (By.XPATH, "//span[text()='极速六合彩']/../..//span[text()='盘口管理']/..")   # 五分彩种 -> 極速六合彩 -> 盤口管理
    menu_five_min_js6_ticket_bet_limit = (By.XPATH, "//span[text()='极速六合彩']/../..//span[text()='投注限额']/..")             # 五分彩种 -> 極速六合彩 -> 投注限額
    menu_five_min_js6_ticket_game_setting = (By.XPATH, "//span[text()='极速六合彩']/../..//span[text()='游戏设置']/..")          # 五分彩种 -> 極速六合彩 -> 遊戲設置
    ok_point_five_min_js6_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='极速六合彩']/../..//*[text()='期数管理']")
    ok_point_five_min_js6_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='极速六合彩']/../..//*[text()='盘口管理']")
    ok_point_five_min_js6_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='极速六合彩']/../..//*[text()='投注限额']")
    ok_point_five_min_js6_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='极速六合彩']/../..//*[text()='游戏设置']")


    menu_five_min_k3_ticket = (By.XPATH, "//span[text()='五分快3']/..")                                                         # 五分彩种 -> 五分快3
    menu_five_min_k3_ticket_period_management = (By.XPATH, "//span[text()='五分快3']/../..//span[text()='期数管理']/..")         # 五分彩种 -> 五分快3 -> 期數管理
    menu_five_min_k3_ticket_handicap_management = (By.XPATH, "//span[text()='五分快3']/../..//span[text()='盘口管理']/..")       # 五分彩种 -> 五分快3 -> 盤口管理
    menu_five_min_k3_ticket_bet_limit = (By.XPATH, "//span[text()='五分快3']/../..//span[text()='投注限额']/..")                 # 五分彩种 -> 五分快3 -> 投注限額
    menu_five_min_k3_ticket_game_setting = (By.XPATH, "//span[text()='五分快3']/../..//span[text()='游戏设置']/..")              # 五分彩种 -> 五分快3 -> 遊戲設置
    ok_point_five_min_k3_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='五分快3']/../..//*[text()='期数管理']")
    ok_point_five_min_k3_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='五分快3']/../..//*[text()='盘口管理']")
    ok_point_five_min_k3_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='五分快3']/../..//*[text()='投注限额']")
    ok_point_five_min_k3_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='五分快3']/../..//*[text()='游戏设置']")


    menu_five_min_pk10_ticket = (By.XPATH, "//span[text()='五分PK拾']/..")                                                      # 五分彩种 -> 五分PK拾
    menu_five_min_pk10_ticket_period_management = (By.XPATH, "//span[text()='五分PK拾']/../..//span[text()='期数管理']/..")      # 五分彩种 -> 五分PK拾 -> 期數管理
    menu_five_min_pk10_ticket_handicap_management = (By.XPATH, "//span[text()='五分PK拾']/../..//span[text()='盘口管理']/..")    # 五分彩种 -> 五分PK拾 -> 盤口管理
    menu_five_min_pk10_ticket_bet_limit = (By.XPATH, "//span[text()='五分PK拾']/../..//span[text()='投注限额']/..")              # 五分彩种 -> 五分PK拾 -> 投注限額
    menu_five_min_pk10_ticket_game_setting = (By.XPATH, "//span[text()='五分PK拾']/../..//span[text()='游戏设置']/..")           # 五分彩种 -> 五分PK拾 -> 遊戲設置
    ok_point_five_min_pk10_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='五分PK拾']/../..//*[text()='期数管理']")
    ok_point_five_min_pk10_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='五分PK拾']/../..//*[text()='盘口管理']")
    ok_point_five_min_pk10_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='五分PK拾']/../..//*[text()='投注限额']")
    ok_point_five_min_pk10_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='五分PK拾']/../..//*[text()='游戏设置']")


    menu_five_min_ssc_ticket = (By.XPATH, "//span[text()='五分时时彩']/..")                                                     # 五分彩种 -> 五分時時彩
    menu_five_min_ssc_ticket_period_management = (By.XPATH, "//span[text()='五分时时彩']/../..//span[text()='期数管理']/..")     # 五分彩种 -> 五分時時彩 -> 期數管理
    menu_five_min_ssc_ticket_handicap_management = (By.XPATH, "//span[text()='五分时时彩']/../..//span[text()='盘口管理']/..")   # 五分彩种 -> 五分時時彩 -> 盤口管理
    menu_five_min_ssc_ticket_bet_limit = (By.XPATH, "//span[text()='五分时时彩']/../..//span[text()='投注限额']/..")             # 五分彩种 -> 五分時時彩 -> 投注限額
    menu_five_min_ssc_ticket_game_setting = (By.XPATH, "//span[text()='五分时时彩']/../..//span[text()='游戏设置']/..")          # 五分彩种 -> 五分時時彩 -> 遊戲設置
    ok_point_five_min_ssc_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='五分时时彩']/../..//*[text()='期数管理']")
    ok_point_five_min_ssc_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='五分时时彩']/../..//*[text()='盘口管理']")
    ok_point_five_min_ssc_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='五分时时彩']/../..//*[text()='投注限额']")
    ok_point_five_min_ssc_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='五分时时彩']/../..//*[text()='游戏设置']")


    menu_five_min_xy28_ticket = (By.XPATH, "//span[text()='五分幸运28']/..")                                                    # 五分彩种 -> 五分幸運28
    menu_five_min_xy28_ticket_period_management = (By.XPATH, "//span[text()='五分幸运28']/../..//span[text()='期数管理']/..")    # 五分彩种 -> 五分幸運28 -> 期數管理
    menu_five_min_xy28_ticket_handicap_management = (By.XPATH, "//span[text()='五分幸运28']/../..//span[text()='盘口管理']/..")  # 五分彩种 -> 五分幸運28 -> 盤口管理
    menu_five_min_xy28_ticket_bet_limit = (By.XPATH, "//span[text()='五分幸运28']/../..//span[text()='投注限额']/..")            # 五分彩种 -> 五分幸運28 -> 投注限額
    menu_five_min_xy28_ticket_game_setting = (By.XPATH, "//span[text()='五分幸运28']/../..//span[text()='游戏设置']/..")         # 五分彩种 -> 五分幸運28 -> 遊戲設置
    ok_point_five_min_xy28_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='五分幸运28']/../..//*[text()='期数管理']")
    ok_point_five_min_xy28_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='五分幸运28']/../..//*[text()='盘口管理']")
    ok_point_five_min_xy28_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='五分幸运28']/../..//*[text()='投注限额']")
    ok_point_five_min_xy28_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='五分幸运28']/../..//*[text()='游戏设置']")

    # *三分彩种
    menu_three_min_ticket = (By.XPATH, "//span[text()='三分彩种']/..")                                                          # 三分彩种

    menu_three_min_3f6_ticket = (By.XPATH, "//span[text()='三分六合彩']/..")                                                    # 三分彩种 -> 三分六合彩
    menu_three_min_3f6_ticket_period_management = (By.XPATH, "//span[text()='三分六合彩']/../..//span[text()='期数管理']/..")    # 三分彩种 -> 三分六合彩 -> 期數管理
    menu_three_min_3f6_ticket_handicap_management = (By.XPATH, "//span[text()='三分六合彩']/../..//span[text()='盘口管理']/..")  # 三分彩种 -> 三分六合彩 -> 盤口管理
    menu_three_min_3f6_ticket_bet_limit = (By.XPATH, "//span[text()='三分六合彩']/../..//span[text()='投注限额']/..")            # 三分彩种 -> 三分六合彩 -> 投注限額
    menu_three_min_3f6_ticket_game_setting = (By.XPATH, "//span[text()='三分六合彩']/../..//span[text()='游戏设置']/..")         # 三分彩种 -> 三分六合彩 -> 遊戲設置
    ok_point_three_min_3f6_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='三分六合彩']/../..//*[text()='期数管理']")
    ok_point_three_min_3f6_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='三分六合彩']/../..//*[text()='盘口管理']")
    ok_point_three_min_3f6_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='三分六合彩']/../..//*[text()='投注限额']")
    ok_point_three_min_3f6_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='三分六合彩']/../..//*[text()='游戏设置']")

    # *香港彩票
    menu_hongkong_ticket = (By.XPATH, "//span[text()='香港彩票']/..")                                                           # 香港彩票

    menu_hongkong_hk6_ticket = (By.XPATH, "//span[text()='香港六合彩']/..")                                                     # 香港彩票 -> 香港六合彩
    menu_hongkong_hk6_ticket_period_management = (By.XPATH, "//span[text()='香港六合彩']/../..//span[text()='期数管理']/..")     # 香港彩票 -> 香港六合彩 -> 期數管理
    menu_hongkong_hk6_ticket_handicap_management = (By.XPATH, "//span[text()='香港六合彩']/../..//span[text()='盘口管理']/..")   # 香港彩票 -> 香港六合彩 -> 盤口管理
    menu_hongkong_hk6_ticket_bet_limit = (By.XPATH, "//span[text()='香港六合彩']/../..//span[text()='投注限额']/..")             # 香港彩票 -> 香港六合彩 -> 投注限額
    menu_hongkong_hk6_ticket_game_setting = (By.XPATH, "//span[text()='香港六合彩']/../..//span[text()='游戏设置']/..")          # 香港彩票 -> 香港六合彩 -> 遊戲設置
    ok_point_hongkong_hk6_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='香港六合彩']/../..//*[text()='期数管理']")
    ok_point_hongkong_hk6_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='香港六合彩']/../..//*[text()='盘口管理']")
    ok_point_hongkong_hk6_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='香港六合彩']/../..//*[text()='投注限额']")
    ok_point_hongkong_hk6_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='香港六合彩']/../..//*[text()='游戏设置']")

    # *福彩/体彩
    menu_welfare_sport_ticket = (By.XPATH, "//span[text()='福彩/体彩']/..")                                                           # 福彩/体彩

    menu_welfare_sport_fc3d_ticket = (By.XPATH, "//span[text()='福彩3D']/..")                                                        # 福彩/体彩 -> 福彩3D
    menu_welfare_sport_fc3d_ticket_period_management = (By.XPATH, "//span[text()='福彩3D']/../..//span[text()='期数管理']/..")        # 福彩/体彩 -> 福彩3D -> 期數管理
    menu_welfare_sport_fc3d_ticket_handicap_management = (By.XPATH, "//span[text()='福彩3D']/../..//span[text()='盘口管理']/..")      # 福彩/体彩 -> 福彩3D -> 盤口管理
    menu_welfare_sport_fc3d_ticket_bet_limit = (By.XPATH, "//span[text()='福彩3D']/../..//span[text()='投注限额']/..")                # 福彩/体彩 -> 福彩3D -> 投注限額
    menu_welfare_sport_fc3d_ticket_game_setting = (By.XPATH, "//span[text()='福彩3D']/../..//span[text()='游戏设置']/..")             # 福彩/体彩 -> 福彩3D -> 遊戲設置
    ok_point_welfare_sport_fc3d_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='福彩3D']/../..//*[text()='期数管理']")
    ok_point_welfare_sport_fc3d_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='福彩3D']/../..//*[text()='盘口管理']")
    ok_point_welfare_sport_fc3d_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='福彩3D']/../..//*[text()='投注限额']")
    ok_point_welfare_sport_fc3d_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='福彩3D']/../..//*[text()='游戏设置']")


    menu_welfare_sport_pl3_ticket = (By.XPATH, "//span[text()='排列三']/..")                                                         # 福彩/体彩 -> 排列三
    menu_welfare_sport_pl3_ticket_handicap_management = (By.XPATH, "//span[text()='排列三']/../..//span[text()='盘口管理']/..")       # 福彩/体彩 -> 排列三 -> 盤口管理
    menu_welfare_sport_pl3_ticket_period_management = (By.XPATH, "//span[text()='排列三']/../..//span[text()='期数管理']/..")         # 福彩/体彩 -> 排列三 -> 期數管理
    menu_welfare_sport_pl3_ticket_bet_limit = (By.XPATH, "//span[text()='排列三']/../..//span[text()='投注限额']/..")                 # 福彩/体彩 -> 排列三 -> 投注限額
    menu_welfare_sport_pl3_ticket_game_setting = (By.XPATH, "//span[text()='排列三']/../..//span[text()='游戏设置']/..")              # 福彩/体彩 -> 排列三 -> 遊戲設置
    ok_point_welfare_sport_pl3_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='排列三']/../..//*[text()='期数管理']")
    ok_point_welfare_sport_pl3_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='排列三']/../..//*[text()='盘口管理']")
    ok_point_welfare_sport_pl3_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='排列三']/../..//*[text()='投注限额']")
    ok_point_welfare_sport_pl3_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='排列三']/../..//*[text()='游戏设置']")

    # *极速彩种
    menu_exteremespeed_ticket = (By.XPATH, "//span[text()='极速彩种']/..")                                                            # 极速彩种

    menu_exteremespeed_ff6_ticket = (By.XPATH, "//span[text()='分分六合彩']/..")                                                      # 极速彩种 -> 分分六合彩
    menu_exteremespeed_ff6_ticket_period_management = (By.XPATH, "//span[text()='分分六合彩']/../..//span[text()='期数管理']/..")      # 极速彩种 -> 分分六合彩 -> 期數管理
    menu_exteremespeed_ff6_ticket_handicap_management = (By.XPATH, "//span[text()='分分六合彩']/../..//span[text()='盘口管理']/..")    # 极速彩种 -> 分分六合彩 -> 盤口管理
    menu_exteremespeed_ff6_ticket_bet_limit = (By.XPATH, "//span[text()='分分六合彩']/../..//span[text()='投注限额']/..")              # 极速彩种 -> 分分六合彩 -> 投注限額
    menu_exteremespeed_ff6_ticket_game_setting = (By.XPATH, "//span[text()='分分六合彩']/../..//span[text()='游戏设置']/..")           # 极速彩种 -> 分分六合彩 -> 遊戲設置
    ok_point_exteremespeed_ff6_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='分分六合彩']/../..//*[text()='期数管理']")
    ok_point_exteremespeed_ff6_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='分分六合彩']/../..//*[text()='盘口管理']")
    ok_point_exteremespeed_ff6_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='分分六合彩']/../..//*[text()='投注限额']")
    ok_point_exteremespeed_ff6_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='分分六合彩']/../..//*[text()='游戏设置']")


    menu_exteremespeed_jsssc_ticket = (By.XPATH, "//span[text()='极速时时彩']/..")                                                    # 极速彩种 -> 极速时时彩
    menu_exteremespeed_jsssc_ticket_period_management = (By.XPATH, "//span[text()='极速时时彩']/../..//span[text()='期数管理']/..")    # 极速彩种 -> 极速时时彩 -> 期數管理
    menu_exteremespeed_jsssc_ticket_handicap_management = (By.XPATH, "//span[text()='极速时时彩']/../..//span[text()='盘口管理']/..")  # 极速彩种 -> 极速时时彩 -> 盤口管理
    menu_exteremespeed_jsssc_ticket_bet_limit = (By.XPATH, "//span[text()='极速时时彩']/../..//span[text()='投注限额']/..")            # 极速彩种 -> 极速时时彩 -> 投注限額
    menu_exteremespeed_jsssc_ticket_game_setting = (By.XPATH, "//span[text()='极速时时彩']/../..//span[text()='游戏设置']/..")         # 极速彩种 -> 极速时时彩 -> 遊戲設置
    ok_point_exteremespeed_jsssc_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='极速时时彩']/../..//*[text()='期数管理']")
    ok_point_exteremespeed_jsssc_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='极速时时彩']/../..//*[text()='盘口管理']")
    ok_point_exteremespeed_jsssc_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='极速时时彩']/../..//*[text()='投注限额']")
    ok_point_exteremespeed_jsssc_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='极速时时彩']/../..//*[text()='游戏设置']")


    menu_exteremespeed_jspk10_ticket = (By.XPATH, "//span[text()='极速PK拾']/..")                                                     # 极速彩种 -> 极速PK拾
    menu_exteremespeed_jspk10_ticket_handicap_management = (By.XPATH, "//span[text()='极速PK拾']/../..//span[text()='盘口管理']/..")   # 极速彩种 -> 极速PK拾 -> 盤口管理
    menu_exteremespeed_jspk10_ticket_period_management = (By.XPATH, "//span[text()='极速PK拾']/../..//span[text()='期数管理']/..")     # 极速彩种 -> 极速PK拾 -> 期數管理
    menu_exteremespeed_jspk10_ticket_bet_limit = (By.XPATH, "//span[text()='极速PK拾']/../..//span[text()='投注限额']/..")             # 极速彩种 -> 极速PK拾 -> 投注限額
    menu_exteremespeed_jspk10_ticket_game_setting = (By.XPATH, "//span[text()='极速PK拾']/../..//span[text()='游戏设置']/..")          # 极速彩种 -> 极速PK拾 -> 遊戲設置
    ok_point_exteremespeed_jspk10_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='极速PK拾']/../..//*[text()='期数管理']")
    ok_point_exteremespeed_jspk10_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='极速PK拾']/../..//*[text()='盘口管理']")
    ok_point_exteremespeed_jspk10_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='极速PK拾']/../..//*[text()='投注限额']")
    ok_point_exteremespeed_jspk10_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='极速PK拾']/../..//*[text()='游戏设置']")


    menu_exteremespeed_jisuk3_ticket = (By.XPATH, "//span[text()='极速快3']/..")                                                        # 极速彩种 -> 极速快3
    menu_exteremespeed_jisuk3_ticket_handicap_management = (By.XPATH, "//span[text()='极速快3']/../..//span[text()='盘口管理']/..")      # 极速彩种 -> 极速快3 -> 盤口管理
    menu_exteremespeed_jisuk3_ticket_period_management = (By.XPATH, "//span[text()='极速快3']/../..//span[text()='期数管理']/..")        # 极速彩种 -> 极速快3 -> 期數管理
    menu_exteremespeed_jisuk3_ticket_bet_limit = (By.XPATH, "//span[text()='极速快3']/../..//span[text()='投注限额']/..")                # 极速彩种 -> 极速快3 -> 投注限額
    menu_exteremespeed_jisuk3_ticket_game_setting = (By.XPATH, "//span[text()='极速快3']/../..//span[text()='游戏设置']/..")             # 极速彩种 -> 极速快3 -> 遊戲設置
    ok_point_exteremespeed_jisuk3_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='极速快3']/../..//*[text()='期数管理']")
    ok_point_exteremespeed_jisuk3_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='极速快3']/../..//*[text()='盘口管理']")
    ok_point_exteremespeed_jisuk3_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='极速快3']/../..//*[text()='投注限额']")
    ok_point_exteremespeed_jisuk3_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='极速快3']/../..//*[text()='游戏设置']")

    # *高频彩种
    menu_high_ticket = (By.XPATH, "//span[text()='高频彩种']/..")                                                                     # 高频彩种

    menu_high_11x5_ticket = (By.XPATH, "//span[text()='11选5']/..")                                                                  # 高频彩种 -> 11选5

    menu_high_other_ticket = (By.XPATH, "//span[text()='其他']/..")                                                                       # 高频彩种 -> 其他

    menu_high_other_lucky_airship_ticket = (By.XPATH, "//span[text()='幸运飞艇']/..")                                                      # 高频彩种 -> 其他 -> 幸运飞艇
    menu_high_other_lucky_airship_ticket_handicap_management = (By.XPATH, "//span[text()='幸运飞艇']/../..//span[text()='盘口管理']/..")      # 高频彩种 -> 其他 -> 幸运飞艇 -> 盤口管理
    menu_high_other_lucky_airship_ticket_period_management = (By.XPATH, "//span[text()='幸运飞艇']/../..//span[text()='期数管理']/..")        # 高频彩种 -> 其他 -> 幸运飞艇 -> 期數管理
    menu_high_other_lucky_airship_ticket_bet_limit = (By.XPATH, "//span[text()='幸运飞艇']/../..//span[text()='投注限额']/..")                # 高频彩种 -> 其他 -> 幸运飞艇 -> 投注限額
    menu_high_other_lucky_airship_ticket_game_setting = (By.XPATH, "//span[text()='幸运飞艇']/../..//span[text()='游戏设置']/..")             # 高频彩种 -> 其他 -> 幸运飞艇 -> 遊戲設置
    ok_point_high_other_lucky_airship_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='幸运飞艇']/../..//*[text()='期数管理']")
    ok_point_high_other_lucky_airship_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='幸运飞艇']/../..//*[text()='盘口管理']")
    ok_point_high_other_lucky_airship_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='幸运飞艇']/../..//*[text()='投注限额']")
    ok_point_high_other_lucky_airship_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='幸运飞艇']/../..//*[text()='游戏设置']")


    menu_high_xy28_ticket = (By.XPATH, "//span[text()='幸运28']/..")                                                      # 高频彩种 -> 幸运28
    menu_high_xy28_pc_ticket = (By.XPATH, "//span[text()='PC蛋蛋']/..")                                                      # 高频彩种 -> 幸运28 -> PC蛋蛋
    menu_high_xy28_pc_ticket_handicap_management = (By.XPATH, "//span[text()='PC蛋蛋']/../..//span[text()='盘口管理']/..")      # 高频彩种 -> 幸运28 -> PC蛋蛋 -> 盤口管理
    menu_high_xy28_pc_ticket_period_management = (By.XPATH, "//span[text()='PC蛋蛋']/../..//span[text()='期数管理']/..")        # 高频彩种 -> 幸运28 -> PC蛋蛋 -> 期數管理
    menu_high_xy28_pc_ticket_bet_limit = (By.XPATH, "//span[text()='PC蛋蛋']/../..//span[text()='投注限额']/..")                # 高频彩种 -> 幸运28 -> PC蛋蛋 -> 投注限額
    menu_high_xy28_pc_ticket_game_setting = (By.XPATH, "//span[text()='PC蛋蛋']/../..//span[text()='游戏设置']/..")             # 高频彩种 -> 幸运28 -> PC蛋蛋 -> 遊戲設置
    ok_point_high_xy28_pc_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='PC蛋蛋']/../..//*[text()='期数管理']")
    ok_point_high_xy28_pc_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='PC蛋蛋']/../..//*[text()='盘口管理']")
    ok_point_high_xy28_pc_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='PC蛋蛋']/../..//*[text()='投注限额']")
    ok_point_high_xy28_pc_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='PC蛋蛋']/../..//*[text()='游戏设置']")
    menu_high_xy28_tw_ticket = (By.XPATH, "//span[text()='台湾幸运28']/..")                                                      # 高频彩种 -> 幸运28 -> 台湾幸运28
    menu_high_xy28_tw_ticket_handicap_management = (By.XPATH, "//span[text()='台湾幸运28']/../..//span[text()='盘口管理']/..")      # 高频彩种 -> 幸运28 -> 台湾幸运28 -> 盤口管理
    menu_high_xy28_tw_ticket_period_management = (By.XPATH, "//span[text()='台湾幸运28']/../..//span[text()='期数管理']/..")        # 高频彩种 -> 幸运28 -> 台湾幸运28 -> 期數管理
    menu_high_xy28_tw_ticket_bet_limit = (By.XPATH, "//span[text()='台湾幸运28']/../..//span[text()='投注限额']/..")                # 高频彩种 -> 幸运28 -> 台湾幸运28 -> 投注限額
    menu_high_xy28_tw_ticket_game_setting = (By.XPATH, "//span[text()='台湾幸运28']/../..//span[text()='游戏设置']/..")             # 高频彩种 -> 幸运28 -> 台湾幸运28 -> 遊戲設置
    ok_point_high_xy28_tw_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='台湾幸运28']/../..//*[text()='期数管理']")
    ok_point_high_xy28_tw_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='台湾幸运28']/../..//*[text()='盘口管理']")
    ok_point_high_xy28_tw_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='台湾幸运28']/../..//*[text()='投注限额']")
    ok_point_high_xy28_tw_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='台湾幸运28']/../..//*[text()='游戏设置']")
    menu_high_xy28_canada_ticket = (By.XPATH, "//span[text()='加拿大幸运28']/..")                                                      # 高频彩种 -> 幸运28 -> 加拿大幸运28
    menu_high_xy28_canada_ticket_handicap_management = (By.XPATH, "//span[text()='加拿大幸运28']/../..//span[text()='盘口管理']/..")      # 高频彩种 -> 幸运28 -> 加拿大幸运28 -> 盤口管理
    menu_high_xy28_canada_ticket_period_management = (By.XPATH, "//span[text()='加拿大幸运28']/../..//span[text()='期数管理']/..")        # 高频彩种 -> 幸运28 -> 加拿大幸运28 -> 期數管理
    menu_high_xy28_canada_ticket_bet_limit = (By.XPATH, "//span[text()='加拿大幸运28']/../..//span[text()='投注限额']/..")                # 高频彩种 -> 幸运28 -> 加拿大幸运28 -> 投注限額
    menu_high_xy28_canada_ticket_game_setting = (By.XPATH, "//span[text()='加拿大幸运28']/../..//span[text()='游戏设置']/..")             # 高频彩种 -> 幸运28 -> 加拿大幸运28 -> 遊戲設置
    ok_point_high_xy28_canada_ticket_period_management = (By.XPATH, "//a[contains(@href, '#') and text()='加拿大幸运28']/../..//*[text()='期数管理']")
    ok_point_high_xy28_canada_ticket_handicap_management = (By.XPATH, "//a[contains(@href, '#') and text()='加拿大幸运28']/../..//*[text()='盘口管理']")
    ok_point_high_xy28_canada_ticket_bet_limit = (By.XPATH, "//a[contains(@href, '#') and text()='加拿大幸运28']/../..//*[text()='投注限额']")
    ok_point_high_xy28_canada_ticket_game_setting = (By.XPATH, "//a[contains(@href, '#') and text()='加拿大幸运28']/../..//*[text()='游戏设置']")


    menu_high_k3_ticket = (By.XPATH, "//span[text()='快3']/..")                                                      # 高频彩种 -> 快3

    menu_high_ssc_ticket = (By.XPATH, "//span[text()='时时彩']/..")                                                      # 高频彩种 -> 时时彩

    red_envelope = (By.XPATH, '//span[text()="红包"]/../..') # 紅包
    # ------------------------------------------ 掃雷 ------------------------------------------
    mine_sweeping = (By.XPATH, '//span[text()="扫雷"]/../..') # 掃雷
    mine_sweeping_opening_management = (By.XPATH, '//span[text()="扫雷"]/../..//span[text()="开局管理"]/..') # 開局管理
    mine_sweeping_hall_management = (By.XPATH, '//span[text()="扫雷"]/../..//span[text()="厅别管理"]/..') # 廳別管理
    mine_sweeping_game_setting = (By.XPATH, '//span[text()="扫雷"]/../..//span[text()="游戏设置"]/..') # 遊戲設置
    mine_sweeping_player_custom = (By.XPATH, '//span[text()="扫雷"]/../..//span[text()="玩家自订"]/..') # 玩家自訂

    # ------------------------------------------ 牛牛 ------------------------------------------
    niu_niu = (By.XPATH, '//span[text()="牛牛"]/../..') # 牛牛
    niu_niu_opening_management = (By.XPATH, '//span[text()="牛牛"]/../..//span[text()="开局管理"]/..') # 開局管理
    niu_niu_hall_management = (By.XPATH, '//span[text()="牛牛"]/../..//span[text()="厅别管理"]/..') # 廳別管理
    niu_niu_game_setting = (By.XPATH, '//span[text()="牛牛"]/../..//span[text()="游戏设置"]/..') # 遊戲設置
    niu_niu_player_custom = (By.XPATH, '//span[text()="牛牛"]/../..//span[text()="玩家自订"]/..') # 玩家自訂


class OperationManagementPage(BasePage):
    # 運維管理
    def click_operation_managenent(self):
        self.wait_loading_finish()

        for _ in range(2):
            if self.is_element_finded(OperationManagementPageLocator.menu_operation_management) is True:
                break
            else:
                self.sleep(3)

        for loop in range(0, 6):
            self.sleep(1)
            if loop != 5:
                try:
                    self.click(OperationManagementPageLocator.menu_operation_management)
                    break
                except:
                    pass
            else:
                self.click(OperationManagementPageLocator.menu_operation_management)

    # 運維管理 -> 注單中心
    def into_order_center(self):
        self.click_operation_managenent()
        self.click(OperationManagementPageLocator.menu_order_center)
        self.wait_visibility(OperationManagementPageLocator.ok_point_order_center)
        self.wait_loading_finish()

    # 運維管理 -> 即时注单
    def into_instant_order_center(self):
        self.click_operation_managenent()
        self.click(OperationManagementPageLocator.menu_instant_order_center)
        self.wait_visibility(OperationManagementPageLocator.ok_point_instant_order_center)
        self.wait_loading_finish()
    
    # 運維管理 -> 外接平台
    def click_external_planform_operation(self):
        self.click_operation_managenent()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_operation) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_external_planform_operation)
    
    # 運維管理 -> 外接平台 -> 遊戲列表
    def into_game_list(self):
        self.click_external_planform_operation()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_gamelist) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_gamelist)
        self.wait_visibility(OperationManagementPageLocator.ok_gamelist)    #確認進入遊戲列表頁

    # 運維管理 -> 外接平台 -> 頻道設置
    def into_channel_setting(self):
        self.click_external_planform_operation()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_channel_setting) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_channel_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_channel_setting)    #確認進入頻道設置頁

    # 運維管理 -> 外接平台 -> 補單管理
    def into_replenishment_management(self):
        self.click_external_planform_operation()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_replenishment_management) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_replenishment_management)
        self.wait_visibility(OperationManagementPageLocator.ok_replenishment_management)    #確認進入補單管理頁

    # # 運維管理 -> 外接平台 -> AG
    # def click_ag(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_ag) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_ag):
    #             self.click(OperationManagementPageLocator.menu_external_planform_ag)
    #             break
    #         else:
    #             self.sleep(1)
            
    #         if i == 2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> AG -> 頻道設置
    # def into_ag_channel_setting(self):
    #     self.click_ag()
    #     self.click(OperationManagementPageLocator.menu_external_planform_ag_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_ag_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> AG -> AG-視訊
    # def click_ag_video(self):
    #     self.click_ag()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_ag_video) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_ag_video)

    # # 運維管理 -> 外接平台 -> AG -> AG-視訊 -> 遊戲列表
    # def into_ag_video_game_list(self):
    #     self.click_ag_video()
    #     self.click(OperationManagementPageLocator.menu_external_planform_ag_video_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_ag_video_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> AG -> AG-視訊 -> 補單管理
    # def into_ag_video_replenishment_management(self):
    #     self.click_ag_video()
    #     self.click(OperationManagementPageLocator.menu_external_planform_ag_video_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_ag_video_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> AG -> AG-電子
    # def click_ag_electronics(self):
    #     self.click_ag()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_ag_electronics) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_ag_electronics)

    # # 運維管理 -> 外接平台 -> AG -> AG-電子 -> 遊戲列表
    # def into_ag_electronics_game_list(self):
    #     self.click_ag_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_ag_electronics_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_ag_electronics_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> AG -> AG-電子 -> 補單管理
    # def into_ag_electronics_replenishment_management(self):
    #     self.click_ag_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_ag_electronics_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_ag_electronics_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> AG -> AG-捕魚
    # def click_ag_fishing(self):
    #     self.click_ag()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_ag_fishing) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_ag_fishing)

    # # 運維管理 -> 外接平台 -> AG -> AG-捕魚 -> 遊戲列表
    # def into_ag_fishing_game_list(self):
    #     self.click_ag_fishing()
    #     self.click(OperationManagementPageLocator.menu_external_planform_ag_fishing_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_ag_fishing_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> AG -> AG-捕魚 -> 補單管理
    # def into_ag_fishing_replenishment_management(self):
    #     self.click_ag_fishing()
    #     self.click(OperationManagementPageLocator.menu_external_planform_ag_fishing_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_ag_fishing_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> BBIN
    # def click_bbin(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_bbin) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_bbin):
    #             self.click(OperationManagementPageLocator.menu_external_planform_bbin)
    #             break
    #         else:
    #             self.sleep(1)

    # # 運維管理 -> 外接平台 -> BBIN -> 頻道設定
    # def into_bbin_channel_setting(self):
    #     self.click_bbin()
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_bbin_channel_setting)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-捕魚
    # def click_bbin_fishing(self):
    #     self.click_bbin()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_bbin_fishing) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_fishing)

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-捕魚 -> 遊戲列表
    # def into_bbin_fishing_game_list(self):
    #     self.click_bbin_fishing()
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_fishing_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_bbin_fishing_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-捕魚 -> 補單管理
    # def into_bbin_fishing_replenishment_management(self):
    #     self.click_bbin_fishing()
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_fishing_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_bbin_fishing_replenishment_management)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-電子
    # def click_bbin_electronics(self):
    #     self.click_bbin()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_bbin_electronics) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_electronics)

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-電子 -> 遊戲列表
    # def into_bbin_electronics_game_list(self):
    #     self.click_bbin_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_electronics_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_bbin_electronics_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-電子 -> 補單管理
    # def into_bbin_electronics_replenishment_management(self):
    #     self.click_bbin_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_electronics_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_bbin_electronics_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-視訊
    # def click_bbin_video(self):
    #     self.click_bbin()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_bbin_video) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_video)

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-視訊 -> 遊戲列表
    # def into_bbin_video_game_list(self):
    #     self.click_bbin_video()
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_video_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_bbin_video_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-視訊 -> 補單管理
    # def into_bbin_video_replenishment_management(self):
    #     self.click_bbin_video()
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_video_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_bbin_video_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-體育
    # def click_bbin_sport(self):
    #     self.click_bbin()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_bbin_sport) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_sport)

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-體育 -> 遊戲列表
    # def into_bbin_sport_game_list(self):
    #     self.click_bbin_sport()
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_sport_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_bbin_sport_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> BBIN -> BBIN-體育 -> 補單管理
    # def into_bbin_sport_replenishment_management(self):
    #     self.click_bbin_sport()
    #     self.click(OperationManagementPageLocator.menu_external_planform_bbin_sport_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_bbin_sport_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> CQ
    # def click_cq(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_cq) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_cq):
    #             self.click(OperationManagementPageLocator.menu_external_planform_cq)
    #             break
    #         else:
    #             self.sleep(1)

    # # 運維管理 -> 外接平台 -> CQ -> 頻道設定
    # def into_cq_channel_setting(self):
    #     self.click_cq()
    #     self.click(OperationManagementPageLocator.menu_external_planform_cq_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_cq_channel_setting)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> CQ -> CQ9-電子
    # def click_cq_electronics(self):
    #     self.click_cq()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_cq_electronics) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_cq_electronics)

    # # 運維管理 -> 外接平台 -> CQ -> CQ9-電子 -> 遊戲列表
    # def into_cq_electronics_game_list(self):
    #     self.click_cq_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_cq_electronics_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_cq_electronics_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> CQ -> CQ9-電子 -> 補單管理
    # def into_cq_electronics_replenishment_management(self):
    #     self.click_cq_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_cq_electronics_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_cq_electronics_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> CQ -> CQ9-捕魚
    # def click_cq_fishing(self):
    #     self.click_cq()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_cq_fishing) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_cq_fishing)

    # # 運維管理 -> 外接平台 -> CQ -> CQ9-捕魚 -> 遊戲列表
    # def into_cq_fishing_game_list(self):
    #     self.click_cq_fishing()
    #     self.click(OperationManagementPageLocator.menu_external_planform_cq_fishing_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_cq_fishing_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> CQ -> CQ9-捕魚 -> 補單管理
    # def into_cq_fishing_replenishment_management(self):
    #     self.click_cq_fishing()
    #     self.click(OperationManagementPageLocator.menu_external_planform_cq_fishing_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_cq_fishing_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> DT
    # def click_dt(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_dt) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_dt):
    #             self.click(OperationManagementPageLocator.menu_external_planform_dt)
    #             break
    #         else:
    #             self.sleep(1)
            
    #         if i == 2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> DT -> 頻道設定
    # def into_dt_channel_setting(self):
    #     self.click_dt()
    #     self.click(OperationManagementPageLocator.menu_external_planform_dt_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_dt_channel_setting)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> DT -> DT-電子
    # def click_dt_electronics(self):
    #     self.click_dt()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_dt_electronics) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_dt_electronics)

    # # 運維管理 -> 外接平台 -> DT -> DT-電子 -> 遊戲列表
    # def into_dt_electronics_game_list(self):
    #     self.click_dt_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_dt_electronics_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_dt_electronics_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> DT -> DT-電子 -> 補單管理
    # def into_dt_electronics_replenishment_management(self):
    #     self.click_dt_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_dt_electronics_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_dt_electronics_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> FG
    # def click_fg(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_fg) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_fg):
    #             self.click(OperationManagementPageLocator.menu_external_planform_fg)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i == 2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> FG -> 頻道設定
    # def into_fg_channel_setting(self):
    #     self.click_fg()
    #     self.click(OperationManagementPageLocator.menu_external_planform_fg_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_fg_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> FG -> FG-棋牌
    # def click_fg_chess(self):
    #     self.click_fg()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_fg_chess) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_fg_chess)

    # # 運維管理 -> 外接平台 -> FG -> FG-棋牌 -> 遊戲列表
    # def into_fg_chess_game_list(self):
    #     self.click_fg_chess()
    #     self.click(OperationManagementPageLocator.menu_external_planform_fg_chess_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_fg_chess_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> FG -> FG-棋牌 -> 補單管理
    # def into_fg_chess_replenishment_management(self):
    #     self.click_fg_chess()
    #     self.click(OperationManagementPageLocator.menu_external_planform_fg_chess_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_fg_chess_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> FG -> FG-電子
    # def click_fg_electronics(self):
    #     self.click_fg()
    #     for _ in range(0,2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_fg_electronics) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_fg_electronics)

    # # 運維管理 -> 外接平台 -> FG -> FG-電子 -> 遊戲列表
    # def into_fg_electronics_game_list(self):
    #     self.click_fg_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_fg_electronics_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_fg_electronics_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> FG -> FG-電子 -> 補單管理
    # def into_fg_electronics_replenishment_management(self):
    #     self.click_fg_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_fg_electronics_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_fg_electronics_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> GC
    # def click_gc(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_gc) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_gc):
    #             self.click(OperationManagementPageLocator.menu_external_planform_gc)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i == 2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> GC -> 頻道設定
    # def into_gc_channel_setting(self):
    #     self.click_gc()
    #     self.click(OperationManagementPageLocator.menu_external_planform_gc_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_gc_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> GC -> GC-視訊
    # def click_gc_video(self):
    #     self.click_gc()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_gc_video) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_gc_video)

    # # 運維管理 -> 外接平台 -> GC -> GC-視訊 -> 遊戲列表
    # def into_gc_video_game_list(self):
    #     self.click_gc_video()
    #     self.click(OperationManagementPageLocator.menu_external_planform_gc_video_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_gc_video_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> GC -> GC-視訊 -> 補單管理
    # def into_gc_video_replenishment_management(self):
    #     self.click_gc_video()
    #     self.click(OperationManagementPageLocator.menu_external_planform_gc_video_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_gc_video_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> GM
    # def click_gm(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_gm) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_gm):
    #             self.click(OperationManagementPageLocator.menu_external_planform_gm)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i == 2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> GM -> 頻道設定
    # def into_gm_channel_setting(self):
    #     self.click_gm()
    #     self.click(OperationManagementPageLocator.menu_external_planform_gm_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_gm_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> GM -> GM-棋牌
    # def click_gm_chess(self):
    #     self.click_gm()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_gm_chess) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_gm_chess)

    # # 運維管理 -> 外接平台 -> GM -> GM-棋牌 -> 遊戲列表
    # def into_gm_chess_game_list(self):
    #     self.click_gm_chess()
    #     self.click(OperationManagementPageLocator.menu_external_planform_gm_chess_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_gm_chess_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> GM -> GM-棋牌 -> 補單管理
    # def into_gm_chess_replenishment_management(self):
    #     self.click_gm_chess()
    #     self.click(OperationManagementPageLocator.menu_external_planform_gm_chess_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_gm_chess_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> KY
    # def click_ky(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_ky) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_ky):
    #             self.click(OperationManagementPageLocator.menu_external_planform_ky)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i == 2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> KY -> 頻道設定
    # def into_ky_channel_setting(self):
    #     self.click_ky()
    #     self.click(OperationManagementPageLocator.menu_external_planform_ky_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_ky_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> KY -> 開元棋牌
    # def click_ky_chess(self):
    #     self.click_ky()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_ky_chess) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_ky_chess)

    # # 運維管理 -> 外接平台 -> KY -> 開元棋牌 -> 遊戲列表
    # def into_ky_chess_game_list(self):
    #     self.click_ky_chess()
    #     self.click(OperationManagementPageLocator.menu_external_planform_ky_chess_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_ky_chess_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> KY -> 開元棋牌 -> 補單管理
    # def into_ky_chess_replenishment_management(self):
    #     self.click_ky_chess()
    #     self.click(OperationManagementPageLocator.menu_external_planform_ky_chess_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_ky_chess_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> LC
    # def click_lc(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_lc) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_lc):
    #             self.click(OperationManagementPageLocator.menu_external_planform_lc)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i == 2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> LC -> 頻道設定
    # def into_lc_channel_setting(self):
    #     self.click_lc()
    #     self.click(OperationManagementPageLocator.menu_external_planform_lc_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_lc_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> LC -> 龍城棋牌
    # def click_lc_chess(self):
    #     self.click_lc()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_lc_chess) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_lc_chess)

    # # 運維管理 -> 外接平台 -> LC -> 龍城棋牌 -> 遊戲列表
    # def into_lc_chess_game_list(self):
    #     self.click_lc_chess()
    #     self.click(OperationManagementPageLocator.menu_external_planform_lc_chess_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_lc_chess_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> LC -> 龍城棋牌 -> 補單管理
    # def into_lc_chess_replenishment_management(self):
    #     self.click_lc_chess()
    #     self.click(OperationManagementPageLocator.menu_external_planform_lc_chess_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_lc_chess_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> MG
    # def click_mg(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_mg) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_mg):
    #             self.click(OperationManagementPageLocator.menu_external_planform_mg)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i == 2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> MG -> 頻道設定
    # def into_mg_channel_setting(self):
    #     self.click_mg()
    #     self.click(OperationManagementPageLocator.menu_external_planform_mg_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_mg_channel_setting)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> MG -> MG-視訊
    # def click_mg_video(self):
    #     self.click_mg()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_mg_video) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_mg_video)

    # # 運維管理 -> 外接平台 -> MG -> MG-視訊 -> 遊戲列表
    # def into_mg_video_game_list(self):
    #     self.click_mg_video()
    #     self.click(OperationManagementPageLocator.menu_external_planform_mg_video_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_mg_video_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> MG -> MG-視訊 -> 補單管理
    # def into_mg_video_replenishment_management(self):
    #     self.click_mg_video()
    #     self.click(OperationManagementPageLocator.menu_external_planform_mg_video_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_mg_video_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> MG -> MG-電子
    # def click_mg_electronics(self):
    #     self.click_mg()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_mg_electronics) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_mg_electronics)

    # # 運維管理 -> 外接平台 -> MG -> MG-電子 -> 遊戲列表
    # def into_mg_electronics_game_list(self):
    #     self.click_mg_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_mg_electronics_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_mg_electronics_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> MG -> MG-電子 -> 補單管理
    # def into_mg_electronics_replenishment_management(self):
    #     self.click_mg_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_mg_electronics_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_mg_electronics_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> PT
    # def click_pt(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_pt) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_pt):
    #             self.click(OperationManagementPageLocator.menu_external_planform_pt)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i == 2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> PT -> 頻道設定
    # def into_pt_channel_setting(self):
    #     self.click_pt()
    #     self.click(OperationManagementPageLocator.menu_external_planform_pt_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_pt_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> PT -> PT-電子
    # def click_pt_electronics(self):
    #     self.click_pt()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_pt_electronics) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_pt_electronics)

    # # 運維管理 -> 外接平台 -> PT -> PT-電子 -> 遊戲列表
    # def into_pt_electronics_game_list(self):
    #     self.click_pt_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_pt_electronics_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_pt_electronics_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> PT -> PT-電子 -> 補單管理
    # def into_pt_electronics_replenishment_management(self):
    #     self.click_pt_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_pt_electronics_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_pt_electronics_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> PT -> PT-捕魚
    # def click_pt_fishing(self):
    #     self.click_pt()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_pt_fishing) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_pt_fishing)

    # # 運維管理 -> 外接平台 -> PT -> PT-捕魚 -> 遊戲列表
    # def into_pt_fishing_game_list(self):
    #     self.click_pt_fishing()
    #     self.click(OperationManagementPageLocator.menu_external_planform_pt_fishing_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_pt_fishing_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> PT -> PT-捕魚 -> 補單管理
    # def into_pt_fishing_replenishment_management(self):
    #     self.click_pt_fishing()
    #     self.click(OperationManagementPageLocator.menu_external_planform_pt_fishing_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_pt_fishing_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB
    # def click_sb(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sb) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sb):
    #             self.click(OperationManagementPageLocator.menu_external_planform_sb)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i == 2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> SB -> 頻道設定
    # def into_sb_channel_setting(self):
    #     self.click_sb()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> SB -> SB-虚拟体育2
    # def click_sb_virtual_sport_two(self):
    #     self.click_sb()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sb_virtual_sport_two) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_virtual_sport_two)

    # # 運維管理 -> 外接平台 -> SB -> SB-虚拟体育2 -> 遊戲列表
    # def into_sb_virtual_sport_two_game_list(self):
    #     self.click_sb_virtual_sport_two()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_virtual_sport_two_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_virtual_sport_two_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-虚拟体育2 -> 補單管理
    # def into_sb_virtual_sport_two_replenishment_management(self):
    #     self.click_sb_virtual_sport_two()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_virtual_sport_two_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_virtual_sport_two_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-虚拟体育
    # def click_sb_virtual_sport(self):
    #     self.click_sb()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sb_virtual_sport) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_virtual_sport)

    # # 運維管理 -> 外接平台 -> SB -> SB-虚拟体育 -> 遊戲列表
    # def into_sb_virtual_sport_game_list(self):
    #     self.click_sb_virtual_sport()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_virtual_sport_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_virtual_sport_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-虚拟体育 -> 補單管理
    # def into_sb_virtual_sport_replenishment_management(self):
    #     self.click_sb_virtual_sport()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_virtual_sport_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_virtual_sport_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-体育
    # def click_sb_sport(self):
    #     self.click_sb()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sb_sport) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_sport)

    # # 運維管理 -> 外接平台 -> SB -> SB-体育 -> 遊戲列表
    # def into_sb_sport_game_list(self):
    #     self.click_sb_sport()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_sport_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_sport_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-体育 -> 補單管理
    # def into_sb_sport_replenishment_management(self):
    #     self.click_sb_sport()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_sport_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_sport_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-百练赛
    # def click_sb_practice(self):
    #     self.click_sb()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sb_practice) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_practice)

    # # 運維管理 -> 外接平台 -> SB -> SB-百练赛 -> 遊戲列表
    # def into_sb_practice_game_list(self):
    #     self.click_sb_practice()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_practice_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_practice_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-百练赛 -> 補單管理
    # def into_sb_practice_replenishment_management(self):
    #     self.click_sb_practice()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_practice_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_practice_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-捕鱼
    # def click_sb_fishing(self):
    #     self.click_sb()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sb_fishing) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_fishing)

    # # 運維管理 -> 外接平台 -> SB -> SB-捕鱼 -> 遊戲列表
    # def into_sb_fishing_game_list(self):
    #     self.click_sb_fishing()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_fishing_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_fishing_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-捕鱼 -> 補單管理
    # def into_sb_fishing_replenishment_management(self):
    #     self.click_sb_fishing()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_fishing_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_fishing_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-电子
    # def click_sb_electronics(self):
    #     self.click_sb()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sb_electronics) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_electronics)

    # # 運維管理 -> 外接平台 -> SB -> SB-电子 -> 遊戲列表
    # def into_sb_electronics_game_list(self):
    #     self.click_sb_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_electronics_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_electronics_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SB -> SB-电子 -> 補單管理
    # def into_sb_electronics_replenishment_management(self):
    #     self.click_sb_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sb_electronics_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sb_electronics_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> 3S
    # def click_ss(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_3s) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_3s):
    #             self.click(OperationManagementPageLocator.menu_external_planform_3s)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i ==2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> 3S -> 頻道設定
    # def into_3s_channel_setting(self):
    #     self.click_ss()
    #     self.click(OperationManagementPageLocator.menu_external_planform_3s_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_3s_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> 3S -> 3S-体育
    # def click_3s_sport(self):
    #     self.click_ss()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_3s_sport) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_3s_sport)

    # # 運維管理 -> 外接平台 -> 3S -> 3S-体育 -> 遊戲列表
    # def into_3s_sport_game_list(self):
    #     self.click_3s_sport()
    #     self.click(OperationManagementPageLocator.menu_external_planform_3s_sport_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_3s_sport_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> 3S -> 3S-体育 -> 補單管理
    # def into_3s_sport_replenishment_management(self):
    #     self.click_3s_sport()
    #     self.click(OperationManagementPageLocator.menu_external_planform_3s_sport_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_3s_sport_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SW
    # def click_sw(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sw) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sw):
    #             self.click(OperationManagementPageLocator.menu_external_planform_sw)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i ==2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> SW -> 頻道設定
    # def into_sw_channel_setting(self):
    #     self.click_sw()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sw_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sw_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> SW -> SW-电子
    # def click_sw_electronics(self):
    #     self.click_sw()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_sw_electronics) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_sw_electronics)

    # # 運維管理 -> 外接平台 -> SW -> SW-电子 -> 遊戲列表
    # def into_sw_electronics_game_list(self):
    #     self.click_sw_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sw_electronics_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sw_electronics_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> SW -> SW-电子 -> 補單管理
    # def into_sw_electronics_replenishment_management(self):
    #     self.click_sw_electronics()
    #     self.click(OperationManagementPageLocator.menu_external_planform_sw_electronics_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_sw_electronics_replenishment_management)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> VG
    # def click_vg(self):
    #     self.click_external_planform_operation()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_vg) is True:
    #             break
    #         self.sleep(5)
        
    #     for i in range(0, 3):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_vg):
    #             self.click(OperationManagementPageLocator.menu_external_planform_vg)
    #             break
    #         else:
    #             self.sleep(1)

    #         if i ==2:
    #             raise EOFError('點擊第三方錯誤')

    # # 運維管理 -> 外接平台 -> VG -> 頻道設定
    # def into_vg_channel_setting(self):
    #     self.click_vg()
    #     self.click(OperationManagementPageLocator.menu_external_planform_vg_channel_setting)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_vg_channel_setting)
    #     self.wait_loading_finish()
    
    # # 運維管理 -> 外接平台 -> VG -> VG-棋牌
    # def click_vg_chess(self):
    #     self.click_vg()
    #     for _ in range(0, 2):
    #         if self.is_element_finded(OperationManagementPageLocator.menu_external_planform_vg_chess) is True:
    #             break
    #         self.sleep(5)
    #     self.click(OperationManagementPageLocator.menu_external_planform_vg_chess)

    # # 運維管理 -> 外接平台 -> VG -> VG-棋牌 -> 遊戲列表
    # def into_vg_chess_game_list(self):
    #     self.click_vg_chess()
    #     self.click(OperationManagementPageLocator.menu_external_planform_vg_chess_game_list)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_vg_chess_game_list)
    #     self.wait_loading_finish()

    # # 運維管理 -> 外接平台 -> VG -> VG-棋牌 -> 補單管理
    # def into_vg_chess_replenishment_management(self):
    #     self.click_vg_chess()
    #     self.click(OperationManagementPageLocator.menu_external_planform_vg_chess_replenishment_management)
    #     self.wait_visibility(OperationManagementPageLocator.ok_point_external_planform_vg_chess_replenishment_management)
    #     self.wait_loading_finish()

    # 五分彩種
    def click_five_min_ticket(self):
        self.click_external_planform_operation()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_five_min_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_five_min_ticket)

    # 五分彩種 -> 極速六合彩
    def click_js6_ticket(self):
        self.click_five_min_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_five_min_js6_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_five_min_js6_ticket)

    # 五分彩種 -> 極速六合彩 -> 期數管理
    def into_js6_period_management(self):
        self.click_js6_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_js6_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_js6_ticket_period_management)
        self.wait_loading_finish()

    # 五分彩種 -> 極速六合彩 -> 盤口管理
    def into_js6_odds_management(self):
        self.click_js6_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_js6_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_js6_ticket_handicap_management)
        self.wait_loading_finish()
        
    # 五分彩種 -> 極速六合彩 -> 投注限額
    def into_js6_bet_limit(self):
        self.click_js6_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_js6_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_js6_ticket_bet_limit)
        self.wait_loading_finish()
        
    # 五分彩種 -> 極速六合彩 -> 遊戲設置
    def into_js6_game_setting(self):
        self.click_js6_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_js6_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_js6_ticket_game_setting)
        self.wait_loading_finish()
        
    # 五分彩種 -> 五分快3
    def click_k3_ticket(self):
        self.click_five_min_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_five_min_k3_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_five_min_k3_ticket)

    # 五分彩種 -> 五分快3 -> 期數管理
    def into_k3_period_management(self):
        self.click_k3_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_k3_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_k3_ticket_period_management)
        self.wait_loading_finish()

    # 五分彩種 -> 五分快3 -> 盤口管理
    def into_k3_handicap_management(self):
        self.click_k3_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_k3_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_k3_ticket_handicap_management)
        self.wait_loading_finish()
        
    # 五分彩種 -> 五分快3 -> 投注限額
    def into_k3_bet_limit(self):
        self.click_k3_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_k3_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_k3_ticket_bet_limit)
        self.wait_loading_finish()
       
    # 五分彩種 -> 五分快3 -> 遊戲設置
    def into_k3_game_setting(self):
        self.click_k3_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_k3_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_k3_ticket_game_setting)
        self.wait_loading_finish()

    # 五分彩種 -> 五分PK拾
    def click_pk10_ticket(self):
        self.click_five_min_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_five_min_pk10_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_five_min_pk10_ticket)

    # 五分彩種 -> 五分PK拾 -> 期數管理
    def into_pk10_period_management(self):
        self.click_pk10_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_pk10_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_pk10_ticket_period_management)
        self.wait_loading_finish()

    # 五分彩種 -> 五分PK拾 -> 盤口管理
    def into_pk10_handicap_management(self):
        self.click_pk10_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_pk10_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_pk10_ticket_handicap_management)
        self.wait_loading_finish()

    # 五分彩種 -> 五分PK拾 -> 投注限額
    def into_pk10_bet_limit(self):
        self.click_pk10_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_pk10_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_pk10_ticket_bet_limit)
        self.wait_loading_finish()

    # 五分彩種 -> 五分PK拾 -> 遊戲設置
    def into_pk10_game_setting(self):
        self.click_pk10_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_pk10_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_pk10_ticket_game_setting)
        self.wait_loading_finish()

    # 五分彩種 -> 五分時時彩
    def click_ssc_ticket(self):
        self.click_five_min_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_five_min_ssc_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_five_min_ssc_ticket)

    # 五分彩種 -> 五分時時彩 -> 期數管理
    def into_ssc_period_management(self):
        self.click_ssc_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_ssc_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_ssc_ticket_period_management)
        self.wait_loading_finish()

    # 五分彩種 -> 五分時時彩 -> 盤口管理
    def into_ssc_handicap_management(self):
        self.click_ssc_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_ssc_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_ssc_ticket_handicap_management)
        self.wait_loading_finish()

    # 五分彩種 -> 五分時時彩 -> 投注限額
    def into_ssc_bet_limit(self):
        self.click_ssc_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_ssc_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_ssc_ticket_bet_limit)
        self.wait_loading_finish()

    # 五分彩種 -> 五分時時彩 -> 遊戲設置
    def into_ssc_game_setting(self):
        self.click_ssc_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_ssc_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_ssc_ticket_game_setting)
        self.wait_loading_finish()

    # 五分彩種 -> 五分幸運28
    def click_xy28_ticket(self):
        self.click_five_min_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_five_min_xy28_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_five_min_xy28_ticket)

    # 五分彩種 -> 五分幸運28 -> 期數管理
    def into_xy28_period_management(self):
        self.click_xy28_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_xy28_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_xy28_ticket_period_management)
        self.wait_loading_finish()

    # 五分彩種 -> 五分幸運28 -> 盤口管理
    def into_xy28_handicap_management(self):
        self.click_xy28_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_xy28_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_xy28_ticket_handicap_management)
        self.wait_loading_finish()

    # 五分彩種 -> 五分幸運28 -> 投注限額
    def into_xy28_bet_limit(self):
        self.click_xy28_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_xy28_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_xy28_ticket_bet_limit)
        self.wait_loading_finish()

    # 五分彩種 -> 五分幸運28 -> 遊戲設置
    def into_xy28_game_setting(self):
        self.click_xy28_ticket()
        self.click(OperationManagementPageLocator.menu_five_min_xy28_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_five_min_xy28_ticket_game_setting)
        self.wait_loading_finish()

    # 三分彩種
    def click_three_min_ticket(self):
        self.click_external_planform_operation()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_three_min_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_three_min_ticket)

    # 三分彩種 -> 三分六合彩
    def click_3f6_ticket(self):
        self.click_three_min_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_three_min_3f6_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_three_min_3f6_ticket)

    # 三分彩種 -> 三分六合彩 -> 期數管理
    def into_3f6_period_management(self):
        self.click_3f6_ticket()
        self.click(OperationManagementPageLocator.menu_three_min_3f6_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_three_min_3f6_ticket_period_management)
        self.wait_loading_finish()

    # 三分彩種 -> 三分六合彩 -> 盤口管理
    def into_3f6_handicap_management(self):
        self.click_3f6_ticket()
        self.click(OperationManagementPageLocator.menu_three_min_3f6_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_three_min_3f6_ticket_handicap_management)
        self.wait_loading_finish()

    # 三分彩種 -> 三分六合彩 -> 投注限額
    def into_3f6_bet_limit(self):
        self.click_3f6_ticket()
        self.click(OperationManagementPageLocator.menu_three_min_3f6_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_three_min_3f6_ticket_bet_limit)
        self.wait_loading_finish()

    # 三分彩種 -> 三分六合彩 -> 遊戲設置
    def into_3f6_game_setting(self):
        self.click_3f6_ticket()
        self.click(OperationManagementPageLocator.menu_three_min_3f6_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_three_min_3f6_ticket_game_setting)
        self.wait_loading_finish()

    # 香港彩票
    def click_hongkong_ticket(self):
        self.click_external_planform_operation()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_hongkong_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_hongkong_ticket)


    # 香港彩票 -> 香港六合彩
    def click_hk6_ticket(self):
        self.click_hongkong_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_hongkong_hk6_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_hongkong_hk6_ticket)

    # 香港彩票 -> 香港六合彩 -> 期數管理
    def into_hk6_period_management(self):
        self.click_hk6_ticket()
        self.click(OperationManagementPageLocator.menu_hongkong_hk6_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_hongkong_hk6_ticket_period_management)
        self.wait_loading_finish()

    # 香港彩票 -> 香港六合彩 -> 盤口管理
    def into_hk6_handicap_management(self):
        self.click_hk6_ticket()
        self.click(OperationManagementPageLocator.menu_hongkong_hk6_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_hongkong_hk6_ticket_handicap_management)
        self.wait_loading_finish()

    # 香港彩票 -> 香港六合彩 -> 投注限額
    def into_hk6_bet_limit(self):
        self.click_hk6_ticket()
        self.click(OperationManagementPageLocator.menu_hongkong_hk6_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_hongkong_hk6_ticket_bet_limit)
        self.wait_loading_finish()

    # 香港彩票 -> 香港六合彩 -> 遊戲設置
    def into_hk6_game_setting(self):
        self.click_hk6_ticket()
        self.click(OperationManagementPageLocator.menu_hongkong_hk6_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_hongkong_hk6_ticket_game_setting)
        self.wait_loading_finish()

    # 福彩/體彩
    def click_welfare_sport_ticket(self):
        self.click_external_planform_operation()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_welfare_sport_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_welfare_sport_ticket)

    # 福彩/體彩 -> 福彩3D
    def click_fc3d_ticket(self):
        self.click_welfare_sport_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_welfare_sport_fc3d_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_welfare_sport_fc3d_ticket)

    # 福彩/體彩 -> 福彩3D -> 期數管理
    def into_fc3d_period_management(self):
        self.click_fc3d_ticket()
        self.click(OperationManagementPageLocator.menu_welfare_sport_fc3d_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_welfare_sport_fc3d_ticket_period_management)
        self.wait_loading_finish()

    # 福彩/體彩 -> 福彩3D -> 盤口管理
    def into_fc3d_handicap_management(self):
        self.click_fc3d_ticket()
        self.click(OperationManagementPageLocator.menu_welfare_sport_fc3d_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_welfare_sport_fc3d_ticket_handicap_management)
        self.wait_loading_finish()

    # 福彩/體彩 -> 福彩3D -> 投注限額
    def into_fc3d_bet_limit(self):
        self.click_fc3d_ticket()
        self.click(OperationManagementPageLocator.menu_welfare_sport_fc3d_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_welfare_sport_fc3d_ticket_bet_limit)
        self.wait_loading_finish()

    # 福彩/體彩 -> 福彩3D -> 遊戲設置
    def into_fc3d_game_setting(self):
        self.click_fc3d_ticket()
        self.click(OperationManagementPageLocator.menu_welfare_sport_fc3d_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_welfare_sport_fc3d_ticket_game_setting)
        self.wait_loading_finish()

    # 福彩/體彩 -> 排列三
    def click_pl3_ticket(self):
        self.click_welfare_sport_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_welfare_sport_pl3_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_welfare_sport_pl3_ticket)

    # 福彩/體彩 -> 排列三 -> 期數管理
    def into_pl3_period_management(self):
        self.click_pl3_ticket()
        self.click(OperationManagementPageLocator.menu_welfare_sport_pl3_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_welfare_sport_pl3_ticket_period_management)
        self.wait_loading_finish()

    # 福彩/體彩 -> 排列三 -> 盤口管理
    def into_pl3_handicap_management(self):
        self.click_pl3_ticket()
        self.click(OperationManagementPageLocator.menu_welfare_sport_pl3_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_welfare_sport_pl3_ticket_handicap_management)
        self.wait_loading_finish()

    # 福彩/體彩 -> 排列三 -> 投注限額
    def into_pl3_bet_limit(self):
        self.click_pl3_ticket()
        self.click(OperationManagementPageLocator.menu_welfare_sport_pl3_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_welfare_sport_pl3_ticket_bet_limit)
        self.wait_loading_finish()

    # 福彩/體彩 -> 排列三 -> 遊戲設置
    def into_pl3_game_setting(self):
        self.click_pl3_ticket()
        self.click(OperationManagementPageLocator.menu_welfare_sport_pl3_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_welfare_sport_pl3_ticket_game_setting)
        self.wait_loading_finish()

    # 極速彩種
    def click_exteremespeed_ticket(self):
        self.click_external_planform_operation()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_exteremespeed_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_exteremespeed_ticket)

    # 極速彩種 -> 分分六合彩
    def click_ff6_ticket(self):
        self.click_exteremespeed_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_exteremespeed_ff6_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_exteremespeed_ff6_ticket)

    # 極速彩種 -> 分分六合彩 -> 期數管理
    def into_ff6_period_management(self):
        self.click_ff6_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_ff6_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_ff6_ticket_period_management)
        self.wait_loading_finish()

    # 極速彩種 -> 分分六合彩 -> 盤口管理
    def into_ff6_handicap_management(self):
        self.click_ff6_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_ff6_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_ff6_ticket_handicap_management)
        self.wait_loading_finish()

    # 極速彩種 -> 分分六合彩 -> 投注限額
    def into_ff6_bet_limit(self):
        self.click_ff6_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_ff6_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_ff6_ticket_bet_limit)
        self.wait_loading_finish()

    # 極速彩種 -> 分分六合彩 -> 遊戲設置
    def into_ff6_game_setting(self):
        self.click_ff6_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_ff6_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_ff6_ticket_game_setting)
        self.wait_loading_finish()

    # 極速彩種 -> 極速時時彩
    def click_jsssc_ticket(self):
        self.click_exteremespeed_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_exteremespeed_jsssc_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_exteremespeed_jsssc_ticket)

    # 極速彩種 -> 極速時時彩 -> 期數管理
    def into_jsssc_period_management(self):
        self.click_jsssc_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jsssc_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jsssc_ticket_period_management)
        self.wait_loading_finish()

    # 極速彩種 -> 極速時時彩 -> 盤口管理
    def into_jsssc_handicap_management(self):
        self.click_jsssc_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jsssc_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jsssc_ticket_handicap_management)
        self.wait_loading_finish()

    # 極速彩種 -> 極速時時彩 -> 投注限額
    def into_jsssc_bet_limit(self):
        self.click_jsssc_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jsssc_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jsssc_ticket_bet_limit)
        self.wait_loading_finish()

    # 極速彩種 -> 極速時時彩 -> 遊戲設置
    def into_jsssc_game_setting(self):
        self.click_jsssc_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jsssc_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jsssc_ticket_game_setting)
        self.wait_loading_finish()

    # 極速彩種 -> 極速PK拾
    def click_jspk10_ticket(self):
        self.click_exteremespeed_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_exteremespeed_jspk10_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_exteremespeed_jspk10_ticket)

    # 極速彩種 -> 極速PK拾 -> 期數管理
    def into_jspk10_period_management(self):
        self.click_jspk10_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jspk10_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jspk10_ticket_period_management)
        self.wait_loading_finish()

    # 極速彩種 -> 極速PK拾 -> 盤口管理
    def into_jspk10_handicap_management(self):
        self.click_jspk10_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jspk10_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jspk10_ticket_handicap_management)
        self.wait_loading_finish()

    # 極速彩種 -> 極速PK拾 -> 投注限額
    def into_jspk10_bet_limit(self):
        self.click_jspk10_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jspk10_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jspk10_ticket_bet_limit)
        self.wait_loading_finish()

    # 極速彩種 -> 極速PK拾 -> 遊戲設置
    def into_jspk10_game_setting(self):
        self.click_jspk10_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jspk10_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jspk10_ticket_game_setting)
        self.wait_loading_finish()

    # 極速彩種 -> 極速快3
    def click_jisuk3_ticket(self):
        self.click_exteremespeed_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_exteremespeed_jisuk3_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_exteremespeed_jisuk3_ticket)

    # 極速彩種 -> 極速快3 -> 期數管理
    def into_jisuk3_period_management(self):
        self.click_jisuk3_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jisuk3_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jisuk3_ticket_period_management)
        self.wait_loading_finish()

    # 極速彩種 -> 極速快3 -> 盤口管理
    def into_jisuk3_handicap_management(self):
        self.click_jisuk3_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jisuk3_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jisuk3_ticket_handicap_management)
        self.wait_loading_finish()

    # 極速彩種 -> 極速快3 -> 投注限額
    def into_jisuk3_bet_limit(self):
        self.click_jisuk3_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jisuk3_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jisuk3_ticket_bet_limit)
        self.wait_loading_finish()

    # 極速彩種 -> 極速快3 -> 遊戲設置
    def into_jisuk3_game_setting(self):
        self.click_jisuk3_ticket()
        self.click(OperationManagementPageLocator.menu_exteremespeed_jisuk3_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_exteremespeed_jisuk3_ticket_game_setting)
        self.wait_loading_finish()

    # 高頻彩種
    def click_high_ticket(self):
        self.click_external_planform_operation()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_high_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_high_ticket)

    # 高頻彩種 -> 11選5
    def click_11x5_ticket(self):
        self.click_high_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_high_11x5_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_high_11x5_ticket)

    # 高頻彩種 -> 其他
    def click_other_ticket(self):
        self.click_high_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_high_other_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_high_other_ticket)

    # 高頻彩種 -> 其他 -> 幸運飛艇
    def click_luckyairship_ticket(self):
        self.click_other_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_high_other_lucky_airship_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_high_other_lucky_airship_ticket)

    # 高頻彩種 -> 其他 -> 幸運飛艇 -> 期數管理
    def into_luckyairship_period_management(self):
        self.click_luckyairship_ticket()
        self.click(OperationManagementPageLocator.menu_high_other_lucky_airship_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_other_lucky_airship_ticket_period_management)
        self.wait_loading_finish()

    # 高頻彩種 -> 其他 -> 幸運飛艇 -> 盤口管理
    def into_luckyairship_handicap_management(self):
        self.click_luckyairship_ticket()
        self.click(OperationManagementPageLocator.menu_high_other_lucky_airship_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_other_lucky_airship_ticket_handicap_management)
        self.wait_loading_finish()

    # 高頻彩種 -> 其他 -> 幸運飛艇 -> 投注限額
    def into_luckyairship_bet_limit(self):
        self.click_luckyairship_ticket()
        self.click(OperationManagementPageLocator.menu_high_other_lucky_airship_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_other_lucky_airship_ticket_bet_limit)
        self.wait_loading_finish()

    # 高頻彩種 -> 其他 -> 幸運飛艇 -> 遊戲設置
    def into_luckyairship_game_setting(self):
        self.click_luckyairship_ticket()
        self.click(OperationManagementPageLocator.menu_high_other_lucky_airship_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_other_lucky_airship_ticket_game_setting)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28
    def click_highxy28_ticket(self):
        self.click_high_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_high_xy28_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_high_xy28_ticket)

    # 高頻彩種 -> 幸運28 -> PC蛋蛋
    def click_pc_ticket(self):
        self.click_highxy28_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_high_xy28_pc_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_high_xy28_pc_ticket)

    # 高頻彩種 -> 幸運28 -> PC蛋蛋 -> 期數管理
    def into_pc_period_management(self):
        self.click_pc_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_pc_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_pc_ticket_period_management)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> PC蛋蛋 -> 盤口管理
    def into_pc_handicap_management(self):
        self.click_pc_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_pc_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_pc_ticket_handicap_management)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> PC蛋蛋 -> 投注限額
    def into_pc_bet_limit(self):
        self.click_pc_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_pc_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_pc_ticket_bet_limit)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> PC蛋蛋 -> 遊戲設置
    def into_pc_game_setting(self):
        self.click_pc_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_pc_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_pc_ticket_game_setting)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> 台灣幸運28
    def click_tw_ticket(self):
        self.click_highxy28_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_high_xy28_tw_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_high_xy28_tw_ticket)

    # 高頻彩種 -> 幸運28 -> 台灣幸運28 -> 期數管理
    def into_tw_period_management(self):
        self.click_tw_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_tw_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_tw_ticket_period_management)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> 台灣幸運28 -> 盤口管理
    def into_tw_handicap_management(self):
        self.click_tw_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_tw_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_tw_ticket_handicap_management)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> 台灣幸運28 -> 投注限額
    def into_tw_bet_limit(self):
        self.click_tw_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_tw_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_tw_ticket_bet_limit)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> 台灣幸運28 -> 遊戲設置
    def into_tw_game_setting(self):
        self.click_tw_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_tw_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_tw_ticket_game_setting)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> 加拿大幸運28
    def click_canada_ticket(self):
        self.click_highxy28_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_high_xy28_canada_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_high_xy28_canada_ticket)

    # 高頻彩種 -> 幸運28 -> 加拿大幸運28 -> 期數管理
    def into_canada_period_management(self):
        self.click_canada_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_canada_ticket_period_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_canada_ticket_period_management)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> 加拿大幸運28 -> 盤口管理
    def into_canada_handicap_management(self):
        self.click_canada_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_canada_ticket_handicap_management)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_canada_ticket_handicap_management)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> 加拿大幸運28 -> 投注限額
    def into_canada_bet_limit(self):
        self.click_canada_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_canada_ticket_bet_limit)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_canada_ticket_bet_limit)
        self.wait_loading_finish()

    # 高頻彩種 -> 幸運28 -> 加拿大幸運28 -> 遊戲設置
    def into_canada_game_setting(self):
        self.click_canada_ticket()
        self.click(OperationManagementPageLocator.menu_high_xy28_canada_ticket_game_setting)
        self.wait_visibility(OperationManagementPageLocator.ok_point_high_xy28_canada_ticket_game_setting)
        self.wait_loading_finish()

    # 高頻彩種 -> 快3
    def click_highk3_ticket(self):
        self.click_high_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_high_k3_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_high_k3_ticket)

    # 高頻彩種 -> 時時彩
    def click_highssc_Ticket(self):
        self.click_high_ticket()
        for _ in range(0, 2):
            if self.is_element_finded(OperationManagementPageLocator.menu_high_ssc_ticket) is True:
                break
            self.sleep(5)
        self.click(OperationManagementPageLocator.menu_high_ssc_ticket)

    # 紅包
    def click_red_envelope(self):
        self.click_operation_managenent()
        self.click(OperationManagementPageLocator.red_envelope)

    # 紅包 -> 掃雷
    def click_mine_sweeping(self):
        self.click_red_envelope()
        self.click(OperationManagementPageLocator.mine_sweeping)

    # 紅包 -> 掃雷 -> 開局管理
    def into_mine_sweeping_opening_management(self):
        self.click_mine_sweeping()
        self.click(OperationManagementPageLocator.mine_sweeping_opening_management)

    # 紅包 -> 掃雷 -> 廳別管理
    def into_mine_sweeping_hall_management(self):
        self.click_mine_sweeping()
        self.click(OperationManagementPageLocator.mine_sweeping_hall_management)

    # 紅包 -> 掃雷 -> 遊戲設置
    def into_mine_sweeping_game_setting(self):
        self.click_mine_sweeping()
        self.click(OperationManagementPageLocator.mine_sweeping_game_setting)

    # 紅包 -> 掃雷 -> 玩家自訂
    def into_mine_sweeping_player_custom(self):
        self.click_mine_sweeping()
        self.click(OperationManagementPageLocator.mine_sweeping_player_custom)

    # 紅包 -> 牛牛
    def click_niu_niu(self):
        self.click_red_envelope()
        self.click(OperationManagementPageLocator.niu_niu)

    # 紅包 -> 牛牛 -> 開局管理
    def into_niu_niu_opening_management(self):
        self.click_niu_niu()
        self.click(OperationManagementPageLocator.niu_niu_opening_management)

    # 紅包 -> 牛牛 -> 廳別管理
    def into_niu_niu_hall_management(self):
        self.click_niu_niu()
        self.click(OperationManagementPageLocator.niu_niu_hall_management)

    # 紅包 -> 牛牛 -> 遊戲設置
    def into_niu_niu_game_setting(self):
        self.click_niu_niu()
        self.click(OperationManagementPageLocator.niu_niu_game_setting)

    # 紅包 -> 牛牛 -> 玩家自訂
    def into_niu_niu_player_custom(self):
        self.click_niu_niu()
        self.click(OperationManagementPageLocator.niu_niu_player_custom)
