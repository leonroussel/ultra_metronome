<?php 
// $argv[0]
$xml = file_get_contents("https://templiers.livetrail.net/coureur.php?rech=3005#");

$xml_interpreted =simplexml_load_file("https://templiers.livetrail.net/coureur.php?rech=3005#") or die("Error: Cannot create object");
$json = json_encode($xml_interpreted, JSON_PRETTY_PRINT);

$fp = fopen('results.json', 'w');
fwrite($fp, $json);
fclose($fp);

?>