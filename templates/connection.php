<?php


$str = file_get_contents('config/pace.config.json');
$json = json_decode($str, true);

$db_server = $json['host'];
$db_user = $json['user'];
$db_password = $json['pass'];
$db_schema = $json['schema'];

$db = mysqli_connect($db_server,$db_user,$db_password,$db_schema) or die('Error connecting to MySQL server.');
$query = "SELECT Longitude AS lng, Latitude AS lat, companyName AS name FROM table2 LIMIT 5";
$result = mysqli_query($db, $query) or die('Error querying database.');

$myArray = array();
while($row = $result->fetch_array()) {
    $myArray[] = $row;
}
  echo json_encode($myArray, JSON_PRETTY_PRINT);
  mysqli_close($db);
?>
