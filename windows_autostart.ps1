
$exePath = Join-Path -Path (Get-Location) -ChildPath "Battery.exe"
$startupFolder = [Environment]::GetFolderPath("Startup")
$shortcutPath = Join-Path -Path $startupFolder -ChildPath "Battery.lnk"

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)
$Shortcut.TargetPath = $exePath
$Shortcut.WorkingDirectory = (Get-Location).Path
$Shortcut.Save()

Write-Host "Battery has been added to startup. It will run automatically when Windows starts."