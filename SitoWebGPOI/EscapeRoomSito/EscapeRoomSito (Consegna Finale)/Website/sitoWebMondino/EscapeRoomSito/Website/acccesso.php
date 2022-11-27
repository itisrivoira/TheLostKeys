<?php
    //require 'login.html';

    if(isset($_POST['invia'])) {
        if (!empty($_POST['username']) && !empty($_POST['password'])) {
            session_start();
            $username = $_POST['username'];
            $pass = $_POST['password'];

            $cn = new mysqli('localhost', 'root', '', 'testlogin');
                    
            if ($cn->connect_errno) {
                echo "<h3 class='h3'>Connessione fallita: ". $cn->connect_error . ".</h3>";
                exit();
            }   

            $password = hash('sha256', $pass);
            $query = "SELECT * FROM utente WHERE BINARY username = '$username' AND password = '$password'";
            $rquery = $cn->query($query);

            if($rquery->num_rows) {
                $row = $rquery->fetch_all(MYSQLI_BOTH);

                $_SESSION['username'] = $row[0]['username'];
                $_SESSION['password'] = $row[0]['password'];


                echo "<h3 class='h3'>Accesso avvenuto con successo</h3>";
                if ($_POST['escaperoom'] == '0') {
                    header('Refresh:1; URL = https://MaisaniSimone.github.io/SoulEnigmistaGhostato');             
                } else if ($_POST['escaperoom'] == '1') {
                    header('Refresh:1; URL = https://matteoseimandi.github.io/TheLostKey');             
                } else if ($_POST['escaperoom'] == '2') {
                    header('Refresh:1; URL= https://justdevendra.github.io/KikisKeyWebGame');             
                } else if ($_POST['escaperoom'] == '3') {
                    header('Refresh:1; URL= https://giachi03.github.io/TrappedWebApp');             
                }
            } else {
                session_destroy();
                echo "<h3 class='h3'>Accesso rifiutato</h3>";
                header('Refresh:1; URL=login.html');
            }
            

            $cn->close();
        } else {
            echo "<h3 class='h3'>Non hai inserito tutti i dati, riprova</h3>";
            header('Refresh:1; URL=login.html');
        }
    }
?>