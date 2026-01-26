# -------------------------------
# start_wda_full.ps1
# 自動啟動 userspace tunnel + WDA，穩定 iOS 17+
# -------------------------------

param(
    [string]$UDID = "00008130-000C45500292001C",
    [string]$BUNDLEID = "com.FYC.facebook.WebDriverAgentRunner.xctrunner",
    [string]$TESTRUNNERID = "com.FYC.facebook.WebDriverAgentRunner.xctrunner",
    [string]$XCTESTCONFIG = "WebDriverAgentRunner.xctest",
    [int]$TUNNEL_PORT = 60105
)

# -------------------------------
# 1️⃣ 終止舊的 ios.exe 進程
Write-Host "🔹 Terminating existing ios.exe processes..."
Get-Process ios -ErrorAction SilentlyContinue | Stop-Process -Force

# -------------------------------
# 2️⃣ 設定環境變數
Write-Host "🔹 Setting environment variables..."
$env:IOS_DEVICE_TUNNEL_FORCE_IPV4 = "1"
$env:ENABLE_GO_IOS_AGENT = "user"

# -------------------------------
# 3️⃣ 啟動 userspace tunnel (前台)
Write-Host "🔹 Starting userspace tunnel..."
Start-Process -FilePath ".\ios.exe" -ArgumentList "tunnel start --udid=$UDID --userspace" -WindowStyle Normal -PassThru | Out-Null

# 等待 tunnel 啟動完成
Write-Host "⏳ Waiting 5秒 for tunnel to initialize..."
Start-Sleep -Seconds 5

# -------------------------------
# 4️⃣ 啟動 WDA
Write-Host "🔹 Starting WebDriverAgent..."
Start-Process -NoNewWindow -Wait -FilePath ".\ios.exe" -ArgumentList "runwda --udid=$UDID --bundleid=$BUNDLEID --testrunnerbundleid=$TESTRUNNERID --xctestconfig=$XCTESTCONFIG"

Write-Host "✅ WDA launch attempt finished. Check above logs for success."
