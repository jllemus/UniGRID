function send_command(){
	var position = document.getElementById("Posicion").value;
	var phase = document.getElementById("phase").value;
	$.ajax({
	url:'send.php',
	type:'GET',
	data:{phase:phase,position: position},
	success: function(data){
		if(data != ""){
			alert(data);
			}
		}
	});
}

setInterval(function reload_info_table(){
	$.ajax({
	url:'retrieve.php',
	dataType:'json',
	success: function(data){
			//extracting json data from turnon.php file;
			var obj_que = jQuery.parseJSON(JSON.stringify(data));
			$(jQuery.parseJSON(JSON.stringify(data))).each(function(){
				var p1 = this.phase1;
				var p2 = this.phase2;
				var p3 = this.phase3;
				var v1 = this.res1;
				var v2 = this.res2;
				var v3 = this.res3;
				var c = this.control;
				document.getElementById("p1").innerHTML = p1;
				document.getElementById("p2").innerHTML = p2;
				document.getElementById("p3").innerHTML = p3;
				document.getElementById("v1").innerHTML = v1;
				document.getElementById("v2").innerHTML = v2;
				document.getElementById("v3").innerHTML = v3;
				if(c == 1){
					modify_elements(true);
				}else{
					modify_elements(false);
				}
			});
		}
	});
},500);

function restore(){
	$.ajax({
	url:'reset.php',
	type:'GET',
	data:{sw:1},
	});
}

function get_csv(){
        var fileinput = document.getElementById("in_file");
        var reader = new FileReader();
        var array_spl = [];
        reader.onload = function () {
                res_str = reader.result;
                var array = res_str.split("\n");
                for(i = 1; i < array.length; i++){
                        array_spl.push(array[i].split(","));
                        phase1 = array_spl[0];
                        phase2 = array_spl[1];
                        phase3 = array_spl[2];
                        time = array_spl[3];
                }
                send_csv(phase1,phase2,phase3,time,array_spl);
        };
        reader.readAsText(fileinput.files[0], 'utf8');
}

function send_csv(p1,p2,p3,t,arr){
        document.getElementById('oculto').style.display = 'block';
        document.getElementById('alert').style.display = 'block';
        $.ajax({
                url:'csv.php',
                type:'GET',
                data:{phase1:p1,phase2:p2,phase3:p3,time:t,array:arr},
                success: function(data){
                        alert("Process finished");
                        //document.getElementById('oculto').style.display = 'none';
                        document.getElementById('alert').style.display  = 'none';
                }
        });
}

function modify_elements(command){
        document.getElementById('phase').disabled = command;
        document.getElementById('Posicion').disabled = command;
        document.getElementById('btn_send').disabled = command;
        document.getElementById('btn_rest').disabled = command;
	document.getElementById("btn_submit").disabled = command;
	document.getElementById("in_file").disabled = command;
}

function cancel(){
	$.ajax({
		url:'cancel.php',
		type:'GET',
	});
}
function close(){
	document.getElementById('oculto').style.display = 'none';
}
