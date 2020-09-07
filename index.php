<?php
$client1 = file_get_contents('http://34.239.126.215/');
$client2 = file_get_contents('http://54.84.195.147/');
echo "Server1 " . $client1 . "<br>";
echo "Server2 " . $client2 . "<br>";
?>
