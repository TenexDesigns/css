 Here we are going To Tali about The declaration
  slector{declaration}

  The declaration Has a 
  {
    property name:property value
  }

  The declaration can be in absoluute value i.e px  -pexels
                          or in relative value i.e em = 16px
                          or in percentage i.e percentage of em e.g 100% = 16px
                                                                    200% = 32px



    <!------ **** Declaring Font Stack **** -----!>

    We declare font family  for tags,But if The user does not have 
    Tha font ,we declare several more fonts for The user to fall on/use
    Incase The first one is note available.This is called a font stack
    e.g
    p{
        font-family:arial,roman,sanrif;        //This is a font stack
    }


     <!-----***** The Box Model ***** ------!>

     The box model has 
     Margin - The spacing Between Different elements
     Border - This encloses the elememnt
     padding - This is the spacing betweeen the elements and the border
     width - This is the hoeizontal lentgh of the elemnt
     height - This is the vertical lenth of the elemnt


     <! ---- **** HTML block level and inline elements **** ---- !>

     HTML elements can be divided into two categories :
       ---> block level 
      ----> inline elements.
     1.By default, block-level elements begin on new lines. e.g Three div elemnts
     2. HTML block level elements can appear in the body of an HTML page.
     3.It can contain another block level as well as inline elements.
        
        *******--- List of block level elements ----****
              
            p
            h1, h2, h3, h4, h5, h6
            ol, ul
            pre
            address
            blockquote
            dl
            div
            fieldset
            form
            hr
            noscript
            table

The list of HTML elements you provided represents a mix of block-level and inline-level elements. Block-level elements typically start on a new line and occupy the full width available, while inline-level elements do not start on a new line and only occupy the space needed for their content. Heres an explanation of each element and whether it is considered a block-level or inline-level element:

<p> (Paragraph): This is a block-level element used to define a paragraph of text.

<h1>, <h2>, <h3>, <h4>, <h5>, <h6> (Headings): These are block-level elements used to define different levels of headings, with <h1> being the highest and <h6> being the lowest.

<ol> (Ordered List) and <ul> (Unordered List): These are block-level elements used to define ordered and unordered lists, respectively.

<pre> (Preformatted Text): This is a block-level element used to preserve whitespace and display text exactly as it is written in the HTML source code.

<address> (Contact Information): This is a block-level element used to define contact information.

<blockquote> (Block Quote): This is a block-level element used to represent a section of quoted content.

<dl> (Definition List): This is a block-level element used to define a list of terms and their corresponding definitions.

<div> (Division): This is a block-level element used to logically group and style sections of content.

<fieldset> (Field Set): This is a block-level element used to group related form elements.

<form> (Form): This is a block-level element used to create a form for user input.

<hr> (Horizontal Rule): This is a block-level element used to insert a horizontal line to visually separate content.

<noscript> (No Script): This is a block-level element used to define alternative content to be displayed when JavaScript is disabled.

<table> (Table): This is a block-level element used to create a table structure with rows and columns.

It's important to note that the default display property of an element can be modified using CSS. For example, you can change a block-level element to behave as an inline-level element or vice versa by using CSS properties like display: inline or display: block.



      

      ******* ----- HTML inline elements -----*******
      1. By default, inline elements do not begin on new lines.
      They appear on the same line e.g Three span elemnts



      ****** ----- List of inline elements ------ *****

       span
       button
       label
       a        --ancor tag
       input
       strong
       textarea
       select
       img
       script
       map
       object
       acronym, abbr, cite, code, dfn, em, kbd, samp, var
       b, big, i, small, tt, bdo, br, q, sub, sup 

 The list of HTML elements you provided represents a variety of inline-level elements. Inline-level elements do not start on a new line and only occupy the space necessary for their content. Here's an explanation of each element:

<span>: This is an inline-level element used to apply styles to a specific portion of text or to group inline elements.

<button>: This is an inline-level element used to create a clickable button.

<label>: This is an inline-level element used to associate a text label with a form element.

<a> (Anchor): This is an inline-level element used to create hyperlinks to other web pages or specific parts of a page.

<input>: This is an inline-level element used to create various types of form input fields, such as text fields, checkboxes, radio buttons, etc.

<strong>: This is an inline-level element used to indicate strong importance or emphasis.

<textarea>: This is an inline-level element used to create a multi-line text input field.

<select>: This is an inline-level element used to create a dropdown list or selection box.

<img> (Image): This is an inline-level element used to display an image on the page.

<script>: This is an inline-level element used to embed or reference JavaScript code within an HTML document.

<map>: This is an inline-level element used in conjunction with <area> elements to create image maps.

<object>: This is an inline-level element used to embed multimedia content or external resources, such as audio, video, or interactive applications.

<acronym>, <abbr>, <cite>, <code>, <dfn>, <em>, <kbd>, <samp>, <var>: These are inline-level elements used to provide semantic meaning to specific types of content, such as abbreviations, citations, code snippets, definitions, emphasis, keyboard input, sample output, and variables.

<b>, <big>, <i>, <small>, <tt>, <bdo>, <br>, <q>, <sub>, <sup>: These are inline-level elements used for various formatting purposes, such as bold text, larger or smaller text, italicized text, monospace text, bidirectional text override, line breaks, inline quotes, subscript, and superscript.

These inline-level elements are commonly used to structure and style specific parts of a document, provide interactivity, handle user input, and present content in a visually appealing manner.

      How ever you can change the display of both inline and block elemnts by changing
      The display in css.
      e.g To change block elements to be displayed inline
      blockelement{
        display:inline-block;
      }
      To change inline elements to be displayed block
       inlineelement{
        display:block;
       }



       <!---- ***** Background image **** ------!>


       Do This for one background Image

       
        div{ 

             background-color: aquamarine;
             width: 100%;
             height: 300px;
             background-image:url(./city.jpg);
             background-repeat:no-repeat;
             background-size: 600px;
             background-position: center;
        }

        Do This for more Than one Background Image
        Note: Images are arranged in order of First come first shown
        I.e First Image Is top most image.
        This is important In sizing and positioning the image.
        This positionion,sizing e.tc are done in order of first come first serve
        e.g  background-image:url(./city.jpg),url(./get.jpg);
             background-size: 200px,600px;
        There the get.jpn image will be at The bottom and the city at the top
        Threfore The get.jpn Image is larger due to the 600px applied
        The city image is made smaller by 200px and is on top of the get image

             


       div{
             background-color: aquamarine;
             width: 100%;
             height: 300px;
             background-image:url(./city.jpg),url(./get.jpg);
             background-repeat:no-repeat;
             background-size: 600px,10%;
             background-position: center,top left;
          }


          }


          <!------- ***** Opacity **** ------ !>
          These show how transparent an element is.
          With opacity of 0 being completely transparent
                          1 being completely solid 

              p{
                backgroud color:red;        This wont be seen
                opacity:0;
              }

                p{
                backgroud color:red;        This will be a see through
                opacity:0.7;                 even the text will be see through
              }

                p{
                backgroud color:rgba(245,34,23,0.7);        To overcome the challenge of 
                                                            We use The rgb to color the bacground and add a proprety of a to contoll opaity
                                                            and not touch the text

              }


                p{
                backgroud color:red;        This will be seen as completely solid/ normal
                opacity:1;
                }


  <! --------***** Vendor Prefix ***** ------!>

  This are prefixex we put before declarition so that that declaration may work on a given browser
  Some browsers may not support certain declarions,so we put vendor prefixes to assisit in overcimg this

  e.g -moz for mozillar
      -o for oprea
      -webkit for safari and google chrome

  e.g -moz-linear-gradient() 


  <! ------****** Gradient *****---- !>

  This is the changing of e.g color from one color to another
  There are many  gradients and one of them is lineaar gradientd
  This signifies change in color from top to bottom
   to apply linear gradient

   linear-gradient (top,bottom, red, 0%,green,100%)

   This shows the two colors you want to change fromi.e red&green
   The TOP-BOTTOM shows from where to where you want to start changing
   The percentage shows from which percent of red to start from 0% most red  and which percent of green to reach ,100% i.e drakest


   If The linear gradient isnt supported by a certain browser ,you can use the vendor prefix
     -moz-linear-gradient(top,bottom, red, 0%,green,100%)   for mozzila fox
     -webkit-linear-gradient(top,bottom, red, 0%,green,100%)  for safari and chrome e.tc


     <!----- **** Box Shadow **** 
     The box Shadow Accepts six intakes 
     i.e
     horizontal       This is the x value or horizontal value of the shadow relative to the item the box shadow is being cast to . (positive pexels e.g 2px push the shadow to the right, Negative value e.g -2px push the shadow to the left
     vertical,        This is the y value or vertical value of the shadow relative to the item the box shadow is being cast to .(positive pexels e.g 2px push the shadow to the bottom, Negative value e.g -2px push the shadow to the top
     blur radius,     This is how blury the shdow is to be,The higher he number the more the blury,but i recoomend below 50,
     spread radius,   This is how far wide spread the box shadow is to be around the iten the box shadow is being cast .(positive pexels e.g 2px make the shadow bigger, Negative value e.g -2px make the shadow smaller  
     rgba()             i.e background color of shadow in rgb and opacity i.e a
                        e.g rgba(255,0,0,0.7) This has a red box shadow and the shaow has an opacity of 0.7
     
                        Note => ...... for more a practical overview visit the website  "https://www.cssmatic.com/box-shadow"





*/
