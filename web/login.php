<?php
session_start();

$servername = "tp-epua:3308";
$username = "cortesmc";
$password = "yeqxmat4";
$dbname = "cortesmc";

$conn = @mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

mysqli_query($conn, "SET NAMES UTF8");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $mot_de_passe = mysqli_real_escape_string($conn, $_POST['password']);

    $sql = "SELECT id, mot_de_passe FROM utilisateurs WHERE email = '$email'";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {
        $row = mysqli_fetch_assoc($result);
        if (password_verify($mot_de_passe, $row['mot_de_passe'])) {
            $_SESSION['loggedin'] = true;
            $_SESSION['userid'] = $row['id'];
            $output=shell_exec('py python/Main.py ' + userid + ' 2>&1');
            if ($output == "True"){
                echo "Vous êtes connecté!";
            }
        } else {
            echo "Mot de passe incorrect!";
        }
    } else {
        echo "Aucun utilisateur trouvé avec cet email!";
    }
}

mysqli_close($conn);
?>
