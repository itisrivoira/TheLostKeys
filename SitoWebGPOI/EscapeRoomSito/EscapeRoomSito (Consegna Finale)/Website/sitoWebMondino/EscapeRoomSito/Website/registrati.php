<?php
    //require 'login.html';
    session_start();
    if (isset($_POST['invia'])) {
        $db_host = 'localhost';
        $db_user = 'root';
        $db_pass = '';
        $db_name = 'testlogin';
        $cn = new mysqli($db_host, $db_user, $db_pass, $db_name);
        if ($cn->connect_errno) {
            echo "Connessione fallita: ". $cn->connect_error . ".";
            exit();
        }
        if (empty($_POST['username']) || empty($_POST['password'])) {
            echo "Non sono stati inseriti tutti i campi richiesti...";
        } else {
            $email = $_POST['email'];
            $data = $_POST['data'];
            $nomeutente = $_POST['username'];
            $psw = hash('sha256', $_POST['password']);
            $sql = "INSERT INTO utente (username , password) VALUES ('". $nomeutente . "', '". $psw . "') ;"; 
            if (!$cn->query($sql)) {
                echo "Errore della query: " . $cn->error . ".";
            }else{
                echo "Dati inseriti correttamente";
                header('Refresh:1; URL=login.html');
            }
        }
    } else {
         echo "Da dove arrivi??";
    }
?>