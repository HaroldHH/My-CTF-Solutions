<?php

// Flag : Neko{tEk1t0uM0ndAiT3kI7oUfLAg}

$users = array(
    "admin" => "caa6d4940850705040738b276c7bb3fea1030460",
    "guest" => "35675e68f4b5af7b995d9205ad0fc43842f16450"
);

function lookup($username) {
    global $users;
    return array_key_exists($username, $users) ? $users[$username] : "";
}

$sha1pass = lookup("guest\0admin");
echo "[*] Data :  $sha1pass\n";
if ($sha1pass == sha1([])) {
	echo "[+] Success\n";
	exit();
} else {
	echo "[-] Fail\n";
}
?>
