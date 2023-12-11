<?php
$config = file_get_contents('config.json');
$config = json_decode($config, true);

$conn = new mysqli($config['host'], $config['username'], $config['password']);

$db_selected = $conn->select_db($config['database']);
?>