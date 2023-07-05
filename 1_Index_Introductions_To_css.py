/* In css We usually have a selector and declation

  slector{declaration}
       
 
 The selector usualyy points out which tag/element we are refering to
 While The declartion indicates things to be done on it

 Here,The  h1 is The selector

 The declarion is what is between The bractes I.e
 The property name and property value i.e color:red;
 We enclose the property name and value within brckets



 h1{
    color:red;
 }
 
 
 */





/*In css we select componets by id,classses or tages
   <!----****ID****----!>
 --we use # for id  ,then the name of the if e.g <p id='book'><p/>
--in css we refer to it by #book{}

   <!----****classes****----!>
   They can be used multiple times in a page
   We give the componet a class name and acept it in css by use of period i.e .
   e.g <p class='book'><p/> 
   in css .book{}

   <!----****tags****----!>
   Theu can only be used  once.They are unique
   We just refer to the tags in html and apply css to all components with same tag
   e.g in html <p>Hand bag<p/> 
                    <p>Groups<p/>
        in css To refer to all p tags 
               p{}

we use
*/


/*   Specificity  & Point system  & conflicting error & cascading system

In css thre maybe conflict of insterest due to 
selecters being for the same component
 e.g 
 p{
    color:red;
 }

 p{
    color:green;
 }
 Here css solves this by using cascding Flow.I.e It moves from up to down
 The selecter that is most down gets excuted I.e color greeen


    <!-----****---Point system---****----!>

    In css if the selcetors are for the same component ,It uses a pont system of specificty 
     id = 100
     class = 10
     tag = 1

     e.g To change The color of a p 

      <div id = 'book'>
        <p class= 'hen'>Hellow George Gacau</p>
        <p>Hellow George Gacau</p>
        <p>Hellow George Gacau</p>
        <div/>

#booK{                      <!----100 points ----!>
    color:red;
}

#book .hen{                  <!---- 110 points ----!>
    color:green;
}

#book p{                      <!----- 101 points ----!>
    color:white
}

p{                            <! ----- 1 Point -----!>
    color:blue
}



*/


/*     <!----**** Decndants ****---!>

All components within the body tag are decendants of the body tag
The h1 and div with id of pen rae decendants of the div with id of book
The p tag is a decendant of the div tag with an id of pen

in css 
To target a tag You can use the id or the inheritance tree

 using id to target the p tag
#pen p{
    color:red;
}
Using Inheritance to Target the p tage
#book #pen p{
    color:red;
}
This inheritance is not realyy adviced





        <body> 

            <div id ='book'>

                  <h1> hellow <h1/>

                  <div id='pen'> 
                      <p> Hellow three<p/>
                  
                  <div/>
            
            <div/>

        
        
        <body/>



*/

/*     <!-----****** Children and child selector *****------!>
The h1 and h2 are children  of the div tag with id of book
The p tag is the child of the div tag with the id of pen
The p tag is a grand child of the div tag with id of book
The div tag with id of book has no access to the p tag as the p tag is not its child
 For a tag to have access to its children only ,We use The child selector i.e >  This is the child selector


 E.g 
 # book > h2{          //This selects Only the h2 Tags That are direct children
    color:red;         of the div tag with id of book .This cannot touch the p tag
 }





<body> 

            <div id ='book'>

                  <h1> hellow <h1/>
                  <h2> Broo welcome <h2/>
                  <h2> Broo welcome <h2/>

                  <div id='pen'> 
                      <p> Hellow three<p/>
                  
                  <div/>
            
            <div/>

        
        
        <body/>






*/







/*       <!--------- ***** Making changes to Multiple Elements in css **** ----!>- 

This makes all selected componets have the specifiet styles,
This sves on time and space

p,h1,li,span{
    color:green;
    font-size:green;

}


*/
/*    <!----- **** ATribute selecter **** ----- !>

The name between square Brackets is the atribute.It is used to udentify tags in Html
It can be a class,id e.t.c


This Takes all tags with a class and clor Them red.It Does not care about The class Name >it takes all spn tags with 
a class and leaves those without
span[class]{
    color:red;
}

This Goes after ever div tag with an id atribute associeted with it

div[id]{
    color:green;
}

To geo after a specific tag ,Just include The name
This Goes after a specific div tag with the id of book
div[id='book']{
    color:blue;
}


To be specific about Things to go after e.g in html
    < href= http:/google.com title='search />
    < href= http:/books.pdf title='search />
    < href= http:/google.com title='search />

To go after Links ending with pdf

a[href$='pdf']{
    color:red;
}

To go after links Starting with http

a[href^='http']{
    color:green;
}




*/




/*   <!--------***** Pseudo classes ****------!>

     <!------- ***** Dynamic pseudo classes **** ------!>
  -- They Target behaviorioal states of an element
  E.g :hover
      :active
      :visited

This changes The color of the a tag on hovering over it
They are mostly used for links and buttons

a:hover{
    color:red
}

a:active{
    color:blue
}
a:visited{
    color:greenyellow;
}



or 
#book:hover{
    color:green;

}



       <!-----**** Structural Pseudo selectors ****-----!>

       ***first & last child ****

    This selects all div and clors greeen THe first p tag
e.g
       div p:first-child{
                color:green;
                }

    This sellects all div tags and colors The last p tag red

        div P:last-child{
            color:red
        }

        **** first of type & last of Type ****

        This selected The first of that type and color it green

        div p:first-of-type{
            color:green;
        }

          div p:last-of-type{
            color:green;
        }


        <!------- **** nth child selector **** ----!>

        This colors The seventh p tag in green

        p:nth-child(7){
            color:green;
        }

        This colors Both The nineth and seventh child selector red

        p:nth-child(7),nth-child(9){
            color:red
        }

        This colors The even p children blue

        P:nth-child(even){
            color:blue;
        }
        This colors The odd children yellow

           P:nth-child(even){
            color:yellow;
        }

        You can even put a math equation in the brackets
        N starts at 0, proceeds to 1,then 2 and so on
        This Puts a purple color on ever nth child where n = 3n+1 

        p:nth-child(3n+1){
            color:purple;
        }


        Nth of type .This tartgets The first of that type

        p:nth-of-type(2){
            color:green;
        }

        */


        /*  <!------ **** Combinide Selectors **** ------!>

        We may have may tags with the same classs name
        e.g <p class='book'> Hellow<p/>
            <div class='book'>Goodbye <div/>
        We can select one of these tags  that share same class name by
        using combine selectors

        This Gets all div tags with the class name of book

        div.booK{
            color:red;
        }

        <!-----**** The universal Selector ****-----!>

        The asterisk is the universal selector *
        This colors everything in collr blue

        *{
            color:blue;
        }







*/

/*
a:hover{
    color:red;
    
}
a:active{
    color:blue
}
a:visited{
    color:greenyellow;
}

#header{
    color:blue;

    

}

#header h1{
    color: greenyellow;
    font-size: medium;
    font-weight: 300;
}
#header p{
    color: black;
    font-size: medium;
    font-weight: 300;
}
p{
    color:coral;

}

a{
    text-decoration: underline;
    color: Green;
}
.deck{
    color:blueviolet

}

span{
    text-transform: uppercase;
    display: block;
    color:green
}






h4{
    background-color: brown;
}

h5{
    color:green;
}*/
*{
    margin: 0%;
}


p{
  margin-top: 40px auto;
  margin-bottom: 30px auto;
  margin-right: 20px auto;
  margin-left: 10px auto;
  
  padding-top: 40px;
  padding-bottom: 30px;
  padding-right: 20px;
  padding-left: 10px;
    
  border: 2px solid;
    

}
.box{
    background-color: aquamarine;
    width: 100%;
    height: 300px;
    background-color: rgb(16, 74, 124);
    background-image:url(./city.jpg),url(./get.jpg);
    background-repeat:no-repeat;
    background-size: 600px,10%;
    background-position: center,top left;
    background:-webkit-linear-gradient();
    
    
}




div{
    
    display: inline-block;
}





div[id]{
    font-family:"Yu gothic";
    font-weight: 800;
    text-transform:lowercase;
}
