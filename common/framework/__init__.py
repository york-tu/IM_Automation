# -*- coding: utf-8 -*-
"""
Framework Layer
框架抽象層，提供統一的基礎類和工廠模式
"""

from common.framework.base_driver import BaseDriver
from common.framework.base_page import BasePage
from common.framework.base_testcase import BaseTestCase
from common.framework.page_factory import PageFactory, PageFactoryBuilder
from common.framework.page_registry import (
    get_page_config,
    register_pages_to_factory,
    PAGE_CONFIGS
)

__all__ = [
    'BaseDriver',
    'BasePage',
    'BaseTestCase',
    'PageFactory',
    'PageFactoryBuilder',
    'get_page_config',
    'register_pages_to_factory',
    'PAGE_CONFIGS',
]

