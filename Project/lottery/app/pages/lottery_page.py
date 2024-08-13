from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base

class LotteryPageLocator:
    base = Xpath_Base()

    a_wfk3 = base.check_device( # 五分快3
        Android = base.data_collation(type_kind='name', type_name='wfk3'),
        iOS = base.data_collation(type_kind='name', type_name='wfk3')
    )

    a_jisuk3 = base.check_device( # 極速快3
        Android = base.data_collation(type_kind='name', type_name='jisuk3'),
        iOS = base.data_collation(type_kind='name', type_name='jisuk3')
    )

    a_wfxy28 = base.check_device( # 五分幸運28
        Android = base.data_collation(type_kind='name', type_name='wfxy28'),
        iOS = base.data_collation(type_kind='name', type_name='wfxy28')
    )

    a_wfpk10 = base.check_device( # 五分PK十
        Android = base.data_collation(type_kind='name', type_name='wfpk10'),
        iOS = base.data_collation(type_kind='name', type_name='wfpk10')
    )

    a_wfssc = base.check_device( # 五分時時彩
        Android = base.data_collation(type_kind='name', type_name='wfssc'),
        iOS = base.data_collation(type_kind='name', type_name='wfssc')
    )

    a_jspk10 = base.check_device( # 極速PK拾
        Android = base.data_collation(type_kind='name', type_name='jspk10'),
        iOS = base.data_collation(type_kind='name', type_name='jspk10')
    )

    a_jsssc = base.check_device( # 極速時時彩
        Android = base.data_collation(type_kind='name', type_name='jsssc'),
        iOS = base.data_collation(type_kind='name', type_name='jsssc')
    )

    a_js6 = base.check_device( # 極速六合彩
        Android = base.data_collation(type_kind='name', type_name='js6'),
        iOS = base.data_collation(type_kind='name', type_name='js6')
    )

    a_ahk3 = base.check_device( # 安徽快三
        Android = base.data_collation(type_kind='name', type_name='ahk3'),
        iOS = base.data_collation(type_kind='name', type_name='ahk3')
    )

    a_hk = base.check_device( # 香港六合彩
        Android = base.data_collation(type_kind='name', type_name='hk'),
        iOS = base.data_collation(type_kind='name', type_name='hk')
    )

    a_xjssc = base.check_device( # 新疆時時彩
        Android = base.data_collation(type_kind='name', type_name='xjssc'),
        iOS = base.data_collation(type_kind='name', type_name='xjssc')
    )

    a_cqssc = base.check_device( # 重慶時時彩
        Android = base.data_collation(type_kind='name', type_name='cqssc'),
        iOS = base.data_collation(type_kind='name', type_name='cqssc')
    )

    a_bjpk10 = base.check_device( # 北京PK拾
        Android = base.data_collation(type_kind='name', type_name='bjpk10'),
        iOS = base.data_collation(type_kind='name', type_name='bjpk10')
    )

    a_bjxy28 = base.check_device( # PC蛋蛋
        Android = base.data_collation(type_kind='name', type_name='bjxy28'),
        iOS = base.data_collation(type_kind='name', type_name='bjxy28')
    )

    a_twxy28 = base.check_device( # 台灣幸運28
        Android = base.data_collation(type_kind='name', type_name='twxy28'),
        iOS = base.data_collation(type_kind='name', type_name='twxy28')
    )

    a_malxyft = base.check_device( # 幸運飛艇
        Android = base.data_collation(type_kind='name', type_name='malxyft'),
        iOS = base.data_collation(type_kind='name', type_name='malxyft')
    )

    a_gd11x5 = base.check_device( # 台灣幸運28
        Android = base.data_collation(type_kind='name', type_name='gd11x5'),
        iOS = base.data_collation(type_kind='name', type_name='gd11x5')
    )

    a_xjpxy28 = base.check_device( # 新加玻幸運28
        Android = base.data_collation(type_kind='name', type_name='xjpxy28'),
        iOS = base.data_collation(type_kind='name', type_name='xjpxy28')
    )

    a_jndbsxy28 = base.check_device( # 加拿大幸運28
        Android = base.data_collation(type_kind='name', type_name='jndbsxy28'),
        iOS = base.data_collation(type_kind='name', type_name='jndbsxy28')
    )

    a_jisu11x5 = base.check_device( # 極速11選5
        Android = base.data_collation(type_kind='name', type_name='jisu11x5'),
        iOS = base.data_collation(type_kind='name', type_name='jisu11x5')
    )

    a_sf11x5 = base.check_device( # 三分11選5
        Android = base.data_collation(type_kind='name', type_name='sf11x5'),
        iOS = base.data_collation(type_kind='name', type_name='sf11x5')
    )

    a_wf11x5 = base.check_device( # 五分11選5
        Android = base.data_collation(type_kind='name', type_name='wf11x5'),
        iOS = base.data_collation(type_kind='name', type_name='wf11x5')
    )

    a_hbk3 = base.check_device( # 湖北快三
        Android = base.data_collation(type_kind='name', type_name='btn_hbk3'),
        iOS = base.data_collation(type_kind='name', type_name='btn_hbk3')
    )

    a_fc3d = base.check_device( # 福彩3D
        Android = base.data_collation(type_kind='name', type_name='fc3d'),
        iOS = base.data_collation(type_kind='name', type_name='fc3d')
    )

    a_shssc = base.check_device( # 上海時時樂
        Android = base.data_collation(type_kind='name', type_name='shssc'),
        iOS = base.data_collation(type_kind='name', type_name='shssc')
    )

    a_pl3 = base.check_device( # 排列三
        Android = base.data_collation(type_kind='name', type_name='pl3'),
        iOS = base.data_collation(type_kind='name', type_name='pl3')
    )

    a_jsk3 = base.check_device( # 江蘇快3
        Android = base.data_collation(type_kind='name', type_name='jsk3'),
        iOS = base.data_collation(type_kind='name', type_name='jsk3')
    )

    a_shk3 = base.check_device( # 上海快3
        Android = base.data_collation(type_kind='name', type_name='shk3'),
        iOS = base.data_collation(type_kind='name', type_name='shk3')
    )

    a_hebk3 = base.check_device( # 河北快3
        Android = base.data_collation(type_kind='name', type_name='hebk3'),
        iOS = base.data_collation(type_kind='name', type_name='hebk3')
    )

    a_gxk3 = base.check_device( # 廣西快3
        Android = base.data_collation(type_kind='name', type_name='gxk3'),
        iOS = base.data_collation(type_kind='name', type_name='gxk3')
    )

    b_wfk3 = base.check_device( # 五分快3
        Android = base.data_collation(type_kind='name', type_name='btn_wfk3'),
        iOS = base.data_collation(type_kind='name', type_name='btn_wfk3')
    )

    b_jisuk3 = base.check_device( # 極速快3
        Android = base.data_collation(type_kind='name', type_name='btn_jisuk3'),
        iOS = base.data_collation(type_kind='name', type_name='btn_jisuk3')
    )

    b_wfxy28 = base.check_device( # 五分幸運28
        Android = base.data_collation(type_kind='name', type_name='btn_wfxy28'),
        iOS = base.data_collation(type_kind='name', type_name='btn_wfxy28')
    )

    b_wfpk10 = base.check_device( # 五分PK十
        Android = base.data_collation(type_kind='name', type_name='btn_wfpk10'),
        iOS = base.data_collation(type_kind='name', type_name='btn_wfpk10')
    )

    b_wfssc = base.check_device( # 五分時時彩
        Android = base.data_collation(type_kind='name', type_name='btn_wfssc'),
        iOS = base.data_collation(type_kind='name', type_name='btn_wfssc')
    )

    b_jspk10 = base.check_device( # 極速PK拾
        Android = base.data_collation(type_kind='name', type_name='btn_jspk10'),
        iOS = base.data_collation(type_kind='name', type_name='btn_jspk10')
    )

    b_jsssc = base.check_device( # 極速時時彩
        Android = base.data_collation(type_kind='name', type_name='btn_jsssc'),
        iOS = base.data_collation(type_kind='name', type_name='btn_jsssc')
    )

    b_js6 = base.check_device( # 極速六合彩
        Android = base.data_collation(type_kind='name', type_name='btn_js6'),
        iOS = base.data_collation(type_kind='name', type_name='btn_js6')
    )

    b_ahk3 = base.check_device( # 安徽快三
        Android = base.data_collation(type_kind='name', type_name='btn_ahk3'),
        iOS = base.data_collation(type_kind='name', type_name='btn_ahk3')
    )

    b_hk = base.check_device( # 香港六合彩
        Android = base.data_collation(type_kind='name', type_name='btn_hk'),
        iOS = base.data_collation(type_kind='name', type_name='btn_hk')
    )

    b_xjssc = base.check_device( # 新疆時時彩
        Android = base.data_collation(type_kind='name', type_name='btn_xjssc'),
        iOS = base.data_collation(type_kind='name', type_name='btn_xjssc')
    )

    b_cqssc = base.check_device( # 重慶時時彩
        Android = base.data_collation(type_kind='name', type_name='btn_cqssc'),
        iOS = base.data_collation(type_kind='name', type_name='btn_cqssc')
    )

    b_bjpk10 = base.check_device( # 北京PK拾
        Android = base.data_collation(type_kind='name', type_name='btn_bjpk10'),
        iOS = base.data_collation(type_kind='name', type_name='btn_bjpk10')
    )

    b_bjxy28 = base.check_device( # PC蛋蛋
        Android = base.data_collation(type_kind='name', type_name='btn_bjxy28'),
        iOS = base.data_collation(type_kind='name', type_name='btn_bjxy28')
    )

    b_twxy28 = base.check_device( # 台灣幸運28
        Android = base.data_collation(type_kind='name', type_name='btn_twxy28'),
        iOS = base.data_collation(type_kind='name', type_name='btn_twxy28')
    )

    b_malxyft = base.check_device( # 幸運飛艇
        Android = base.data_collation(type_kind='name', type_name='btn_malxyft'),
        iOS = base.data_collation(type_kind='name', type_name='btn_malxyft')
    )

    b_gd11x5 = base.check_device( # 台灣幸運28
        Android = base.data_collation(type_kind='name', type_name='btn_gd11x5'),
        iOS = base.data_collation(type_kind='name', type_name='btn_gd11x5')
    )

    b_xjpxy28 = base.check_device( # 新加玻幸運28
        Android = base.data_collation(type_kind='name', type_name='btn_xjpxy28'),
        iOS = base.data_collation(type_kind='name', type_name='btn_xjpxy28')
    )

    b_jndbsxy28 = base.check_device( # 加拿大幸運28
        Android = base.data_collation(type_kind='name', type_name='btn_jndbsxy28'),
        iOS = base.data_collation(type_kind='name', type_name='btn_jndbsxy28')
    )

    b_jisu11x5 = base.check_device( # 極速11選5
        Android = base.data_collation(type_kind='name', type_name='btn_jisu11x5'),
        iOS = base.data_collation(type_kind='name', type_name='btn_jisu11x5')
    )

    b_sf11x5 = base.check_device( # 三分11選5
        Android = base.data_collation(type_kind='name', type_name='btn_sf11x5'),
        iOS = base.data_collation(type_kind='name', type_name='btn_sf11x5')
    )

    b_wf11x5 = base.check_device( # 五分11選5
        Android = base.data_collation(type_kind='name', type_name='btn_wf11x5'),
        iOS = base.data_collation(type_kind='name', type_name='btn_wf11x5')
    )

    b_hbk3 = base.check_device( # 湖北快三
        Android = base.data_collation(type_kind='name', type_name='btn_btn_hbk3'),
        iOS = base.data_collation(type_kind='name', type_name='btn_btn_hbk3')
    )

    b_fc3d = base.check_device( # 福彩3D
        Android = base.data_collation(type_kind='name', type_name='btn_fc3d'),
        iOS = base.data_collation(type_kind='name', type_name='btn_fc3d')
    )

    b_shssc = base.check_device( # 上海時時樂
        Android = base.data_collation(type_kind='name', type_name='btn_shssc'),
        iOS = base.data_collation(type_kind='name', type_name='btn_shssc')
    )

    b_pl3 = base.check_device( # 排列三
        Android = base.data_collation(type_kind='name', type_name='btn_pl3'),
        iOS = base.data_collation(type_kind='name', type_name='btn_pl3')
    )

    b_jsk3 = base.check_device( # 江蘇快3
        Android = base.data_collation(type_kind='name', type_name='btn_jsk3'),
        iOS = base.data_collation(type_kind='name', type_name='btn_jsk3')
    )

    b_shk3 = base.check_device( # 上海快3
        Android = base.data_collation(type_kind='name', type_name='btn_shk3'),
        iOS = base.data_collation(type_kind='name', type_name='btn_shk3')
    )

    b_hebk3 = base.check_device( # 河北快3
        Android = base.data_collation(type_kind='name', type_name='btn_hebk3'),
        iOS = base.data_collation(type_kind='name', type_name='btn_hebk3')
    )

    b_gxk3 = base.check_device( # 廣西快3
        Android = base.data_collation(type_kind='name', type_name='btn_gxk3'),
        iOS = base.data_collation(type_kind='name', type_name='btn_gxk3')
    )

    # 彩種入口
    pk10 = base.check_device( # PK10
        Android = base.data_collation(type_kind='text', type_name='PK10'),
        iOS = base.data_collation(type_kind='name', type_name='PK10')
    )

    mark6 = base.check_device( # 六合彩
        Android = base.data_collation(type_kind='text', type_name='六合彩'),
        iOS = base.data_collation(type_kind='name', type_name='六合彩')
    )

    eleven_x5 = base.check_device( # 11选5
        Android = base.data_collation(type_kind='text', type_name='11选5'),
        iOS = base.data_collation(type_kind='name', type_name='11选5')
    )

    k3 = base.check_device( # 快3
        Android = base.data_collation(type_kind='text', type_name='快3'),
        iOS = base.data_collation(type_kind='name', type_name='快3')
    )

    ssc = base.check_device( # 时时彩
        Android = base.data_collation(type_kind='text', type_name='时时彩'),
        iOS = base.data_collation(type_kind='name', type_name='时时彩')
    )

    xy28 = base.check_device( # 幸运28
        Android = base.data_collation(type_kind='text', type_name='幸运28'),
        iOS = base.data_collation(type_kind='name', type_name='幸运28')
    )

    general_lottery = base.check_device( # 一般彩票
        Android = base.data_collation(type_kind='text', type_name='一般彩票'),
        iOS = base.data_collation(type_kind='name', type_name='一般彩票')
    )

    # 彩票入口
    hk = base.check_device( 
        Android = base.data_collation(type_kind='text', type_name='香港六合彩'),
        iOS = base.data_collation(type_kind='name', type_name='香港六合彩')
    )
    
    wfssc = base.check_device( 
        Android = base.data_collation(type_kind='text', type_name='五分时时彩'),
        iOS = base.data_collation(type_kind='name', type_name='五分时时彩')
    )

    wfpk10 = base.check_device( 
        Android = base.data_collation(type_kind='text', type_name='五分PK拾'),
        iOS = base.data_collation(type_kind='name', type_name='五分PK拾')
    )

    twxy28 = base.check_device( 
        Android = base.data_collation(type_kind='text', type_name='台湾幸运28'),
        iOS = base.data_collation(type_kind='name', type_name='台湾幸运28')
    )

    wf11x5 = base.check_device( 
        Android = base.data_collation(type_kind='text', type_name='五分11选5'),
        iOS = base.data_collation(type_kind='name', type_name='五分11选5')
    )

    wfk3 = base.check_device( 
        Android = base.data_collation(type_kind='text', type_name='五分快3'),
        iOS = base.data_collation(type_kind='name', type_name='五分快3')
    )

    fc3d = base.check_device( 
        Android = base.data_collation(type_kind='text', type_name='福彩3D'),
        iOS = base.data_collation(type_kind='name', type_name='福彩3D')
    )

    close_announcement = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*ibClose'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*ibClose')
    )

    skip_change_password = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='暂不修改'),
        iOS = base.data_collation(type_kind='name', type_name='暂不修改')
    )

    close_mail = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='稍后阅读'),
        iOS = base.data_collation(type_kind='text', type_name='稍后阅读')
    )

    member = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*rvTabBar', action='child()[4]'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*rvTabBar', action='child()[4]')
    )

    bet_record = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='投注记录'),
        iOS = base.data_collation(type_kind='name', type_name='投注记录')
    )

    @staticmethod
    def bet_record_lottery(lottery_name):
        bet_record_lottery = LotteryPageLocator.base.check_device(
            Android = LotteryPageLocator.base.data_collation(type_kind='text', type_name=lottery_name),
            iOS = LotteryPageLocator.base.data_collation(type_kind='name', type_name=lottery_name)
        )
        return bet_record_lottery

class BaseLotteryPage(Base):
    def enter_lottery(self,game_name):
        self.common.sleep(3)
        
        if self.common.poco_exists(game_name):
            self.common.poco_click(game_name)
        else:
            for num in range(0, 12):
                self.common.go_down()
                self.common.sleep(2)

                if self.common.poco_exists(game_name):
                    self.common.poco_click(game_name)
                    break
                
                if num == 11:
                    raise EOFError(f'找不到{game_name["type_name"]}彩種入口')

class LotteryPageA(BaseLotteryPage):
    # 五分快3
    def game_play_wfk3(self):
        self.enter_lottery(LotteryPageLocator.a_wfk3)

    # 極速快3
    def game_play_jisuk3(self):
        self.enter_lottery(LotteryPageLocator.a_jisuk3)

    # 五分幸運28
    def game_play_wfxy28(self):
        self.enter_lottery(LotteryPageLocator.a_wfxy28)

    # 五分PK十
    def game_play_wfpk10(self):
        self.enter_lottery(LotteryPageLocator.a_wfpk10)

    # 五分時時彩
    def game_play_wfssc(self):
        self.enter_lottery(LotteryPageLocator.a_wfssc)

    # 極速PK拾
    def game_play_jspk10(self):
        self.enter_lottery(LotteryPageLocator.a_jspk10)

    # 極速時時彩
    def game_play_jsssc(self):
        self.enter_lottery(LotteryPageLocator.a_jsssc)

    # 極速六合彩
    def game_play_js6(self):
        self.enter_lottery(LotteryPageLocator.a_js6)

    # 安徽快三
    def game_play_ahk3(self):
        self.enter_lottery(LotteryPageLocator.a_ahk3)

    # 香港六合彩
    def game_play_hk(self):
        self.enter_lottery(LotteryPageLocator.a_hk)

    # 新疆時時彩
    def game_play_xjssc(self):
        self.enter_lottery(LotteryPageLocator.a_xjssc)

    # 重慶時時彩
    def game_play_cqssc(self):
        self.enter_lottery(LotteryPageLocator.a_cqssc)

    # 北京PL拾
    def game_play_bjpk10(self):
        self.enter_lottery(LotteryPageLocator.a_bjpk10)

    # PC蛋蛋
    def game_play_bjxy28(self):
        self.enter_lottery(LotteryPageLocator.a_bjxy28)

    # 新加玻幸運28
    def game_play_xjpxy28(self):
        self.enter_lottery(LotteryPageLocator.a_xjpxy28)

    # 台灣幸運28
    def game_play_twxy28(self):
        self.enter_lottery(LotteryPageLocator.a_twxy28)

    # 幸運飛艇
    def game_play_malxyft(self):
        self.enter_lottery(LotteryPageLocator.a_malxyft)

    # 廣東11選5
    def game_play_gd11x5(self):
        self.enter_lottery(LotteryPageLocator.a_gd11x5)

    # 加拿大幸運28
    def game_play_jndbxy28(self):
        self.enter_lottery(LotteryPageLocator.a_jndbsxy28)

    # 極速11選5
    def game_play_jisu11x5(self):
        self.enter_lottery(LotteryPageLocator.a_jisu11x5)

    # 三分11選5
    def game_play_sf11x5(self):
        self.enter_lottery(LotteryPageLocator.a_sf11x5)

    # 五分11選5
    def game_play_wf11x5(self):
        self.enter_lottery(LotteryPageLocator.a_wf11x5)

    # 湖北快三
    def game_play_hbk3(self):
        self.enter_lottery(LotteryPageLocator.a_hbk3)

    # 福彩3D
    def game_play_fc3d(self):
        self.enter_lottery(LotteryPageLocator.a_fc3d)

    # 上海時時樂
    def game_play_shssc(self):
        self.enter_lottery(LotteryPageLocator.a_shssc)

    # 排列三
    def game_play_pl3(self):
        self.enter_lottery(LotteryPageLocator.a_pl3)

    # 江蘇快3
    def game_play_jsk3(self):
        self.enter_lottery(LotteryPageLocator.a_jsk3)

    # 上海快3
    def game_play_shk3(self):
        self.enter_lottery(LotteryPageLocator.a_shk3)

    # 河北快3
    def game_play_hebk3(self):
        self.enter_lottery(LotteryPageLocator.a_hebk3)

    # 廣西快3
    def game_play_gxk3(self):
        self.enter_lottery(LotteryPageLocator.a_gxk3)

class LotteryPageB(BaseLotteryPage):
    # 五分快3
    def game_play_wfk3(self):
        self.enter_lottery(LotteryPageLocator.b_wfk3)

    # 極速快3
    def game_play_jisuk3(self):
        self.enter_lottery(LotteryPageLocator.b_jisuk3)

    # 五分幸運28
    def game_play_wfxy28(self):
        self.enter_lottery(LotteryPageLocator.b_wfxy28)

    # 五分PK十
    def game_play_wfpk10(self):
        self.enter_lottery(LotteryPageLocator.b_wfpk10)

    # 五分時時彩
    def game_play_wfssc(self):
        self.enter_lottery(LotteryPageLocator.b_wfssc)

    # 極速PK拾
    def game_play_jspk10(self):
        self.enter_lottery(LotteryPageLocator.b_jspk10)

    # 極速時時彩
    def game_play_jsssc(self):
        self.enter_lottery(LotteryPageLocator.b_jsssc)

    # 極速六合彩
    def game_play_js6(self):
        self.enter_lottery(LotteryPageLocator.b_js6)

    # 安徽快三
    def game_play_ahk3(self):
        self.enter_lottery(LotteryPageLocator.b_ahk3)

    # 香港六合彩
    def game_play_hk(self):
        self.enter_lottery(LotteryPageLocator.b_hk)

    # 新疆時時彩
    def game_play_xjssc(self):
        self.enter_lottery(LotteryPageLocator.b_xjssc)

    # 重慶時時彩
    def game_play_cqssc(self):
        self.enter_lottery(LotteryPageLocator.b_cqssc)

    # 北京PL拾
    def game_play_bjpk10(self):
        self.enter_lottery(LotteryPageLocator.b_bjpk10)

    # PC蛋蛋
    def game_play_bjxy28(self):
        self.enter_lottery(LotteryPageLocator.b_bjxy28)

    # 新加玻幸運28
    def game_play_xjpxy28(self):
        self.enter_lottery(LotteryPageLocator.b_xjpxy28)

    # 台灣幸運28
    def game_play_twxy28(self):
        self.enter_lottery(LotteryPageLocator.b_twxy28)

    # 幸運飛艇
    def game_play_malxyft(self):
        self.enter_lottery(LotteryPageLocator.b_malxyft)

    # 廣東11選5
    def game_play_gd11x5(self):
        self.enter_lottery(LotteryPageLocator.b_gd11x5)

    # 加拿大幸運28
    def game_play_jndbxy28(self):
        self.enter_lottery(LotteryPageLocator.b_jndbsxy28)

    # 極速11選5
    def game_play_jisu11x5(self):
        self.enter_lottery(LotteryPageLocator.b_jisu11x5)

    # 三分11選5
    def game_play_sf11x5(self):
        self.enter_lottery(LotteryPageLocator.b_sf11x5)

    # 五分11選5
    def game_play_wf11x5(self):
        self.enter_lottery(LotteryPageLocator.b_wf11x5)

    # 湖北快三
    def game_play_hbk3(self):
        self.enter_lottery(LotteryPageLocator.b_hbk3)

    # 福彩3D
    def game_play_fc3d(self):
        self.enter_lottery(LotteryPageLocator.b_fc3d)

    # 上海時時樂
    def game_play_shssc(self):
        self.enter_lottery(LotteryPageLocator.b_shssc)

    # 排列三
    def game_play_pl3(self):
        self.enter_lottery(LotteryPageLocator.b_pl3)

    # 江蘇快3
    def game_play_jsk3(self):
        self.enter_lottery(LotteryPageLocator.b_jsk3)

    # 上海快3
    def game_play_shk3(self):
        self.enter_lottery(LotteryPageLocator.b_shk3)

    # 河北快3
    def game_play_hebk3(self):
        self.enter_lottery(LotteryPageLocator.b_hebk3)

    # 廣西快3
    def game_play_gxk3(self):
        self.enter_lottery(LotteryPageLocator.b_gxk3)

class LotteryPage(BaseLotteryPage):
    # 六合彩入口
    def enter_lottery_mark6(self):
        self.enter_lottery(LotteryPageLocator.mark6)
    # PK拾入口
    def enter_lottery_pk10(self):
        self.enter_lottery(LotteryPageLocator.pk10)
    # 11選5入口
    def enter_lottery_11x5(self):
        self.enter_lottery(LotteryPageLocator.eleven_x5)
    # 快3入口
    def enter_lottery_k3(self):
        self.enter_lottery(LotteryPageLocator.k3)
    # 時時彩入口
    def enter_lottery_ssc(self):
        self.enter_lottery(LotteryPageLocator.ssc)
    # 幸運28入口
    def enter_lottery_xy28(self):
        self.enter_lottery(LotteryPageLocator.xy28)
    # 一般彩票入口
    def enter_lottery_general(self):
        self.enter_lottery(LotteryPageLocator.general_lottery)

    def enter_hk(self):
        self.enter_lottery_mark6()
        if self.common.poco_wait_exists(LotteryPageLocator.hk):
            self.common.poco_click(LotteryPageLocator.hk)
        else:
            raise EOFError(f'找不到香港六合彩入口')
    
    def enter_wfssc(self):
        self.enter_lottery_ssc()
        if self.common.poco_wait_exists(LotteryPageLocator.wfssc):
            self.common.poco_click(LotteryPageLocator.wfssc)
        else:
            raise EOFError(f'找不到五分時時彩入口')
    
    def enter_wfpk10(self):
        self.enter_lottery_pk10()
        if self.common.poco_wait_exists(LotteryPageLocator.wfpk10):
            self.common.poco_click(LotteryPageLocator.wfpk10)
        else:
            raise EOFError(f'找不到五分PK拾入口')

    def enter_twxy28(self):
        self.enter_lottery_xy28()
        if self.common.poco_wait_exists(LotteryPageLocator.twxy28):
            self.common.poco_click(LotteryPageLocator.twxy28)
        else:
            raise EOFError(f'找不到台灣幸運28入口')

    def enter_wf11x5(self):
        self.enter_lottery_11x5()
        if self.common.poco_wait_exists(LotteryPageLocator.wf11x5):
            self.common.poco_click(LotteryPageLocator.wf11x5)
        else:
            raise EOFError(f'找不到五分11選5入口')

    def enter_wfk3(self):
        self.enter_lottery_k3()
        if self.common.poco_wait_exists(LotteryPageLocator.wfk3):
            self.common.poco_click(LotteryPageLocator.wfk3)
        else:
            raise EOFError(f'找不到五分快3入口')

    def enter_fc3d(self):
        self.enter_lottery_general()
        if self.common.poco_wait_exists(LotteryPageLocator.fc3d):
            self.common.poco_click(LotteryPageLocator.fc3d)
        else:
            raise EOFError(f'找不到福彩3D入口')
    
    # 關閉登入公告
    def skip_announcement_napp(self):
        if self.common.poco_exists(LotteryPageLocator.close_announcement):
            self.common.poco_click(LotteryPageLocator.close_announcement)

    # 關閉更新密碼提醒
    def skip_change_password(self):
        if self.common.poco_exists(LotteryPageLocator.skip_change_password):
            self.common.poco_click(LotteryPageLocator.skip_change_password)
    
    # 關閉站內信彈窗
    def skip_mail_popup(self):
        if self.common.poco_exists(LotteryPageLocator.close_mail):
            self.common.poco_click(LotteryPageLocator.close_mail)

    # 確認彩票注單
    def bet_lottery_record(self, lottery_name):
        self.go_back()      # 回到首頁
        self.common.sleep(1)
        self.skip_announcement_napp()
        self.skip_change_password()
        self.skip_mail_popup()
        if self.common.poco_wait_exists(LotteryPageLocator.member):
            self.common.poco_click(LotteryPageLocator.member)
        else:
            raise EOFError('點擊會員頁面錯誤')
        
        if self.common.poco_exists(LotteryPageLocator.bet_record):
            self.common.poco_click(LotteryPageLocator.bet_record)
        
        self.wait_loading_finish()
        assert self.common.poco_exists(LotteryPageLocator.bet_record_lottery(lottery_name)), f'找不到{lottery_name}注單'

