import sys
flag = 0
maxi = 0
header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        .reponse{
            display:none;
        }
        .block{
            display: block;
            padding:10px;
            margin:10px;
            border-style: none;
            width:100eh;
            height: 5ev;
            background-color:rgb(207, 229, 253);
            border-radius: 10px;
        }
        .button{
            background-color:rgb(68, 92, 226);
            border-radius: 10px;
        }
    </style>
        
</head>
<body>
    <form>
"""
footer = """            <span onclick="valider()" class="block button">Valider</span>
        </div>
    </form>
    <div class="reponse">
        Résultat : <span id="score"></span>
    </div>
</body>
    <script>
         function valider(){
            var score = 0
			
            var lesReponses=document.getElementsByClassName('reponse');
            var NbReponse=lesReponses.length;
            for (var i=0; i<lesReponses.length;i++){
                lesReponses[i].style.display='block';
            }
			
            var el=document.getElementsByTagName("input")
			for (var i = 0; i < el.length; i++) {
				if(el[i].checked)(score+=Number(el[i].dataset.pts))
				if(Number(el[i].dataset.pts)<0){el[i].parentElement.style.backgroundColor="#FDE5CF"}

			}
            
            document.getElementById("score").innerHTML = score + "/" + ###
        }
    </script>
</html>"""
#crée un fichier avec le même nom que le csv mais avec l'extension html
fo = open(sys.argv[1][0:-3]+'html', 'w' , encoding='utf8')
fo.write(header)
with open(sys.argv[1], 'r', encoding='ansi') as fi :
    for line in fi :
        fields = line.split(';')
        if flag == 0 :
            fo.write(f"<h1>{fields[0]}</h1><div><div>{fields[1]}</div>\n")
            flag = 1
        else :
            fo.write("<div class='block'>\n")
            fo.write(f"<input type='checkbox' data-pts='{fields[2]}'>\n")
            fo.write(f"<label for=''>{fields[0]}</label><br>\n")
            fo.write(f"<span class='reponse'>{fields[1]} : {fields[2]}pt(s) </span>\n")
            fo.write("</div>\n")
            if int(fields[2])>0 :
                maxi += int(fields[2])

fo.write(footer.replace("###", str(maxi)))
fo.close()