var x;
x=$(document);
x.ready(inicializarEventos);

function inicializarEventos()
{
var x;
x=$("#titulo1");		 //recuperamos selector
x.click(presionTitulo1) //a través del método click invocamos la función.


x=$("#titulo2");
x.click(presionTitulo2)

x=$("tr");				//recuperamos selector de fila
x.click(presionFila);	//invocamos al metodo presionFila al hacer click


x=$("#boton1");		//recuperamos el id del boton
x.click(resaltar);		//invocamos a la funcion resaltar a partir del evento click


}

function presionTitulo1() //definición de la función, modificamos estilo
{
var x;
x=$("#titulo1");
x.css("color","#BA4A00");
x.css("background-color","#D1F2EB");
x.css("font-family","Courier");
}


function presionTitulo2()
{
var x;
x=$("#titulo2");
x.css("color","#ffff00");
x.css("background-color","#D1F2EB");
x.css("font-family","Arial");
}

function presionFila()
{
var x;
x=$(this); //fila actual
x.css("background-color","#4AB080 ");
}

function resaltar()
{
var x;
x=$(".resaltado");
x.css("background-color","#ffff00");
}



