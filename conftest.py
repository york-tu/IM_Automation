# -*- coding: utf-8 -*-
"""
Pytest 配置檔案
用於過濾測試輸出中的無用訊息
"""
import pytest
import sys
import re


def pytest_configure(config):
    """Pytest 配置鉤子"""
    # 註冊自定義標記
    config.addinivalue_line("markers", "app: 標記為 App 測試")
    config.addinivalue_line("markers", "web: 標記為 Web 測試")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """測試設置鉤子"""
    pass


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item):
    """測試清理鉤子"""
    pass


def _filter_pocoservice_output(text):
    """
    過濾掉 pocoservice.apk 相關的輸出
    
    Args:
        text: 要過濾的文字
        
    Returns:
        str: 過濾後的文字
    """
    if not text:
        return text
    
    lines = text.split('\n')
    filtered_lines = []
    
    for line in lines:
        # 過濾 [pocoservice.apk] 相關的輸出
        if '[pocoservice.apk]' in line:
            continue
        
        # 過濾包含 INSTRUMENTATION_RESULT 且與 pocoservice 相關的輸出
        if 'INSTRUMENTATION_RESULT' in line and 'pocoservice' in line:
            continue
        
        # 過濾包含 'Process crashed' 且與 pocoservice 相關的輸出
        if 'Process crashed' in line and 'pocoservice' in line:
            continue
        
        filtered_lines.append(line)
    
    return '\n'.join(filtered_lines)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """攔截測試報告生成，過濾 stdout 中的無用訊息"""
    outcome = yield
    report = outcome.get_result()
    
    # 只在測試失敗或錯誤時過濾 stdout
    if report.when == "call" and (report.failed or report.skipped):
        if hasattr(report, 'capstdout') and report.capstdout:
            report.capstdout = _filter_pocoservice_output(report.capstdout)
        
        if hasattr(report, 'capstderr') and report.capstderr:
            report.capstderr = _filter_pocoservice_output(report.capstderr)
    
    # 對於 setup 和 teardown 階段也進行過濾
    if report.when in ("setup", "teardown") and report.failed:
        if hasattr(report, 'capstdout') and report.capstdout:
            report.capstdout = _filter_pocoservice_output(report.capstdout)
        
        if hasattr(report, 'capstderr') and report.capstderr:
            report.capstderr = _filter_pocoservice_output(report.capstderr)

