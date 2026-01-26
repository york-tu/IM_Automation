# start_wda_clean.ps1

param (
    [string]$UDID = "00008130-000C45500292001C",
    [string]$BUNDLEID = "com.FYC.facebook.WebDriverAgentRunner.xctrunner",
    [string]$TESTRUNNERBUNDLEID = "com.FYC.facebook.WebDriverAgentRunner.xctrunner",
    [string]$XCTESTCONFIG = "WebDriverAgentRunner.xctest"
)

Write-Host "Stopping existing ios.exe processes..."
Get-Process ios -ErrorAction SilentlyContinue | Stop-Process -Force

Write-Host "Removing old tunnel adapter (tun0) if exists..."
$adapter = Get-NetAdapter -Name "tun0" -ErrorAction SilentlyContinue
if ($adapter) {
    Remove-NetAdapter -Name "tun0" -Confirm:$false
    Write-Host "tun0 removed."
} else {
    Write-Host "No tun0 adapter found."
}

Write-Host "Starting userspace tunnel..."
Start-Process -FilePath ".\ios.exe" -ArgumentList "tunnel start --udid=$UDID --userspace" -WindowStyle Hidden

Write-Host "Waiting 5 seconds for tunnel to initialize..."
Start-Sleep -Seconds 5

Write-Host "Starting WebDriverAgent..."
Start-Process -FilePath ".\ios.exe" -ArgumentList "runwda --udid=$UDID --bundleid=$BUNDLEID --testrunnerbundleid=$TESTRUNNERBUNDLEID --xctestconfig=$XCTESTCONFIG"
