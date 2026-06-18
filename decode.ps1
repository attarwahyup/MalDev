Get-ChildItem -Path "$Home\Documents\Test Data Penting" -Filter "*.locked" -Recurse | ForEach-Object {
    # 1. Baca isi teks Base64 dari file .locked
    $EncodedContent = Get-Content $_.FullName -Raw
    
    # 2. Kembalikan teks Base64 ke dalam bentuk Byte, lalu konversi ke teks UTF-8 asli
    $Bytes = [Convert]::FromBase64String($EncodedContent)
    $DecodedContent = [System.Text.Encoding]::UTF8.GetString($Bytes)
    
    # 3. Tulis kembali isi asli ke dalam file
    Set-Content -Path $_.FullName -Value $DecodedContent
    
    # 4. Hapus ekstensi ".locked" dari nama file
    $NewName = $_.Name -replace '\.locked$', ''
    Rename-Item -Path $_.FullName -NewName $NewName
}