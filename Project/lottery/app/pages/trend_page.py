from common.app.common import Common
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl
   
class TrendPageLocator :
    base = Xpath_Base()

    trend_image = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='走势图.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='走势图.*')
    )

    def trend_back():
        if gl.get_value('OS_VERSION') == '11':
            action='parent().parent().child().child().child()'
            type_name='走势图.*'
            type_kind='textMatches'
        else:
            action='parent().child()'
            type_name='开奖走势'
            type_kind='text'
        trend_back = TrendPageLocator.base.check_device(
            Android = TrendPageLocator.base.data_collation(type_kind=type_kind, type_name=type_name, action=action),
            iOS = TrendPageLocator.base.data_collation(type_kind='name', type_name='开奖走势.*', action='child()')
        )
        return trend_back

    @staticmethod
    def lottery_kind(lottery_chinese):
        lottery_kind = TrendPageLocator.base.check_device(
            Android = TrendPageLocator.base.data_collation(type_kind='text', type_name=lottery_chinese),
            iOS = TrendPageLocator.base.data_collation(type_kind='text', type_name=lottery_chinese)
        )
        return lottery_kind

    @staticmethod
    def lottery_name(num=''):
        if num == 1:
            action = 'parent().child()[3]'
        else:
            action = 'parent().child()[2]'
        lottery_name = TrendPageLocator.base.check_device(
            Android = TrendPageLocator.base.data_collation(type_kind='textMatches', type_name='走势图.*', action = action),
            iOS = TrendPageLocator.base.data_collation(type_kind='textMatches', type_name='走势图.*', action = action)
        )
        return lottery_name

    @staticmethod
    def lottery_transfer_chinese(lottery_kind):
        mapping_dict = {
            'hk': '香港六合彩',
            'wfk3': '五分快3',
            'jisuk3': '极速快3',
            'wfxy28': '五分幸运28',
            'wfpk10': '五分PK拾',
            'wfssc': '五分时时彩',
            'jspk10': '极速PK拾',
            'jsssc': '极速时时彩',
            'js6': '极速六合彩',
            'ahk3': '安徽快三',
            'xjssc': '新疆时时彩',
            'cqssc': '重庆时时彩',
            'bjpk10': '北京PK拾',
            'bjxy28': 'PC蛋蛋',
            'xjpxy28': '新加坡幸运28',
            'twxy28': '台湾幸运28',
            'malxyft': '幸运飛艇',
            'gd11x5': '广东11选5',
            'jndbsxy28': '加拿大幸运28',
            'jisu11x5': '极速11选5',
            'sf11x5': '三分11选5',
            'wf11x5': '五分11选5',
            'gxk3': '广西快3',
            'hebk3': '河北快3',
            'shk3': '上海快3',
            'jsk3': '江苏快3',
            'pl3': '排列三',
            'shssc': '上海時時樂',
            'fc3d': '福彩3D',
            'hbk3': '湖北快三'
        }
        
        return mapping_dict[lottery_kind]

class TrendPage(Base):
    def trend(self, lottery_kind):
        self.common.sleep(2)
        
        if not self.common.poco_exists(TrendPageLocator.trend_image):
            raise EOFError('走勢圖不存在')

        lottery_chinese = TrendPageLocator.lottery_transfer_chinese(lottery_kind)
        if self.common.poco_exists(TrendPageLocator.lottery_kind(lottery_chinese)) == True:
            lottery_get_name = self.common.poco_get_text(TrendPageLocator.lottery_kind(lottery_chinese))
        else:
            lottery_get_name = self.common.poco_get_text(TrendPageLocator.lottery_name())

        if lottery_chinese != lottery_get_name:
            lottery_get_name = self.common.poco_get_text(TrendPageLocator.lottery_name(1))
            assert lottery_chinese == lottery_get_name, '對應錯誤的走勢圖'
            
        self.common.poco_click(TrendPageLocator.trend_back())