<!-- Javascript functions-->
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.js" integrity="sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE=" crossorigin="anonymous"></script>
<script type="text/javascript" src="jquery.js"></script>
<!--Html functions-->
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
		<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
		<!-- Optional theme -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
		<link rel="stylesheet" href="estilos.css">
		<link rel = "stylesheet" href="theme.css">
		<link rel = "stylesheet" href= "bootstrap.css">
		<link rel="shortcut icon" href="#" />
		<title>Banco de carga UniGRID</title>
	</head>
	<body>
		<header>
		<center><div class = "container row" >
				<div class = "col-xs-3 col-md-3"  align = "left">
					<img src="Uninorte.png" style ="max-width: 80px; max_height:75px">
				</div>
				<div class ="col-xs-9 col-md-6" >
					<h2 id = "title-header">Modules control UniGRID</h2>
					<h5>Dpto. Ingeniería Electrónica</h5>
				</div>
		</div></center>
		</header>
		<br>
		<div style = "border:2px solid black" class = "container" id = "main">
			<section class="main row">
				<article class = "col-xs-12 col-md-9">
					<h3 id = "control-manual">Manual control</h3>
					<form action = "" class = "form-inline">
						<div class = "form-group">
							<label for = "Phase"><i>Phase</i></label>
							<select class = "form-control" id = "phase">
								<option>empty</option>
								<option value = "1">Phase 1</option>
								<option value = "2">Phase 2</option>
								<option value = "3">Phase 3</option>
							</select>
							<label for = "Position"><i>Position</i></label>
							<select class = "form-control"id= "Posicion">
								<option>empty</option>
								<option value = "0">∞</option>
								<option value = "1">240 Ω</option>
								<option value = "2">120 Ω</option>
								<option value = "3">80 Ω</option>
								<option value = "4">60 Ω</option>
								<option value = "5">48 Ω</option>
								<option value = "6">40 Ω</option>
							</select>
						</div>
						<div class = "form-group">
							<button class = "btn btn-primary" id = "btn_send" type = "button" onclick = "send_command()">Send</button>
							<button class = "btn btn-primary" id = "btn_rest" type = "button" onclick = "restore()">Reset</button>
						</div>
					</form>
					<r>
					<form class = "form-inline">
						<div class = "form-group">
							<h3 id = "demand-curves">Demand curves</h3>
						</div>
					</form>
					<form id = "upload_csv" method = "POST" enctype = "multipart/form-data"><label><i>File</i></label>
							<input type = "file" name = "in_file" id = "in_file" disabled="true" accept = ".csv"><p><i>csv format</i></p></input>
					</form>
					<button  id = "btn_submit" class ="btn btn-primary" onclick = "get_csv()">Send</button>
				</article>
				<aside  class = "col-xs-12 col-md-3">
					<br>
					<h3 class = "text-center">  Information table <h3>
					<br>
					<table class="table table-bordered">
						<tr>
							<th style = "color:white;" class ="text-center">Phase</th>
							<th style = "color:white;" class ="text-center">Position</th>
							<th style = "color:white;" class ="text-center">Value (ohms)</th>
						</tr>
						<tr>
							<td style = "color:white;" class ="text-center">1</td>
							<td style = "color:white;" class ="text-center" id = "p1"></td>
							<td style = "color:white;" class ="text-center" id = "v1"></td>
						</tr>
						<tr>
							<td style = "color:white;" class ="text-center">2</td>
							<td style = "color:white;" class ="text-center" id = "p2"></td>
							<td style = "color:white;" class ="text-center" id = "v2"></td>
						<tr>
							<td style = "color:white;" class ="text-center">3</td>
							<td style = "color:white;" class ="text-center" id = "p3"></td>
							<td style = "color:white;" class ="text-center" id = "v3"></td>
						</tr>
					</table>
				</aside>
			</section>
		</div>
		<br>
		<div class = "container">
			<div class="alert alert-info alert-dismissible" id = "oculto" style="display:none;" >
				<a class = "close" data-dismiss = "alert"><span aria-hidden = "false">&times;</span></a>
				<strong>¡File successfully loaded!</strong>
			</div>
		</div>
		<div id = "alert" class = " modal">
			<div class="modal-content">
   				<span></span>
    				<k>All other features have been disabled until the process is completed. Please wait until the process is completely done or cancel it.</p>
				<br>
				<center><div class = "progress">
                                	<div class = "progress-bar progress-bar-striped active" role = "progressbar" style = "width:100%"><i></i></div>
                                </div></center>
				<center><button id = "cancel" type = "button" class ="btn btn-secondary" onclick = "cancel()">Cancel process</button></center>
			</div>
		</div>
	<script src="http://code.jquery.com/jquery-latest.js"></script>
	<!-- Latest compiled and minified JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
	<script src = "bootstrap.js"></script>
	<script src = "functions.js"></script>
	</body>
</html>
