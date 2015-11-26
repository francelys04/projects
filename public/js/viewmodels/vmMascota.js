//Variables Globales
var mascotas = ko.observableArray([]);

function MascotaViewModel() {
	var self = this;
	self.cause_page_number = 1;
	self.cause_page_size = 4;

	self.dataCause = new Array();

	function mascotasCallback(data) {		
		console.log(data)
		mascotas.removeAll();
		data.mascotas.forEach(function(data) {	
			mascotas.push(new Mascota(data.id_mascota, data.nombre, data.raza, data.tamano, data.color,data.fecha_nacimiento, data.propietario.id_propietario, data.propietario.nombre_propietario));
		});

	}
	

	buscarMascotas = function() {
		Dajaxice.mascota.dajax_buscar_mascotas(mascotasCallback);
	};

	buscarMascotas();
   
    
    this.gridViewModel = new ko.simpleGrid.viewModel({
        data: mascotas,
        columns: [
            { headerText: " Nombre ", rowText: "nombre"     },
            { headerText: " Raza ", rowText: "raza" },
            { headerText: " Tamaño ", rowText: "tamano" },
            { headerText: " Color ", rowText: "color" },
            { headerText: " Fecha de Nacimiento", rowText: "fechaNacimiento" },           
            { headerText: "Nombre Propietario", rowText: "nombrePropietario" }
        ],
        pageSize: 50
    });

}
// ko.applyBindings(new CauseViewModel());
ko.applyBindings(MascotaViewModel(), document.getElementById("mascotaViewModel"));