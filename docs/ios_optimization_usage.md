# iOS 自動化測試優化使用指南

## 1. 超時時間優化

### 自動優化
所有等待方法已自動針對 iOS 優化，默認超時時間從 10 秒減少到 5 秒：

```python
# 自動優化：iOS 使用 5 秒，Android 使用 10 秒
self.common.poco_wait_exists(locator)  # iOS: 5秒, Android: 10秒
self.common.poco_wait_appearance(locator)  # iOS: 5秒, Android: 10秒
self.common.poco_wait_disappearance(locator)  # iOS: 5秒, Android: 10秒
self.common.wait_image(image_path)  # iOS: 5秒, Android: 10秒
```

### 手動指定超時時間
如果需要自定義超時時間，可以明確指定：

```python
# 明確指定超時時間（不會自動優化）
self.common.poco_wait_exists(locator, timeout=3)  # iOS 和 Android 都使用 3 秒
self.common.poco_wait_exists(locator, timeout=8)  # iOS 和 Android 都使用 8 秒
```

## 2. 批量操作優化

### 2.1 批量檢查元素是否存在

**使用場景：** 需要同時檢查多個元素是否存在

**優化效果：** iOS 只請求一次 UI 樹，而不是多次請求

```python
# 批量檢查多個元素
locators = [
    MainPageLocator.main_btn,
    MainPageLocator.share_profile_btn,
    MainPageLocator.edit_profile_btn
]

# 一次性檢查所有元素（iOS 只請求一次 UI 樹）
results = self.common.poco_batch_exists(locators)

# 結果是字典格式：{locator: exists_result}
if results[MainPageLocator.main_btn]:
    print("主頁按鈕存在")
if results[MainPageLocator.share_profile_btn]:
    print("分享按鈕存在")
```

### 2.2 批量等待元素出現

**使用場景：** 需要等待多個元素中的任意一個或全部出現

**優化效果：** 減少 HTTP 請求次數，提高效率

```python
# 等待任意一個元素出現（任一存在即返回）
locators = [
    ChatRoomPageLocator.message_input,
    ChatRoomPageLocator.send_message_btn
]

results = self.common.poco_batch_wait_exists(
    locators, 
    timeout=5, 
    all_required=False  # 任一存在即返回
)

# 檢查結果
if results[ChatRoomPageLocator.message_input]:
    print("訊息輸入框已出現")
```

```python
# 等待所有元素都出現（全部存在才返回）
locators = [
    MainPageLocator.main_btn,
    MainPageLocator.share_profile_btn,
    MainPageLocator.edit_profile_btn
]

results = self.common.poco_batch_wait_exists(
    locators, 
    timeout=5, 
    all_required=True  # 全部存在才返回
)

# 檢查是否所有元素都存在
if all(results.values()):
    print("所有元素都已出現")
```

### 2.3 批量獲取元素屬性

**使用場景：** 需要獲取多個元素的文字或屬性

**優化效果：** iOS 只請求一次 UI 樹，一次性獲取所有屬性

```python
# 批量獲取多個元素的文字
locators = [
    MainPageLocator.main_nickname,
    MainPageLocator.main_description
]

# 一次性獲取所有元素的文字（iOS 只請求一次 UI 樹）
texts = self.common.poco_get_multiple(locators, attribute='text')

# 結果是字典格式：{locator: text_value}
nickname = texts[MainPageLocator.main_nickname]
description = texts[MainPageLocator.main_description]

print(f"暱稱: {nickname}")
print(f"簡介: {description}")
```

```python
# 批量獲取其他屬性
locators = [
    ChatRoomPageLocator.message_input,
    ChatRoomPageLocator.send_message_btn
]

# 獲取 'enabled' 屬性
attributes = self.common.poco_get_multiple(locators, attribute='enabled')

if attributes[ChatRoomPageLocator.send_message_btn] == '1':
    print("發送按鈕已啟用")
```

## 3. 實際應用範例

### 範例 1：登入後檢查主頁元素

**優化前（多次請求）：**
```python
# 每次檢查都需要請求 UI 樹（iOS 慢）
if self.common.poco_wait_exists(MainPageLocator.main_btn):
    self.common.poco_click(MainPageLocator.main_btn)
if self.common.poco_wait_exists(MainPageLocator.share_profile_btn):
    print("分享按鈕存在")
if self.common.poco_wait_exists(MainPageLocator.edit_profile_btn):
    print("編輯按鈕存在")
```

**優化後（一次請求）：**
```python
# 一次性檢查所有元素（iOS 只請求一次）
locators = [
    MainPageLocator.main_btn,
    MainPageLocator.share_profile_btn,
    MainPageLocator.edit_profile_btn
]

results = self.common.poco_batch_wait_exists(locators, timeout=5, all_required=True)

if results[MainPageLocator.main_btn]:
    self.common.poco_click(MainPageLocator.main_btn)
if results[MainPageLocator.share_profile_btn]:
    print("分享按鈕存在")
if results[MainPageLocator.edit_profile_btn]:
    print("編輯按鈕存在")
```

### 範例 2：檢查聊天室是否載入完成

**優化前：**
```python
# 分別檢查每個元素（多次請求）
self.common.poco_wait_exists(ChatRoomPageLocator.message_input, timeout=10)
self.common.poco_wait_exists(ChatRoomPageLocator.send_message_btn, timeout=10)
```

**優化後：**
```python
# 一次性等待所有元素出現（減少請求次數）
locators = [
    ChatRoomPageLocator.message_input,
    ChatRoomPageLocator.send_message_btn
]

results = self.common.poco_batch_wait_exists(locators, timeout=5, all_required=True)
assert all(results.values()), "聊天室未完全載入"
```

### 範例 3：獲取用戶資料

**優化前：**
```python
# 分別獲取每個屬性（多次請求）
nickname = self.common.poco_get_text(MainPageLocator.main_nickname)
description = self.common.poco_get_text(MainPageLocator.main_description)
user_id = self.common.poco_get_attr(MainPageLocator.user_id, 'value')
```

**優化後：**
```python
# 一次性獲取所有屬性（只請求一次）
locators = [
    MainPageLocator.main_nickname,
    MainPageLocator.main_description,
    MainPageLocator.user_id
]

# 獲取文字屬性
texts = self.common.poco_get_multiple(locators, attribute='text')
nickname = texts[MainPageLocator.main_nickname]
description = texts[MainPageLocator.main_description]

# 獲取其他屬性
values = self.common.poco_get_multiple([MainPageLocator.user_id], attribute='value')
user_id = values[MainPageLocator.user_id]
```

## 4. 性能提升估算

### 超時時間優化
- **單次等待操作：** 節省約 5 秒（10秒 → 5秒）
- **測試案例中多次等待：** 可節省 20-50 秒

### 批量操作優化
假設需要檢查 5 個元素：

**優化前：**
- 5 次 HTTP 請求
- 每次約 100-200ms
- 總計：500-1000ms

**優化後：**
- 1 次 HTTP 請求
- 約 100-200ms
- 總計：100-200ms

**性能提升：** 約 **4-5 倍**

## 5. 注意事項

1. **批量操作適用場景：**
   - 需要同時檢查/獲取多個元素時
   - 元素在同一頁面時
   - 元素定位器已確定時

2. **不適用場景：**
   - 元素在不同頁面時
   - 需要動態等待元素出現時（使用 `poco_wait_exists` 更合適）

3. **超時時間調整：**
   - 如果元素載入較慢，可以明確指定更長的超時時間
   - 例如：`poco_wait_exists(locator, timeout=8)`

4. **向後兼容：**
   - 所有優化都向後兼容
   - 現有代碼無需修改即可享受超時時間優化
   - 批量操作是可選的，可以逐步遷移


