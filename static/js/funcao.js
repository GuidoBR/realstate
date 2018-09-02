//variáveis globais
var largura =  window.innerWidth || document.documentElement.clientWidth; 
var flag=0;



// área da funções
function loop()
{
    setInterval('detectaBar()', 1000);
}


function config_inicial()
{

    //Calculando área disponível - Altura
	var altura =  window.innerHeight || document.documentElement.clientHeight;

	
	//ajustando abertura
	document.getElementById("abertura").style.height= altura+"px";
	$('body').css("overflow-y","hidden");


	
}


function detectaBar()
{
         
    if($('body').scrollTop() > 180)
    {
        if(largura>1024)
        {
            //Altera estilo do height para outro valor
    		$('.bar_selecao').animate({height:"60px"},200,function(){
    			 
                
                    //Exibe logotipo                
                	$('#logo_mini').css('display','inline-block');
                	$('#logo_mini').animate({opacity:"1.0"},200);
                
    		});
        }
    }
    else
    {
        //Oculta logotipo
        $('#logo_mini').animate({opacity:"0.0"},200, function(){$('#logo_mini').css('display','none');});

        //Ajusta height para fixo
        $('.bar_selecao').animate({height:"40px"},200)
    }
   
}


function pop_menu()
{

    $("#bt_menu").click(function(){ 
        
        if(flag==0)
        {
            $(".guias3").css("display","block");//descloqueia a div
            $(".guias3").animate({opacity:1.0},500);//torna DIV visível
            flag=1;
        }
        else
        {
            $(".guias3").animate({opacity:0.0},500, function(){
            
                $(".guias3").css("display","none");
                $(".guias3").animate({opacity:1.0},500);//torna DIV visível p/ ser reutilizada
            });
                
            flag=0;
        }
        
    });

}


function GetBuscaImovel(tipo_locacao)
{
    //Instanciando objeto
    var xmlreq = new XMLHttpRequest();

    //Capturando variáveis do form de busca
    var par1=document.form_busca.tipo_imovel.value;
    var par2=document.form_busca.valor.value;

    if(tipo_locacao=='ALUGUEL-COMERCIAL'){ var par3=document.form_busca.area.value;}else{ var par3=document.form_busca.num_quartos.value;}

    var par4=document.form_busca.local.value;


    // Exibi a imagem de progresso
    document.getElementById("imoveis_selecionados").style.display="block";
    document.getElementById("carregando").style.display="block";

    // Requisição
    xmlreq.open("GET", "../busca-imovel.php?par1="+par1+"&par2="+par2+"&par3="+par3+"&par4="+par4+"&tipo="+tipo_locacao, true);

    // Atribui uma função para ser executada sempre que houver uma mudança de ado
    xmlreq.onreadystatechange = function(){
     
         // Verifica se foi concluído com sucesso e a conexão fechada (readyState=4)
         if (xmlreq.readyState == 4)
         {
             
             // Verifica se o arquivo foi encontrado com sucesso
             if (xmlreq.status == 200) {
                 //Desativa animação de carregando
                 document.getElementById("carregando").style.display="none";

                 //aPONTA PARA A ÂNCORA
                 $('html,body').animate({scrollTop: $('#imoveis_selecionados').offset().top}, 2000);
                 
                 //adiciona a rsposta à ID
                 result_busca.innerHTML = xmlreq.responseText;
             }
             else
             {
                result_busca.innerHTML = "Erro: " + xmlreq.statusText;
             }

         }
    };

    xmlreq.send(null);


}



function atualizaValor(tipo_locacao,tipo_imovel)
{

    //Instanciando objeto
    var xmlreq= new XMLHttpRequest();   

    xmlreq.open("GET", "../atualizaValor.php?tipo_locacao="+tipo_locacao+"&tipo_imovel="+tipo_imovel, true);

    xmlreq.onreadystatechange = function(){
     
         // Verifica se foi concluído com sucesso e a conexão fechada (readyState=4)
         if (xmlreq.readyState == 4)
         {
             
             // Verifica se o arquivo foi encontrado com sucesso
             if (xmlreq.status == 200) {
                 
                 //adiciona a rsposta à ID
                 option_valor.innerHTML = xmlreq.responseText; 
             }
             else
             {
                 option_valor.innerHTML = "Erro: " + xmlreq.statusText;
             }

         }
    };

    xmlreq.send(null);

}


function atualizaQuartos(tipo_locacao,valor)
{
    //Obtendo resultados dos forms
    var tipo_imovel=document.form_busca.tipo_imovel.value;

    //Instanciando objeto
    var xmlreq= new XMLHttpRequest();  

    xmlreq.open("GET", "../atualizaQuarto.php?tipo_locacao="+tipo_locacao+"&tipo_imovel="+tipo_imovel+"&valor="+valor, true);

    xmlreq.onreadystatechange = function(){
     
         // Verifica se foi concluído com sucesso e a conexão fechada (readyState=4)
         if (xmlreq.readyState == 4)
         {
             
             // Verifica se o arquivo foi encontrado com sucesso
             if (xmlreq.status == 200) {
                 
                 //adiciona a rsposta à ID
                 option_quartos.innerHTML = xmlreq.responseText; 
             }
             else
             {
                 option_quartos.innerHTML = "Erro: " + xmlreq.statusText;
             }

         }
    };

    xmlreq.send(null);

}


function atualizaArea(tipo_locacao,valor)
{
    //Obtendo resultados dos forms
    var tipo_imovel=document.form_busca.tipo_imovel.value;

    //Instanciando objeto
    var xmlreq= new XMLHttpRequest();  

    xmlreq.open("GET", "../atualizaArea.php?tipo_locacao="+tipo_locacao+"&tipo_imovel="+tipo_imovel+"&valor="+valor, true);

    xmlreq.onreadystatechange = function(){
     
         // Verifica se foi concluído com sucesso e a conexão fechada (readyState=4)
         if (xmlreq.readyState == 4)
         {
             
             // Verifica se o arquivo foi encontrado com sucesso
             if (xmlreq.status == 200) {
                 
                 //adiciona a rsposta à ID
                 option_area.innerHTML = xmlreq.responseText; 
             }
             else
             {
                 option_area.innerHTML = "Erro: " + xmlreq.statusText;
             }

         }
    };

    xmlreq.send(null);

}



function atualizaLocal(tipo_locacao,quarto)
{
    //Obtendo resultados dos forms
    var tipo_imovel=document.form_busca.tipo_imovel.value;
    var valor=document.form_busca.valor.value;

    //Instanciando objeto
    var xmlreq= new XMLHttpRequest();  

    xmlreq.open("GET", "../atualizaLocal.php?tipo_locacao="+tipo_locacao+"&tipo_imovel="+tipo_imovel+"&valor="+valor+"&quarto="+quarto, true);

    xmlreq.onreadystatechange = function(){
     
         // Verifica se foi concluído com sucesso e a conexão fechada (readyState=4)
         if (xmlreq.readyState == 4)
         {
             
             // Verifica se o arquivo foi encontrado com sucesso
             if (xmlreq.status == 200) {
                 
                 //adiciona a rsposta à ID
                 option_local.innerHTML = xmlreq.responseText; 
             }
             else
             {
                 option_local.innerHTML = "Erro: " + xmlreq.statusText;
             }

         }
    };

    xmlreq.send(null);

}


function atualizaLocal2(tipo_locacao,area)
{
    //Obtendo resultados dos forms
    var tipo_imovel=document.form_busca.tipo_imovel.value;
    var valor=document.form_busca.valor.value;

    //Instanciando objeto
    var xmlreq= new XMLHttpRequest();  

    xmlreq.open("GET", "../atualizaLocal2.php?tipo_locacao="+tipo_locacao+"&tipo_imovel="+tipo_imovel+"&valor="+valor+"&area="+area, true);

    xmlreq.onreadystatechange = function(){
     
         // Verifica se foi concluído com sucesso e a conexão fechada (readyState=4)
         if (xmlreq.readyState == 4)
         {
             
             // Verifica se o arquivo foi encontrado com sucesso
             if (xmlreq.status == 200) {
                 
                 //adiciona a rsposta à ID
                 option_local.innerHTML = xmlreq.responseText; 
             }
             else
             {
                 option_local.innerHTML = "Erro: " + xmlreq.statusText;
             }

         }
    };

    xmlreq.send(null);

}