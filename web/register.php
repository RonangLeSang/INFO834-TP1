<?php
$servername = "localhost";
$username = "name";
$password = "password";
$dbname = "dbname";

// Créer la connexion
$conn = @mysqli_connect($servername, $username, $password, $dbname);

// Vérifier la connexion
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

mysqli_query($conn, "SET NAMES UTF8");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nom = mysqli_real_escape_string($conn, $_POST['nom']);
    $prenom = mysqli_real_escape_string($conn, $_POST['prenom']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $mot_de_passe = password_hash(mysqli_real_escape_string($conn, $_POST['password']), PASSWORD_DEFAULT);

    $sql = "INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe) VALUES ('$nom', '$prenom', '$email', '$mot_de_passe')";

    if (mysqli_query($conn, $sql)) {
        echo "Nouvel enregistrement créé avec succès";
    } else {
        echo "Erreur: " . $sql . "<br>" . mysqli_error($conn);
    }
}

mysqli_close($conn);
?>
