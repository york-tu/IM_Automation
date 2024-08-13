from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl

class FeedbackPageLocator:
    base = Xpath_Base()

    member_page = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='额度转换'),
        iOS = base.data_collation(type_kind='name', type_name='额度转换')
    )

    member_page_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='会员'),
        iOS = base.data_collation(type_kind='name', type_name='会员')
    )

    confirm_btn = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='确认.*'),
        iOS = base.data_collation(type_kind='name', type_name='确认')
    )

    success = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='提交成功.*'),
        iOS = base.data_collation(type_kind='name', type_name='提交成功')
    )

    send_btn = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='提交反馈.*'),
        iOS = base.data_collation(type_kind='name', type_name='提交反馈')
    )

    message = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='尊敬的会员.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='尊敬的会员.*')
    )

    types = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='请选择类型.*'),
        iOS = base.data_collation(type_kind='name', type_name='ios_touchable_wrapper')
    )

    types_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请选择'),
        iOS = base.data_collation(type_kind='name', type_name='请选择')
    )

    problem = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='出入款项问题.*'),
        iOS = base.data_collation(pos=(0.5, 0.9, 0.5, 0.8))
    )

    title = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='请输入标题.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='请输入标题.*')
    )

    title_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请简述问题'),
        iOS = base.data_collation(type_kind='name', type_name='请简述问题')
    )

    description = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='请输入内容.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='请输入内容.*')
    )

    description_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*etContentEnterText'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*etContentEnterText')
    )

    push = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='上传图片'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='上传图片.*', action='child()')
    )

    upload_photo = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*ivUploadFeedbackPhoto'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*ivUploadFeedbackPhoto.*')
    )

    agree = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*:id\/permission_allow_button'),
        iOS = base.data_collation(type_kind='name', type_name='ScrollView', action='child().child().child()')
    )

    enter = base.check_device(
        Android = base.data_collation(type_kind='', type_name=''),
        iOS = base.data_collation(type_kind='name', type_name='done_button')
    )

    cancel = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='拒絕'),
        iOS = base.data_collation(type_kind='name', type_name='取消')
    )

    camera = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='使用相机'),
        iOS = base.data_collation(type_kind='name', type_name='使用相机')
    )

    camera_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='拍照'),
        iOS = base.data_collation(type_kind='name', type_name='拍照')
    )

    allow_camera = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*permission_allow.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*permission_allow.*')
    )

    shutter_button = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*shutter_button.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*shutter_button.*')
    )

    camera_shutter = base.check_device(
        Android = base.data_collation(type_kind='desc', type_name='拍照'),
        iOS = base.data_collation(type_kind='desc', type_name='拍照')
    )

    done_button = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*done_button'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*done_button')
    )

    okay_button = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*okay'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*okay')
    )



class FeedbackPage(Base):
    def report(self):
        self.common.poco_wait_exists(FeedbackPageLocator.types)
        self.common.poco_click(FeedbackPageLocator.types)

        if gl.get_value('PHONE_PLATFORM') == 'Android':
            self.common.poco_click(FeedbackPageLocator.problem)
        else:
            self.common.swipe(FeedbackPageLocator.problem)
            self.common.sleep(3)
            self.common.poco_click(FeedbackPageLocator.enter)

        self.common.poco_send_text(FeedbackPageLocator.title, '機器人')
        self.common.poco_send_text(FeedbackPageLocator.description, '我就是世界無敵霹靂超級天下第一無人能敵機器人')
        self.common.sleep(2)
        self.common.poco_click(FeedbackPageLocator.message)
        self.common.go_bottom()

        if self.common.poco_exists(FeedbackPageLocator.push):
            self.common.poco_click(FeedbackPageLocator.push)
            self.common.poco_click(FeedbackPageLocator.camera)
            
            # 裝置允許使用相機權限，按到完
            self.common.sleep(2)
            while self.common.poco_exists(FeedbackPageLocator.agree):
                self.common.poco_click(FeedbackPageLocator.agree)
            
            if gl.get_value('PHONE_PLATFORM') == 'Android':
                self.common.keyevent("BACK") # 安卓的相機介面沒有取消鈕可以按
            elif self.common.poco_exists(FeedbackPageLocator.cancel):
                self.common.poco_click(FeedbackPageLocator.cancel)
            
            # 確認已經退出相機
            self.common.sleep(2)
            if not self.common.poco_exists(FeedbackPageLocator.send_btn):
                raise EOFError('進入/退出 相機畫面錯誤')

        self.common.poco_click(FeedbackPageLocator.send_btn)

        if self.common.poco_exists(FeedbackPageLocator.success):
            self.common.poco_click(FeedbackPageLocator.confirm_btn)
            

            assert self.common.poco_exists(FeedbackPageLocator.member_page), '倒轉回會員中心失敗'
        else:
            raise EOFError('意見反饋錯誤')
    
    # 提交意見反饋
    def feedback(self):
        self.common.poco_wait_exists(FeedbackPageLocator.types_napp)
        self.common.poco_click(FeedbackPageLocator.types_napp)

        self.common.poco_click(FeedbackPageLocator.problem)

        self.common.poco_send_text(FeedbackPageLocator.title_napp, '機器人')
        self.common.poco_send_text(FeedbackPageLocator.description_napp, '我就是世界無敵霹靂超級天下第一無人能敵機器人')

        if self.common.poco_exists(FeedbackPageLocator.upload_photo):
            self.common.poco_click(FeedbackPageLocator.upload_photo)
            # 裝置允許使用相機權限，按到完
            self.common.sleep(1)
            while self.common.poco_exists(FeedbackPageLocator.allow_camera):
                self.common.poco_click(FeedbackPageLocator.allow_camera)
            self.common.poco_wait_exists(FeedbackPageLocator.camera_napp)
            self.common.poco_click(FeedbackPageLocator.camera_napp)
            
            if self.common.poco_wait_exists(FeedbackPageLocator.shutter_button):
                self.common.poco_click(FeedbackPageLocator.shutter_button)
            if self.common.poco_exists(FeedbackPageLocator.camera_shutter):
                self.common.poco_click(FeedbackPageLocator.camera_shutter)

            if self.common.poco_wait_exists(FeedbackPageLocator.done_button):
                self.common.poco_click(FeedbackPageLocator.done_button)
            if self.common.poco_exists(FeedbackPageLocator.okay_button):
                self.common.poco_click(FeedbackPageLocator.okay_button)

            # 確認已經退出相機
            self.common.sleep(1)
            if not self.common.poco_exists(FeedbackPageLocator.upload_photo):
                raise EOFError('進入/退出 相機畫面錯誤')
        
        self.common.go_bottom()
        if self.common.poco_exists(FeedbackPageLocator.send_btn):
            self.common.poco_click(FeedbackPageLocator.send_btn)

        if self.common.poco_wait_exists(FeedbackPageLocator.success, timeout=20):
            self.common.poco_click(FeedbackPageLocator.confirm_btn)
            
            assert self.common.poco_exists(FeedbackPageLocator.member_page_napp), '倒轉回會員中心失敗'
        else:
            raise EOFError('意見反饋提交失敗')