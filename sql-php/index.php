<?php

function findName($mydb, $mail) {

	$sql = "SELECT * FROM customer where email = '{$mail}'";
	$result = $mydb->query($sql);

	if ($row = $result->fetch_assoc()) {
		echo "		<p class='font-weight-bold'>Welcome {$row['first_name']} {$row['last_name']}</p>\n";
		$rtn = "{$row['customer_id']}\n";
	} else {
		echo "		please enter valid email\n";
		$rtn = "";
	}

	return $rtn;
}

function postHidden($page) {
	echo "<input type='hidden' id='page' name='page' value='{$page}'>\n";
	echo "<input type='hidden' id='email' name='email' value='{$_POST['email']}'>\n";
	echo "<input type='hidden' id='actor' name='actor' value='{$_POST['actor']}'>\n";
	echo "<input type='hidden' id='genre' name='genre' value='{$_POST['genre']}'>\n";
	echo "<input type='hidden' id='rating' name='rating' value='{$_POST['rating']}'>\n";
	echo "<input type='hidden' id='movie_id' name='movie_id' value='{$_POST['movie_id']}'>\n";
	if (isset($_POST['mine'])) {
		echo "<input type='hidden' id='mine' name='mine' value='{$_POST['mine']}'>\n";
	}
}
?>


<?php
	
	$servername = "localhost";
	$username = "root";
	$password = "root";
	$database = "sakila";
	
	$mydb = new mysqli($servername, $username, $password, $database);

	if ($mydb->connect_error) {
	  die("Connection failed: -" . $mydb->connect_error);
	}

	echo "<!DOCTYPE html>
		<html>
		<head>

		<meta charset='utf-8'>
		<meta name='viewport' content='width=device-width, initial-scale=1'>
		<title>playing with sql</title>
		<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet'>
		<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js'></script>

		</head>
		<body>\n";

	//var_dump($_POST);

	if (!isset($_REQUEST['page']) || $_REQUEST['page'] == "1") {
		echo "<br>";
		echo "<div class='container p-5 my-5 border border-2'>";

		echo "<div class='row col-sm-6 border border-2'>";
		

		echo "<form action='index.php' method='post'>\n";
		
		$sql = "SELECT name, category_id FROM sakila.category";
		$result = $mydb->query($sql);
        
		if (isset($_REQUEST['email'])) {			
			$email = $_REQUEST['email'];
		} else {
			$email = "";
		}

		if ($result->num_rows > 0) {
			echo "<label for='email'>Email Address:</label><br>";
			echo "<input class=' col-xs-2' type='text' id='email' name='email' value=$email ><br><br>";
			echo "<select class=' col-xs-2' name='genre' id='genre'>\n";
			echo "<option class='dropdown-item' value=''>Pick Genre</option>\n";
			  
			while($row = $result->fetch_assoc()) {
				echo "<option class='dropdown-item' value='{$row['category_id']}'>{$row['name']} </option>\n";
			}
			echo "</select>\n";
		
		} else {
			echo "0 results";
		}

		$sql = "SELECT rating FROM ratings";
		$rating = $mydb->query($sql);

		if ($rating->num_rows > 0) {
		  
			echo "<br><br><select class=' col-xs-2' name='rating' id='rating'>\n";
			echo "<option class='dropdown-item' value=''>Pick Rating</option>\n";
					  
			while($row = $rating->fetch_assoc()) {
				echo "<option class='dropdown-item' value='{$row['rating']}'>{$row['rating']}</option>\n";
			}
			echo "</select>\n";
			  		
		} else {
			echo "0 results";
		}

		$sql = "SELECT actor_id, first_name, last_name FROM sakila.actor";
		$actor = $mydb->query($sql);

		if ($actor->num_rows > 0) {
		  
			echo "<br><br><select class=' col-xs-2' name='actor' id='actor'>\n";
			echo "<option class='dropdown-item' value=''>Pick actor</option>\n";
		  
			while($row = $actor->fetch_assoc()) {
				echo "<option class='dropdown-item' value='{$row['actor_id']}'>{$row['first_name']} {$row['last_name']}</option>\n";
			}
			echo "</select>\n";
			
		} else {
			echo "0 results";
		}
		
		echo "<br><br><input type='radio' name='mine' value='1' onclick='submit();'>Show my past rentals\n";
		
		echo "<br><br><input type='submit' value='Submit'>";
		echo "<input type='hidden' id='page' name='page' value='2'>";
		
		echo "</form>";

		echo "</div>";
	
		echo "</div>";
	
		$mydb->close();
		
	} elseif ($_REQUEST['page'] == "2")  {
		 
		echo "<div class='container p-5 my-5 borderder-2'>";

		echo "<div class='row col-sm-6 border border-2'>"; 
		 
		 
		$foundEmail = findName($mydb, $_POST['email']);
		echo "<form action='index.php' method='post'>";
		if (isset($_POST['mine'])) {
			$sql = "SELECT 
						fi.title,
						fi.film_id
					from 
						film as fi
					inner join
						inventory as iv on iv.film_id = fi.film_id
					inner join
						rental as re on re.inventory_id = iv.inventory_id
					where 
						re.customer_id = {$foundEmail}";
			$result = $mydb->query($sql);
			while($row = $result->fetch_assoc()) {
			
				echo "<div class='radio'>
					<label><input type='radio' name='movie_id' value={$row['film_id']} onclick='submit();'>{$row['title']}</input></label>
					</div>";	
			}
			
			echo "<input type='hidden' id='page' name='page' value='3'>\n";
			echo "<input type='hidden' id='email' name='email' value='{$_POST['email']}'>\n";
			echo "<input type='hidden' id='actor' name='actor' value='{$_POST['actor']}'>\n";
			echo "<input type='hidden' id='genre' name='genre' value='{$_POST['genre']}'>\n";
			echo "<input type='hidden' id='rating' name='rating' value='{$_POST['rating']}'>\n";
			echo "<input type='hidden' id='mine' name='mine' value='{$_POST['mine']}'>\n";
			echo "</form>";
			
			echo "<form action='index.php' method='post'>\n";
			echo "<input type='hidden' id='email' name='email' value='{$_POST['email']}'>\n";

			echo "<input type='submit' value='Start over' name='page' value=''>\n";
			echo "<input type='hidden' id='page' name='page' value='1'>\n";		
			
			echo "</form>";
			
		} else {
		
			if ($_REQUEST['actor'] != "" && $_REQUEST['genre'] != "" && $_REQUEST['rating'] != ""){
				
				$sql_add = "WHERE\n
					film_actor.actor_id = {$_REQUEST['actor']}\n
				AND\n
					category.category_id = {$_REQUEST['genre']}\n
				AND\n
					film.rating = '{$_REQUEST['rating']}'";
					
			} elseif ($_REQUEST['genre'] != "") {
				if ($_REQUEST['rating'] != "") {
					
				$sql_add = "WHERE\n
					category.category_id = {$_REQUEST['genre']}
							AND\n
					film.rating = '{$_REQUEST['rating']}'";		
				
				} elseif ($_REQUEST['actor'] != "") {
					
				$sql_add = "WHERE\n
					category.category_id = {$_REQUEST['genre']}
							AND\n
					film_actor.actor_id = {$_REQUEST['actor']}\n";		
				
				} else {
					$sql_add = "WHERE\n
						category.category_id = {$_REQUEST['genre']}";
				}
				
			} elseif ($_REQUEST['rating'] != ""){
				if ($_REQUEST['actor'] != "") {
					
				$sql_add = "WHERE\n
					film.rating = '{$_REQUEST['rating']}'
							AND
					film_actor.actor_id= {$_REQUEST['actor']}";		
				
				} elseif ($_REQUEST['genre'] != "") {
					
				$sql_add = "WHERE\n
					film.rating = '{$_REQUEST['rating']}'
							AND\n
					category.category_id = {$_REQUEST['genre']}\n";		
				
				} else {
					$sql_add = "WHERE\n
						film.rating = '{$_REQUEST['rating']}'";
				}
				
				
			} elseif ($_REQUEST['actor'] != ""){
				
				if ($_REQUEST['actor'] != "") {
					
				$sql_add = "WHERE\n
					category.category_id = {$_REQUEST['actor']}
							AND\n
					film.rating = '{$_REQUEST['rating']}'";		
				
				} elseif ($_REQUEST['actor'] != "") {
					
				$sql_add = "WHERE\n
					category.category_id = {$_REQUEST['genre']}
							AND\n
					film_actor.actor_id = {$_REQUEST['actor']}\n";		
				
				} else {
					$sql_add = "WHERE\n
						film_actor.actor_id = {$_REQUEST['actor']}\n";
				}
				
				
				$sql_add = "WHERE\n
					film_actor.actor_id = {$_REQUEST['actor']}";
				
			} else {
				$sql_add = "WHERE\n
					film_actor.actor_id >= 1";
			}
			
			$sql = "
				SELECT DISTINCT
					actor.first_name,
					actor.last_name,
					film_actor.film_id,
					film.title,
					category.name
				FROM 
					actor
						INNER JOIN
					film_actor ON actor.actor_id = film_actor.actor_id
						INNER JOIN
					film on film.film_id = film_actor.film_id
						INNER JOIN
					film_category on film_category.film_id = film_actor.film_id
						INNER JOIN
					category on film_category.category_id = category.category_id
				
					";
			$sql .= $sql_add ;
				
			$result = $mydb->query($sql);
				
			$prev_row = "";
				
			
			echo "<form action='index.php' method='post'>";
			if ($foundEmail != "")  {
				echo "<div class='col h3 text-primary'>Select a movie:</div><div>\n";
			}
			while($row = $result->fetch_assoc()) {
				if ($foundEmail == "")  {
					echo "Please enter email\n";
					echo "<input type='hidden' id='page' name='page' value='1'>\n";
					echo "<input type='submit' value='Sbmit'>";
					echo "</form>\n";
					break;
				} 
		
				if ($row['film_id'] == $prev_row){
					continue;
				}

				echo "<div class='radio'>
				<label><input type='radio' name='movie_id' value={$row['film_id']} onclick='submit();'>{$row['title']}</input></label>
				</div>";
				$prev_row = $row['film_id'];
			}
			if ($foundEmail != "")  {
				echo "<input type='hidden' id='page' name='page' value='3'>\n";
				echo "<input type='hidden' id='email' name='email' value='{$_POST['email']}'>\n";
				echo "<input type='hidden' id='actor' name='actor' value='{$_POST['actor']}'>\n";
				echo "<input type='hidden' id='genre' name='genre' value='{$_POST['genre']}'>\n";
				echo "<input type='hidden' id='rating' name='rating' value='{$_POST['rating']}'>\n";
				

			} else {
					//echo "<input type='hidden' id='page' name='page' value='3'>";
			}
			
			echo "</form>";	
			echo "<form action='index.php' method='post'>\n";
			echo "<input type='hidden' id='email' name='email' value='{$_POST['email']}'>\n";

			echo "<input type='submit' value='Start over' name='page' value=''>\n";
			echo "<input type='hidden' id='page' name='page' value='1'>\n";		
			
			echo "</form>";
		}
		echo "</div>";
		echo "</div>";
		echo "</div>";
		$mydb->close();
		
	} elseif ($_REQUEST['page'] == "3")  {
		echo "<br>";
		echo "<div class='container p-5 my-5 border border-2'>";
		echo "<div class='row border border-2'>";
		echo "<form action='index.php' method='post'>\n";

		$foundEmail = findName($mydb, $_POST['email']);
	
		echo "<div class='container p-5 my-5 border border-2'>";
		echo "<div class='row'>";
		
		echo "<div class='col'>";

		if (isset($_POST['mine'])) {
			
			$sql = "SELECT 
						re.rental_date,
						re.customer_id,
						re.inventory_id
					from 
						rental as re
					inner join
						inventory as iv on iv.inventory_id = re.inventory_id
					where 
						re.customer_id = '{$foundEmail}'
					and 
						iv.film_id = '{$_POST['movie_id']}'";
			
			$result = $mydb->query($sql);
			$row = $result->fetch_assoc();

			$pattern = '/ [0-9]*:[0-9]*:[0-9]*/';
			$str = $row['rental_date'] ;
			$str = preg_replace($pattern, '', $str);
			echo "<b>You rented this movie on</b> {$str}<br>";
			
		}

		$sql = "SELECT DISTINCT
			film.title,
			film.description,
			film.special_features,
			category.name
		FROM 
			film
				INNER JOIN
			film_actor ON film.film_id = film_actor.film_id
				INNER JOIN 
			film_category ON film_category.film_id = film.film_id
				INNER JOIN
			category on film_category.category_id = category.category_id
		where
			film.film_id = {$_REQUEST['movie_id']}";

		$result = $mydb->query($sql);
		while($row = $result->fetch_assoc()) {
			$features = $row['special_features'];
			$genre = $row['name'];
			echo "<div class='h3'>{$row['title']}:</div><div class='h5'>[{$genre}]</div> {$row['description']}\n";
		}
		
		$sql = "SELECT DISTINCT
				film.title,
				film.rating,
				film.length,
				film.language_id, 
                actor.first_name,
                actor.last_name
			FROM 
				film
					INNER JOIN
				film_actor ON film.film_id = film_actor.film_id
					inner join
				actor on actor.actor_id = film_actor.actor_id
			where
				film.film_id = {$_REQUEST['movie_id']}";
		$result = $mydb->query($sql);
		
		echo "<p class='h3 '>Starring:</p><p class='h3'>";
		while($row = $result->fetch_assoc()) {
			echo "<div class='font-weight-bold'>{$row['first_name']} {$row['last_name']}</div>\n";
			$rating = $row['rating'] ;
			$length = $row['length'] ;
			$language = $row['language_id'] ;
		}
		echo "<br><div class='font-weight-bold'>Containing:</div><div>{$features}</div>\n";
		echo "</div>\n";
		echo "<div class='col'>\n";
		echo "<br><br><br><br><p><b>Rating</b> {$rating}</p>\n";
		echo "<p><b>length</b> {$length} minutes</p>\n";
		$sql = "SELECT name FROM language where language_id = $language";
		$result = $mydb->query($sql);
		$row = $result->fetch_assoc();
		echo "<p><b>language</b> {$row['name']} </p>\n";
		
		
		echo "<form action='index.php' method='post'>\n";
			postHidden('2');

			echo "<br><input type='submit' value='Pick Another Movie'><br>\n";
		
		echo "</form>\n";
		echo "<form action='index.php' method='post'>\n";		
			echo "<br><br><input type='submit' value='Rent This Movie' name='page' value=''>\n";
			postHidden('4');
		echo "</form>\n";
		
		echo "<div class='col'></div>\n";
		echo "</div>\n";
		echo "</div>\n";
		$mydb->close();
		
	} elseif ($_REQUEST['page'] == "4")  {
		echo "<br>";
		echo "<div class='container p-5 my-5 border border-2'>";
		echo "<div class='row border border-2'>";
		echo "<form action='index.php' method='post'>\n";

		$foundEmail = findName($mydb, $_POST['email']);

		$sql = "SELECT 
				cu.first_name, 
				cu.last_name, 
				cu.email, 
				ci.city,
				co.country,
				ad.address ,				
				ad.district ,				
				ad.postal_code ,				
				ad.phone 			
			
			FROM 
				customer as cu
					INNER JOIN
				address as ad ON cu.address_id = ad.address_id
					INNER JOIN
				city as ci ON ci.city_id = ad.city_id
					INNER JOIN
				country as co on co.country_id = ci.country_id
					WHERE
				cu.customer_id = '{$foundEmail}'";

		$result = $mydb->query($sql);

		if ($row = $result->fetch_assoc()) {
			echo "<p class='font-weight-bold'>Please verify your information</p>";
			echo "<p>{$row['first_name']} {$row['last_name']}\n</p>";
			echo "{$row['address']}\n<br>";
			echo "{$row['city']},  {$row['district']}\n";
			
			echo "<div class='row'>";
			echo "<br><span class='col-sm-1 '></span>"; 
			echo "<span class='col-sm-7 '>"; 
			
			
			echo "{$row['postal_code']}\n";
			echo "</span>";
			echo "</div>";
			//echo "<span class='col-sm-4 border border-2'>ffg</span>"; 

			echo "{$row['country']}\n";
			echo "<br>Phone: {$row['phone']}<br><br>\n";
			echo "<form action='index.php' method='post'>\n";
			
				echo "<input type='submit' value='Yes Thats Me' name='page' value=''>\n";
				postHidden('5');

			echo "</form>\n";
			echo "</div>\n";
			echo "</div>\n";
			echo "</div>\n";
		}
		$mydb->close();
		
	} elseif ($_REQUEST['page'] == "5" || $_REQUEST['page'] == "6")  {
		echo "<br>";
		echo "<div class='container p-5 my-5 border border-2'>";
		echo "<div class='row border border-2'>";
		echo "<form action='index.php' method='post'>\n";

		if ($_REQUEST['page'] == "6") {
			$sql = "UPDATE rental SET returned = '1' WHERE (rental_id={$_REQUEST['rental']})";
			$result = $mydb->query($sql);
		}
		
		echo "<br><br>";
		$foundEmail = findName($mydb, $_POST['email']);
		
		$sql = "select 
				fi.title,
				cu.last_name,
				re.customer_id,
				re.rental_id ,
				fi.last_update,
				re.rental_date,
				re.inventory_id
			FROM 
				film as fi
					INNER JOIN
				inventory as iv on fi.film_id = iv.film_id
					INNER JOIN
				rental as re on re.inventory_id = iv.inventory_id
					INNER JOIN
				customer as cu on cu.customer_id = re.customer_id
			where
				cu.customer_id = {$foundEmail}
			AND
				re.returned IS NULL ";
		$result = $mydb->query($sql);
		
		echo "<br>You have these rentals out, wouls you like to return any?\n";
		echo "<form action='index.php' method='post'>\n";
			
			postHidden('6');


		while ($row = $result->fetch_assoc()) {		
			$date1=date_create();
			$date2=date_create($row['rental_date']);
			$diff=date_diff($date2,$date1);
			$diff2 = $diff->format("%R%a days");
			echo "<br><input type='radio' name='rental' value={$row['rental_id']} onclick='submit();'>{$row['title']} - {$diff2} Days Late\n";
		}

		echo "</form>";
		
		echo "<form action='index.php' method='post'>\n";
		
			echo "<br> 	<input type='submit' value='Im Finished' name='page' value=''>\n";
			postHidden('7');

		echo "</form>\n";
		$mydb->close();
		
	} elseif ($_REQUEST['page'] == "7")  {
		echo "<br>";
		echo "<div class='container p-5 my-5 border border-2'>";
		echo "<div class='row border border-2'>";
		echo "<form action='index.php' method='post'>\n";
	
		$movie_id = $_POST['movie_id'];

		$sql = "SELECT 
				count(inventory_id) as count 
			from rental		
			
			where
				inventory_id = {$movie_id}";
			
		$result = $mydb->query($sql);
		$row = $result->fetch_assoc();
		
		$sql = "SELECT 
				title
			from film		
			
			where
				film_id = {$movie_id}";
		$result2 = $mydb->query($sql);
		$row2 = $result2->fetch_assoc();
		
		$countTotal = $row['count'];
		
		$sql = "SELECT 
				count(iv.film_id) as count
			FROM 
				inventory as iv 
					inner join
				rental  as re on re.inventory_id = iv.inventory_id
			where
				iv.film_id = {$movie_id}
			and
				re.returned is  null";
		
		$result = $mydb->query($sql);
		
		while ($row = $result->fetch_assoc()) {	
			$countOut = $row['count'];
		}
echo $sql;
		$sql = "SELECT 
				count(iv.film_id) as count
			FROM 
				inventory as iv 
					inner join
				rental  as re on re.inventory_id = iv.film_id
			where
				iv.film_id = {$movie_id}
			and
				re.returned is not null;";
		
		$result = $mydb->query($sql);

		while ($row = $result->fetch_assoc()) {	
			$countRet = $row['count'];
		}

		if ($countTotal > $countOut) {
			echo "<p>you are in luck! Your movie is in {$countTotal} {$countOut}:</p>";
			$sql = "select * from film where film_id = {$_POST['movie_id']}";
			$result = $mydb->query($sql);
			
			$row = $result->fetch_assoc();
			
			echo "{$row['title']}:<br> <b>  Release year: </b>{$row['release_year']}<b>  Length:</b> {$row['length']} <b>  Rating:</b> {$row['rating']}<br>";
			echo "<u>Rental rates</u><br>";
			echo "<b>Rental duration:</b> {$row['rental_duration']} days <b>Rental Rate:</b> \${$row['rental_rate']} <b>Replacement cost</b> \${$row['replacement_cost']}";
			$date=date_create();
			date_add($date,date_interval_create_from_date_string("{$row['rental_duration']} days"));
			$backIn = date_format($date,"Y-m-d");
			
			echo "<br><b>Due Back:</b> {$backIn} ";

			echo "<br><br><input type='submit' value='Finished' name='page' value=''>\n";
			echo "<input type='hidden' id='days' name='days' value='{$row['rental_duration']}'>\n";

			postHidden('8');

		} else {
			echo "<br>Sorry that movie is out  {$countTotal} {$countOut}";
			echo "<input type='submit' value='Finished' name='page' value=''>\n";
			postHidden('2');
		}
	} elseif ($_REQUEST['page'] == "8")  {
		
		echo "<br>";
		echo "<div class='container p-5 my-5 border border-2'>";
		echo "<div class='row border border-2'>";
		echo "<form action='index.php' method='post'>\n";

		$foundEmail = findName($mydb, $_POST['email']);
		
		$rtndate=date_create();
		date_add($rtndate,date_interval_create_from_date_string("{$_POST['days']} days"));
		$backIn = date_format($rtndate,"Y-m-d h:m:s");
		$date = date_create();
		$entrDate = date_format($date,"Y-m-d h:m:s");
		echo "<br>enter date: {$entrDate}";
		echo "<br>return_date: {$backIn} ";
		echo "<br>customer_id: {$foundEmail} ";
		echo "<br>staff_id: 1";
		echo "<br>film_id: {$_POST['movie_id']}";
		
		$sql ="select film_id, inventory_id from inventory where film_id = {$_POST['movie_id']}";
		$result = $mydb->query($sql);

		$movies = [];
		$outMovies = [];
		while ($row = $result->fetch_assoc()) {	
			array_push($movies, $row['inventory_id']);
		}
		
		$loop = 0;
		$size = sizeof($movies);
		echo "<br>size:{$size}";

		for ($inventory_id = 0; $inventory_id <= ($size - 1); $inventory_id++) {

			$sql ="select  inventory_id from rental where inventory_id = {$movies[$inventory_id]}
					AND returned is null";
			$result = $mydb->query($sql);
			$row = $result->fetch_assoc();

			if (!isset($row['inventory_id'])) {
				$inventory_id = $movies[$inventory_id];
				break;
			} 
		}
		echo "<br>inventory id: {$inventory_id}";
		
		$sql = "INSERT INTO rental (rental_date, inventory_id, customer_id, return_date, staff_id)
			VALUES ('{$entrDate}','{$inventory_id}','{$foundEmail}','{$backIn}','1')";
		$result = $mydb->query($sql);
		
		echo "<br>SQL = {$sql}<br>";
		
	} else {
		echo "<br>";
		echo "<div class='container p-5 my-5 border border-2'>";
		echo "<div class='row border border-2'>";
		echo "<form action='index.php' method='post'>\n";

		echo "wa Wa Wa";
	}

?>