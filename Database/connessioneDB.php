<?php
session_start();
error_reporting(E_ERROR | E_PARSE);
$db_host = 'localhost'; #connessione al db
$db_user = 'root';
$db_pass = '';
$db_name = 'TheLostKeys';
$cn = new mysqli($db_host, $db_user, $db_pass, $db_name);
if ($cn->connect_errno) {
    echo "Connessione fallita: ". $cn->connect_error . ".";
    exit();
};
if (!empty($_SESSION['nutente']) && !empty($_SESSION['password'])) {
    $controllo = "SELECT * FROM utenti WHERE Nickgame = ' ". $_SESSION['nutente']. "'";
    $rcontrollo = $cn->query($controllo); #eseguo la query e vedo se va a buon fine
        if($rcontrollo->num_rows) { #controllo se la query restituisce righe (se l'utente esiste già nel nostro log
            $row = $rcontrollo->fetch_all(MYSQLI_BOTH);
            $_SESSION['utentelog'] = $_SESSION['nutente'];
            header("location:index.html"); #restituisce la pagina principale di Giulio
        } else {
            $query = "INSERT INTO utenti (Nickname, Email) VALUES ( ' ". $_SESSION['nutente'] . "', ' ".$_SESSION['psw']. " ');";
            $rquery =  $cn->query($query);
        };
}else{
    header("location:index.html"); #restituisce la pagina principale di Giulio
}





?>