from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl


class DepositRecordPageLocator:
    base = Xpath_Base()

    all = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='全部'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    not_yet = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='待确认'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    success = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='成功'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    cancel = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='取消'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    not_yet_info = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='待确认', num=1),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    success_info = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='成功', num=1),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    cancel_info = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='取消', num=1),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 關閉
    close = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.view.ViewGroup', num=-1),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    back = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='back'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 收支詳細資訊
    title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='充值纪录详情资讯'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    text_deposit = base.check_device(
        Android=base.data_collation(type_kind='nameMatches', type_name='充值.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    no_info = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='empty_data'),
        iOS=base.data_collation(type_kind='', type_name='')
    )


class DepositRecordPage(Base):
    error_list = []

    def deposit_sort(self):
        tab_list = (
            (DepositRecordPageLocator.all, self.open_info, ''),
            (DepositRecordPageLocator.not_yet, self.not_yet_info, ''),
            (DepositRecordPageLocator.success, self.success_info, ''),
            (DepositRecordPageLocator.cancel, self.cancel_info, 'skip_check'),

        )

        self.common.sleep(1)
        for i in tab_list:
            if self.common.poco_exists(i[0]):
                self.common.poco_click(i[0])

                if (i[2] != "skip_check") and (self.common.poco_exists(DepositRecordPageLocator.text_deposit)):
                    i[1]()
                else:
                    if self.common.poco_exists(DepositRecordPageLocator.no_info) == False:
                        self.error_list.append(f"充值记录此分類未顯示尚無資料:{i[0]['type_name']}")

            else:
                self.error_list.append(f"充值记录找不到上方分類:{i[0]['type_name']}")

        if self.error_list != []:
            raise EOFError(f'{self.error_list}')

    def open_info(self):
        self.common.poco_click(DepositRecordPageLocator.text_deposit)

        if self.common.poco_exists(DepositRecordPageLocator.title):
            self.common.poco_click(DepositRecordPageLocator.back)
        else:
            self.error_list.append('全部: "充值纪录详情资讯"頁錯誤')

    def not_yet_info(self):
        self.common.poco_click(DepositRecordPageLocator.not_yet_info)

        if self.common.poco_exists(DepositRecordPageLocator.title):
            self.common.poco_click(DepositRecordPageLocator.back)
        else:
            self.error_list.append('待確認: "充值纪录详情资讯"頁錯誤')

    def success_info(self):
        self.common.poco_click(DepositRecordPageLocator.success_info)

        if self.common.poco_exists(DepositRecordPageLocator.title):
            self.common.poco_click(DepositRecordPageLocator.back)
        else:
            self.error_list.append('成功: "充值纪录详情资讯"頁錯誤')

    def cancel_info(self):
        # if not self.common.poco_exists(DepositRecordPageLocator.no_info):
        self.common.poco_click(DepositRecordPageLocator.cancel_info)

        if self.common.poco_exists(DepositRecordPageLocator.title):
            self.common.poco_click(DepositRecordPageLocator.back)
        else:
            self.error_list.append('取消: "充值纪录详情资讯"頁錯誤')
        # else:
        #     assert self.common.poco_get_text(DepositRecordPageLocator.no_info) == '尚无资料', f'取消頁資料錯誤'
