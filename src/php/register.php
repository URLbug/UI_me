<?php
include 'connect.php';

if(isset($_POST['firstName'], $_POST['lastName'], $_POST['email'], $_POST['password'])){
    $firstName = htmlspecialchars($_POST['firstName']); 
    $lastName = htmlspecialchars($_POST['lastName']); 
    $email = htmlspecialchars($_POST['email']); 
    $password = md5(htmlspecialchars($_POST['password']));

    $stmt = $conn->prepare('INSERT INTO user (first_name, last_name, email, password) VALUES (?, ?, ?, ?)');

    $stmt->bind_param('ssss', $firstName, $lastName, $email, $password);

    $stmt->execute();
    $stmt->close();

    header('Location: /index.php');
    exit;
}
?>