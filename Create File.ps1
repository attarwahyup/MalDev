# 1. Tentukan path folder tujuan
$TargetFolder = "$Home\Documents\Test Data Penting"

# 2. Cek apakah folder sudah ada, kalau belum ada maka buat baru
if (-not (Test-Path -Path $TargetFolder)) {
    New-Item -Path $TargetFolder -ItemType Directory | Out-Null
    Write-Host "[+] Folder 'Test Data Penting' berhasil dibuat di: $TargetFolder" -ForegroundColor Green
} else {
    Write-Host "[!] Folder sudah ada, langsung lanjut generate file dummy..." -ForegroundColor Yellow
}

# 3. List data dummy yang mau dibuat (Nama File dan Isinya)
$DummyFiles = @{
    "rahasia_perusahaan.txt" = "Ini adalah data finansial rahasia kuartal ini. Jangan disebarluaskan."
    "daftar_password.txt"   = "admin:Admin123!`nuser1:Password2026!`nroot:SuperSecretRootPass"
    "rencana_project.txt"   = "Project Alpha: Migrasi server backend selesai pada akhir bulan ini."
    "data_nasabah.csv"      = "Nama,Email,NoHP`nBudi,budi@mail.com,0812345678`nSiti,siti@mail.com,0819876543"
}

# 4. Generate file dummy ke dalam folder tersebut
foreach ($FileName in $DummyFiles.Keys) {
    $FilePath = Join-Path -Path $TargetFolder -ChildPath $FileName
    $Content = $DummyFiles[$FileName]
    
    # Tulis isi konten ke file teks murni
    Set-Content -Path $FilePath -Value $Content
    Write-Host "    -> File dibuat: $FileName" -ForegroundColor Cyan
}

Write-Host "[+] Semua data dummy siap digunakan untuk pengujian lab!" -ForegroundColor Green