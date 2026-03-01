$base = "https://html-classic.itch.zone/html/16183209"
$files = @(
    "index.html",
    "renpy-pre.js",
    "renpy.js",
    "renpy.wasm",
    "renpy.data",
    "game.zip",
    "manifest.json",
    "web-presplash.jpg"
)

foreach ($f in $files) {
    $url = "$base/$f"
    $out = Join-Path $PSScriptRoot $f
    Write-Host "Downloading $f ..." -ForegroundColor Cyan
    try {
        Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing
        $size = (Get-Item $out).Length
        Write-Host "  OK - $([math]::Round($size/1MB, 2)) MB" -ForegroundColor Green
    } catch {
        Write-Host "  FAILED: $_" -ForegroundColor Red
    }
}
Write-Host "`nAll done!" -ForegroundColor Yellow
